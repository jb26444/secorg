import paramiko
import time
import getpass
import os
from host_seedfile import network_devices
from host_config_file import host_conf

 
UN = raw_input("Username : ")
PW = getpass.getpass("Password : ")
FN = raw_input("File-name : ")
 
 
#This For loop calls host list in the seed file "hostlist_script.py"
for ip in  network_devices:
    print ip
    twrssh = paramiko.SSHClient()
    twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    twrssh.connect(ip, port=22, username=UN, password=PW)
    remote = twrssh.invoke_shell()
    remote.send('term len 0\n')
    time.sleep(1)
    #This for loop uses config file 'host_config1.py' to enter commands one by one
    for command in host_conf:
        remote.send(' %s \n' % command)
        time.sleep(2)
        buf = remote.recv(65000)
        print buf
        f = open(FN, 'a')
        f.write(buf)
        f.close()
    twrssh.close()
