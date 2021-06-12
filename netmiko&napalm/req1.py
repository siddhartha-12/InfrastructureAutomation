from netmiko import ConnectHandler
import re

for ip in ['192.168.229.10','192.168.229.11']:
    cisco_881 = {
        'device_type': 'cisco_ios',
        'host':   ip,
        'username': 'admin',
        'password': 'admin',
    }
    net_connect = ConnectHandler(**cisco_881)
    interface = net_connect.send_command('show ip int brief')
    print(interface)

    output = net_connect.send_command('show version')
    #finding hostname in output using regular expressions
    regex_hostname = re.compile(r'(\S+)\suptime')
    hostname = regex_hostname.findall(output)

    #finding uptime in output using regular expressions
    regex_uptime = re.compile(r'\S+\suptime\sis\s(.+)')
    uptime = regex_uptime.findall(output)

    #finding version in output using regular expressions
    regex_version = re.compile(r'Cisco\sIOS\sSoftware.+Version\s([^,]+)')
    version = regex_version.findall(output)

    print("Hostname : "+ hostname[0] + "\nuptime : "+ uptime[0]+"\nversion : "+version[0])
