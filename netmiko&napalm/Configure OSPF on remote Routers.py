from netmiko import ConnectHandler
for ip in ['192.168.229.10','192.168.229.11','192.168.229.13','192.168.229.14']:
#for ip in ['192.168.229.10']:
    cisco_881 = {
        'device_type': 'cisco_ios',
        'host':   ip,
        'username': 'admin',
        'password': 'admin',
        'secret': 'admin',
    }
    net_connect = ConnectHandler(**cisco_881)
    net_connect.enable()
    if(ip == '192.168.229.10'):
        filename = "R1.txt"
        router = "R1"
    elif(ip == '192.168.229.11'):
        filename = "R2.txt"
        router = "R2"
    elif(ip == '192.168.229.13'):
        filename = "R3.txt"
        router = "R3"
    elif(ip == '192.168.229.14'):
        filename = "R4.txt"
        router = "R4"   
    print("----- Configuring router "+router+"------\nChecking for file " + filename)
    if(filename):
        print("Sending configs to " + router)
        net_connect.send_config_from_file(filename)
        print(router + " Config done. Closing connection ")
    net_connect.disconnect()
    print("Connection closed")
