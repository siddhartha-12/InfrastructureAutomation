from napalm import get_network_driver
import json
driver = get_network_driver('ios')
optional = {'secret': 'admin'}

device = driver('192.168.229.10', 'admin', 'admin',optional_args=optional)
device.open()
print("\n-------Printing ARP Table--------\n")
result = device.get_arp_table(vrf='')
for element in result:
    del element['interface']
arpTable = json.dumps(result, indent=4)
f = open("arp.txt", "w")
data = ["-------- Router 1 ARP table--------",arpTable]
f.writelines(data)
f.close()
print(arpTable)
device.close()

destination = '192.168.229.13'
device = driver(destination, 'admin', 'admin',optional_args=optional)
device.open()
result = device.ping(destination, source='', ttl=255, timeout=2, size=1000, count=10, vrf='')
rrtAvg = result['success']['rtt_min']
rrtMax = result['success']['rtt_max']
rrtMin = result['success']['rtt_min']
print("\n-------Printing RTT Values--------\n")
f = open("ping.txt", "w")
data = "RTTavg - "+str(rrtAvg) + "\nRTTmax - "+str(rrtMax) + "\nRTTmin - "+str(rrtMin)
f.writelines(data)
f.close()
device.close()
print(data)
