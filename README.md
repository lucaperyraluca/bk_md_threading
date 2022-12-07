# bk_md_threading
This script backs up multiple Cisco devices at once, using multithreading. For its use, you must replace (or add/remove) the values in 
router1, router2 etc:

router1 = {'hostname': '192.168.122.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
router2 = {'hostname': '192.168.122.20', 'port': '22', 'username': 'u1', 'password': 'cisco'}
router3 = {'hostname': '192.168.122.30', 'port': '22', 'username': 'u1', 'password': 'cisco'}

with those corresponding to the devices you want to back up.

Also, you must take in mind that you must specify the 'enable' password. That is substituted into the list called 'enables', and should follow the same order as the routers:

enables = ['cisco2\n', 'cisco4\n', 'cisco3\n']

