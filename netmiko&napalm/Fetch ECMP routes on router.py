import csv
import threading
from getpass import getpass
from netmiko import ConnectHandler
from operator import itemgetter
import json
import time
 
USER = 'admin'
PASSWORD = 'admin'
SECRET = 'admin'
routers = ["192.168.229.10","192.168.229.11"]
#routers = ["192.168.229.10"]
def main(router):
    print("\nCheck 1 for router "+router)
    routerl = {'device_type': 'cisco_ios', 'ip': router, 'username': USER, 'password': PASSWORD,'secret':SECRET, 'verbose': False, }
    net_connect = ConnectHandler(**routerl)
    output = net_connect.send_command('show ip route ospf')
##    l = len(output)
##    ecmpOutput = ""
##    for i in range(0,l):
##        if output[i]['protocol'] =="O":
##            ecmpOutput+= json.dumps(output[i],indent=2)
##    print(router +" -----\n"+ ecmpOutput)
    print(output)

if __name__ == "__main__":
    for router in routers:
        print(str(router))
        my_thread = threading.Thread(target=main, args=(router,))
        my_thread.setDaemon(True)
        my_thread.start()
    print("\nThreads created. Starting thread!!!\n")
    main_thread = threading.currentThread()
    time.sleep(3)
    print("Program Ended")
