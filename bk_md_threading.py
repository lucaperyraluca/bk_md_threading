import paramiko
import time
from datetime import datetime
import threading


def backup(router,a):
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hours = now.hour

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    file_name = f'{router["hostname"]}_{year}_{month}_{day}.txt'

    print(f'Connecting to {router["hostname"]}')

    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()

    shell.send('terminal length 0\n')
    shell.send('enable\n')
    shell.send(enables[a])
    shell.send('show running-config\n')
    time.sleep(2)

    output = shell.recv(10000)
    output = output.decode('utf-8')
    output_list = output.splitlines()
    output_list = output_list[13:-1]
    output = '\n'.join(output_list)

    with open(file_name, 'w') as f:
        f.write(output)

    if ssh_client.get_transport().is_active() == True:
        ssh_client.close()
        print(f'Closing connection to {router["hostname"]}')




router1 = {'hostname': '192.168.122.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
router2 = {'hostname': '192.168.122.20', 'port': '22', 'username': 'u1', 'password': 'cisco'}
router3 = {'hostname': '192.168.122.30', 'port': '22', 'username': 'u1', 'password': 'cisco'}

routers = [router1, router2, router3]




threads = list()
counter = 0
for router in routers:
    # Here you need to change the 'enable' password values ​​for each device. Note that it must have the same order as the 'routers'
    enables = ['cisco2\n', 'cisco4\n', 'cisco3\n']
    th = threading.Thread(target=backup, args=(router,counter,))
    threads.append(th)
    counter=counter+1

for th in threads:
    th.start()

for th in threads:
    th.join()
