from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host":'nxos2.lasthop.io',
    "device_type": 'cisco_nxos',
    "username": 'pyclass',
    "password": getpass(),
    #"session_log": 'firstconnect.txt',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
