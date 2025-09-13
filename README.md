# SolarViewerDiscord
This basic discord bot is designed to render data captured by [GitHub.com/AlexVerrico/SolarMonitor](https://github.com/AlexVerrico/SolarMonitor) into basic graphs.  
To get started, you will need to know your discord guild ID for the server you want to add the bot to.   
If you access your server through the discord web app, this is the long number displayed after /channels/, eg. 1234 in the following example url (although a real guild ID is much longer): https://discord.com/channels/1234/5678
You will also need to have [GitHub.com/AlexVerrico/SolarMonitor](https://github.com/AlexVerrico/SolarMonitor) configured and running to create & populate the database file.  
You will also need a discord bot token with the "Message Content Intent" enabled, attached to an application with the "application.commands" and "bot" scopes, and "Attach Files", "Connect", "Change Nickname", "Embed Links", and "Send Messages" permissions.  
Does it actually need all of those permissions? I suspect it doesn't need the change nickname or embed links perms, but haven't tested to confirm.  
Set up the python environment using venv - `python -m venv .venv && ./.venv/bin/python -m pip install -r requirements.txt` (this command may need to be adjusted if you are not running on Linux) 
Once you have all of this, copy config.example.py to config.py, and add your config values, then start the bot using python main.py
