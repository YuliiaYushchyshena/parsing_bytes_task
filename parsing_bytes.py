import sys

test_data = [("10FA0E00", {'field1': 'Low',
                           'field2': '00',
                           'field3': '01',
                           'field4': '00',
                           'field5': '00',
                           'field6': '01',
                           'field7': '00',
                           'field8': 'Very High',
                           'field9': '00',
                           'field10': '00'}),
             ]

# Format settings - array [sett_byte1 as dict {bit: [size, 'field_name']}, sett_byte2, sett_byte3, sett_byte4]
device_settings = [{0: [3, 'field1'],
                    3: [1, 'field2'],
                    4: [1, 'field3'],
                    5: [3, 'field4']},
                   {0: [1, 'field5'],
                    1: [1, 'field6'],
                    2: [1, 'field7'],
                    3: [3, 'field8'],
                    },
                   {0: [1, 'field9'],
                    5: [1, 'field10']
                    },
                   {}
                   ]

field1 = {'0': 'Low',
          '1': 'reserved',
          '2': 'reserved',
          '3': 'reserved',
          '4': 'Medium',
          '5': 'reserved',
          '6': 'reserved',
          '7': 'High',
          }
field4 = {'0': '00',
          '1': '10',
          '2': '20',
          '3': '30',
          '4': '40',
          '5': '50',
          '6': '60',
          '7': '70',
          }
field8 = {'0': 'Very Low',
          '1': 'reserved',
          '2': 'Low',
          '3': 'reserved',
          '4': 'Medium',
          '5': 'High',
          '6': 'reserved',
          '7': 'Very High',
          }

field_mask_values = {'1': 0x01,
                     '3': 0x07}


def get_data_from_payload(payload):
    keys = []
    for setting in device_settings:
        [keys.append(value[1]) for value in setting.values()]
    parsed_data = dict.fromkeys(keys)
    try:
        input_bytes = bytearray.fromhex(payload)
    except ValueError:
        sys.stderr.write('Invalid payload')
        sys.exit(1)
    for sett_byte in device_settings:
        for key, value in sett_byte.items():
            byte_index = device_settings.index(sett_byte)
            field_position = key
            field_mask = field_mask_values.get(str(value[0]))
            # expression for field value calculation
            # (payload >> position) & mask
            field_value = (input_bytes[byte_index] >> field_position) & field_mask
            if value[1] in ['field1', 'field4', 'field8']:
                parsed_data[value[1]] = (eval(value[1])).get(str(field_value))
                continue
            parsed_data[value[1]] = format(field_value, '02x')

    return parsed_data


if __name__ == '__main__':
    input_data = '10FA0E00'
    data = get_data_from_payload(input_data)
    print(input_data, data)
