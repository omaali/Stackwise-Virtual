from netmiko import ConnectHandler

USERNAME = 'username'  # edit to reflect
PASSWORD = 'password'  # edit to reflect
DEVICES = ['xxx.xxx.xxx.xxx', 'xxx.xxx.xxx.xxx']  # edit to reflect
PORT = 000  # edit to reflect

for device in DEVICES:
    m = ConnectHandler(device_type='cisco_ios', ip=device, username=USERNAME, password=PASSWORD)
    m.send_command('terminal length 0')  # max timeout
    m.send_command('enable')  # Editable to be what ever is needed
    m.send_config_set(['stackwise-virtual', 'domain 10'])
    m.send_config_set(['interface range te2/0/1-2', 'stackwise-virtual link 1'])
    m.send_config_set(['interface te2/0/3', 'stackwise-virtual dual-active-detection'])
    m.send_config_set(['do wr'])
    m.send_config_set(['do reload', 'yes'])
