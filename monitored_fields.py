monitored_fields = {
    'ac_input_voltage': {
        'name': 'ac_input_voltage',
        'db_table': 'ac_input_voltage',
        'unit': 'V',
        'limits': {
            'min': 180,
            'max': 280
        },
        'graphable': True
    },
    'ac_input_frequency': {
        'name': 'ac_input_frequency',
        'db_table': 'ac_input_frequency',
        'unit': 'Hz',
        'limits': {
            'min': 30,
            'max': 70
        },
        'graphable': True
    },
    'ac_output_voltage': {
        'name': 'ac_output_voltage',
        'db_table': 'ac_output_voltage',
        'unit': 'V',
        'limits': {
            'min': 180,
            'max': 280
        },
        'graphable': True
    },
    'ac_output_frequency': {
        'name': 'ac_output_frequency',
        'db_table': 'ac_output_frequency',
        'unit': 'Hz',
        'limits': {
            'min': 30,
            'max': 70
        },
        'graphable': True
    },
    'ac_output_apparent_power': {
        'name': 'ac_output_apparent_power',
        'db_table': 'ac_output_apparent_power',
        'unit': 'Va',
        'limits': {
            'min': 0,
            'max': 7000
        },
        'graphable': True
    },
    'ac_output_active_power': {
        'name': 'ac_output_active_power',
        'db_table': 'ac_output_active_power',
        'unit': 'W',
        'limits': {
            'min': 0,
            'max': 6000
        },
        'graphable': True
    },
    'ac_output_load': {
        'name': 'ac_output_load',
        'db_table': 'ac_output_load',
        'unit': '?',
        'limits': {
            'min': 0,
            'max': 100
        },
        'graphable': True
    },
    'battery_voltage': {
        'name': 'battery_voltage',
        'db_table': 'battery_voltage',
        'unit': 'V',
        'limits': {
            'min': 40,
            'max': 62
        },
        'graphable': True
    },
    'battery_charging_current': {
        'name': 'battery_charging_current',
        'db_table': 'battery_charging_current',
        'unit': 'A',
        'limits': {
            'min': 0,
            'max': 130
        },
        'graphable': True
    },
    # 'bus_voltage': {
    #     'name': 'bus_voltage',
    #     'db_table': 'bus_voltage',
    #     'unit': 'V'
    # },
    'inverter_heat_sink_temperature': {
        'name': 'inverter_heat_sink_temperature',
        'db_table': 'inverter_heat_sink_temperature',
        'unit': 'C',
        'limits': {
            'min': -10,
            'max': 80
        },
        'graphable': True
    },
    'pv_input_current_for_battery': {
        'name': 'pv_input_current_for_battery',
        'db_table': 'pv_input_current_for_battery',
        'unit': 'A',
        'limits': {
            'min': 0,
            'max': 130
        },
        'graphable': True
    },
    'pv_input_voltage': {
        'name': 'pv_input_voltage',
        'db_table': 'pv_input_voltage',
        'unit': 'V',
        'limits': {
            'min': 0,
            'max': 450
        },
        'graphable': True
    },
    'battery_discharge_current': {
        'name': 'battery_discharge_current',
        'db_table': 'battery_discharge_current',
        'unit': 'A',
        'limits': {
            'min': 0,
            'max': 120
        },
        'graphable': True
    },
    'pv_input_power': {
        'name': 'pv_input_power',
        'db_table': 'pv_input_power',
        'unit': 'W',
        'limits': {
            'min': 0,
            'max': 6000
        },
        'graphable': True
    },
    'chargeaveragecurrent': {
        'name': 'chargeaveragecurrent',
        'db_table': 'chargeaveragecurrent',
        'unit': '?',
        'limits': {
            'min': 0,
            'max': 130
        },
        'graphable': True
    },
    'scc_pwm_temperature': {
        'name': 'scc_pwm_temperature',
        'db_table': 'scc_pwm_temperature',
        'unit': 'C',
        'limits': {
            'min': -10,
            'max': 80
        },
        'graphable': True
    },
    'inverter_temperature': {
        'name': 'inverter_temperature',
        'db_table': 'inverter_temperature',
        'unit': 'C',
        'limits': {
            'min': -10,
            'max': 80
        },
        'graphable': True
    },
    'battery_temperature': {
        'name': 'battery_temperature',
        'db_table': 'battery_temperature',
        'unit': 'C',
        'limits': {
            'min': -10,
            'max': 80
        },
        'graphable': True
    },
    'transformer_temperature': {
        'name': 'transformer_temperature',
        'db_table': 'transformer_temperature',
        'unit': 'C',
        'limits': {
            'min': -10,
            'max': 80
        },
        'graphable': True
    },
    'fan_lock_status': {
        'name': 'fan_lock_status',
        'db_table': 'fan_lock_status',
        'unit': 'NA',
        'graphable': False
    },
    'fan_pwm_speed': {
        'name': 'fan_pwm_speed',
        'db_table': 'fan_pwm_speed',
        'unit': '?',
        'limits': {
            'min': 0,
            'max': 105
        },
        'graphable': True
    },
    'scc_charge_power': {
        'name': 'scc_charge_power',
        'db_table': 'scc_charge_power',
        'unit': 'W',
        'limits': {
            'min': 0,
            'max': 6000
        },
        'graphable': True
    },
    'sync_frequency': {
        'name': 'sync_frequency',
        'db_table': 'sync_frequency',
        'unit': '?',
        'graphable': True,
        'limits': {
            'min': 0,
            'max': 100
        }
    },
    'inverter_charge_status': {
        'name': 'inverter_charge_status',
        'db_table': 'inverter_charge_status',
        'unit': 'NA',
        'graphable': False
    }
}