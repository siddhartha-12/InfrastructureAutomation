import csv
import threading
from getpass import getpass
from netmiko import ConnectHandler
from operator import itemgetter
import random
import ipaddress
import sys
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
    output = net_connect.send_command('show ip int brief', use_textfsm=True)
    l = len(output)
    downInterface = []
    for i in range(0,l):
        if output[i]['status'] != 'up':
            downInterface.append(output[i]['intf'])
    print("\nTotal down interfaces " + str(len(downInterface)))
    count = 0
    modifiedInterface = []
    print("\nCheck 2 for router "+router)
    i=0
    while(downInterface and i<2):
        random.shuffle(downInterface)
        changeInterface = downInterface.pop()
        net_connect.enable()
        ip_address = str(ipaddress.IPv4Address(random.randint(0,2 ** 32)))
        print("assigning IP " + str(ip_address) + " to interface "+changeInterface+" on router " +router +"\n")
        cfCommands = ['config t','interface '+str(changeInterface),'ip add '+ str(ip_address) + ' 255.255.255.0','no shut','exit','exit']
        net_connect.send_config_set(cfCommands)
        i+=1

    output = net_connect.send_command('show ip int brie', use_textfsm=True)
    l = len(output)
    print("\nCheck 3 for router "+router)
    upInterface = [("-----Config of router with IP----- "+router +"\n")]
    for i in range(0,l):
        if output[i]['status'] == 'up':
            upInterface.append("Interface - " + output[i]['intf'] + " | Ip-Address - " + output[i]['ipaddr'] +" | Status - " + output[i]['status'] + " | Protocol - " + output[i]['proto'] + "\n")
    f = open("interfaces.txt", "a")
    f.writelines(upInterface)
    f.close()
    print("\nCheck 4 for router "+router)
    

if __name__ == "__main__":
    for router in routers:
        my_thread = threading.Thread(target=main, args=(router,))
        my_thread.setDaemon(True)
        my_thread.start()
    print("\nThreads created. Starting thread!!!\n")
    main_thread = threading.currentThread()
    time.sleep(3)
    print("Program Ended")
