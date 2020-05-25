import pytest
from parsing_bytes import get_data_from_payload
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
             ("00000000", {'field1': 'Low',
                           'field2': '00',
                           'field3': '00',
                           'field4': '00',
                           'field5': '00',
                           'field6': '00',
                           'field7': '00',
                           'field8': 'Very Low',
                           'field9': '00',
                           'field10': '00'}),
             ("FFFFFFFF", {'field1': 'High',
                           'field2': '01',
                           'field3': '01',
                           'field4': '70',
                           'field5': '01',
                           'field6': '01',
                           'field7': '01',
                           'field8': 'Very High',
                           'field9': '01',
                           'field10': '01'})]


@pytest.mark.parametrize("payload, expected", test_data)
def test_payload_check(payload, expected):
    assert get_data_from_payload(payload) == expected
