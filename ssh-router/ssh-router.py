# SSH to Multiple Devices from devices file
from netmiko import ConnectHandler
# importing netmiko connection handler
with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'geordie',
            'password': 'teabag22'
        }
#above is opening a file called device.txt and using the details in the file and alias it to router
        net_connect = ConnectHandler(**Router)
#above is using netmiko connection handler to connect to the devices related to Router
        print ('Connecting to ' + IP)
        print('-'*79)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*79)
#above is going to print the output on the screen and send the command to the router
net_connect.disconnect()
# Finally the script will close the SSH connection to the device