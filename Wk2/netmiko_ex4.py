import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime

password = os.getenv("pnpass") if os.getenv("pnpass") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    #"fast_cli": True,
}

net_connect = ConnectHandler(**device)

print()
cmds = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]
# for cmd in cmds:
output = net_connect.send_config_set(cmds)
print("#" * 80)
print(cmds)
print("#" * 80)
pprint(output)
print("#" * 80)

print()

#if cmd == "show lldp neighbors":
#    print("LLDP Data Structure Type: {}".format(type(output)))
#    print("HPE Switch Connection Port: {}".format(output[0]["neighbor_interface"]))

#print()

start_time = datetime.now()

ping_output = net_connect.send_command("ping google.com")
if "!!" in ping_output:
    print("Ping Successful:")
    print("\n\nPing Output: {}\n\n".format(ping_output))
else:
    raise ValueError("\n\nPing Failed: {}\n\n".format(ping_output))
net_connect.disconnect()

end_time = datetime.now()
print("Total Execution Time: {}\n".format(end_time - start_time))

