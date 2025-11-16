import sqlite3
from datetime import datetime, timedelta
import discord
from discord import app_commands
from matplotlib import pyplot as plt
import tempfile

import config
from monitored_fields import monitored_fields

MY_GUILD = discord.Object(id=config.DISCORD_GUILD_ID)
db_file = config.SQLITE_DB_PATH


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application
        # command state required to make it work. This is a separate class
        # because it allows all the extra state to be opt-in. Whenever you
        # want to work with application commands, your tree is used to store
        # and work with them. Note: When using commands.Bot instead of
        # discord.Client, the bot will maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)
    # In this basic example, we just synchronize the app commands to one
    # guild. Instead of specifying a guild to every command, we copy over
    # our global commands instead. By doing so, we don't have to wait up to
    # an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

client = MyClient(intents=discord.Intents.default())

component_choices = [
    app_commands.Choice(name=x, value=x) for x in monitored_fields.keys()
]

@client.tree.command()
@app_commands.describe(
    component='Component to graph, eg. batteries, panels, controller',
    hours='How many hours to graph'
)
@app_commands.choices(
    component=component_choices
)
async def graph(interaction: discord.Interaction, component: str, hours: int):
    await interaction.response.defer(ephemeral=True, thinking=True)
    if component not in monitored_fields.keys():
        await interaction.followup.send(f'Unsupported component')
    elif monitored_fields[component].get('graphable', False) is not True:
        await interaction.followup.send(f'Ungraphable component')
    else:

        now = datetime.utcnow().timestamp()
        start_timestamp = now - hours * 60 * 60
        end_timestamp = now
        if hours <= 6:
            granularity = 1  * 60
        elif 6 < hours <= 12:
            granularity = 5 * 60
        elif 24 >= hours > 12:
            granularity = 10 * 60
        else:
            granularity = 60 * 60

        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"""SELECT * FROM main.inverter_records WHERE timestamp > {start_timestamp} AND timestamp < {end_timestamp} AND data_type = '{component}' ORDER BY timestamp ASC""")
            data = cursor.fetchall()

        def transform_date(timestamp):
            x = datetime.fromtimestamp(timestamp) + timedelta(hours=10)
            y = x.isoformat().split('T')[1].rsplit(':', 1)[0]
            return y

        output = [
            (data[0][0], data[0][1], data[0][2], transform_date(data[0][0])),
        ]
        last_row = None
        for row in data:
            if row[0] > output[-1][0] + granularity:
                output.append((row[0], row[1], row[2], transform_date(row[0])))
            last_row = row
        output.append((last_row[0], last_row[1], last_row[2], transform_date(last_row[0])))

        fig = plt.figure(dpi=128, figsize=(16, 9))
        plt.title(f'{component} - {hours} hours to {str(datetime.fromtimestamp(output[-1][0]) + timedelta(hours=10))}', fontsize=24)
        plt.plot([row[3] for row in output], [row[2] for row in output])
        last_annotated = None
        count_since_annotated = 0
        for row in output:
            count_since_annotated += 1
            if last_annotated == row[2] and count_since_annotated < 5:
                continue
            if last_annotated is not None and count_since_annotated < 5:
                if last_annotated * 1.01 > row[2] > last_annotated * 0.999:
                    continue
            plt.annotate(xy=(transform_date(row[0]), row[2]), text=row[2])
            last_annotated = row[2]
            count_since_annotated = 0
        plt.ylim(monitored_fields[component]['limits']['min'], monitored_fields[component]['limits']['max'])
        plt.xlabel('Time', fontsize=16)
        plt.ylabel(monitored_fields[component]['unit'], fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=6)
        plt.legend()

        with tempfile.TemporaryFile() as x:
            fig.savefig(x, format='png')
            x.seek(0)
            file = discord.File(x, filename='graph.png')

            await interaction.followup.send(f'', files=[file, ])


with sqlite3.connect(db_file) as _conn:
    _cursor = _conn.cursor()
    _cursor.execute("""SELECT * FROM main.db_version LIMIT 1""")
    version = _cursor.fetchone()[0]
    if version != 2:
        print(f'Invalid DB version {version}')
        exit(1)

client.run(config.DISCORD_BOT_TOKEN)
