import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from pprint import pprint

password = os.getenv("pnpass") if os.getenv("pnpass") else getpass()

<<<<<<< HEAD
start_time = datetime.now()
device = {
    "host": "nxos1.lasthop.io",
=======
#start_time = datetime.now()
device = {
    "host": "nxos2.lasthop.io",
>>>>>>> fc24601651582c2f2d2919179e261e1ba0ccdf96
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    # "fast_cli": True,
}

net_connect = ConnectHandler(**device)

<<<<<<< HEAD
cmds = ["sh vlan brief"]
=======
cmds = ["sh vlan summary"]
>>>>>>> fc24601651582c2f2d2919179e261e1ba0ccdf96
for cmd in cmds:
    output = net_connect.send_command(cmd, use_textfsm=True)
    print()
    print("#" * 80)
    print("CFG Change: ")
    pprint(output)
    print("#" * 80)
    print()

<<<<<<< HEAD

=======
>>>>>>> fc24601651582c2f2d2919179e261e1ba0ccdf96
