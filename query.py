import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from pprint import pprint

password = os.getenv("pnpass") if os.getenv("pnpass") else getpass()

#start_time = datetime.now()
device = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    # "fast_cli": True,
}

net_connect = ConnectHandler(**device)

cmds = ["sh vlan summary"]
for cmd in cmds:
    output = net_connect.send_command(cmd, use_textfsm=True)
    print()
    print("#" * 80)
    print("CFG Change: ")
    pprint(output)
    print("#" * 80)
    print()

