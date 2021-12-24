#Using netmiko to backup a device, using getpass to prompt for password
from netmiko import ConnectHandler
from getpass import getpass

username = input('Username: ')
password = getpass()

CSR = {
    'device_type': 'cisco_ios',
    'ip': '1.1.1.1',
    'password': password, 
    'username': username
}
#you will be prompted to provide your username and password when the script runs

net_connect = ConnectHandler(**CSR)

print('-'*79)
print('Saving Config ')
print('-'*79)

output = net_connect.save_config()
print(output)

print('-'*79)
print('Config Saved ')
print('-'*79)