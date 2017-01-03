import paramiko
import time
import getpass
import os
from host_seedfile import network_devices

 
UN = raw_input("Username : ")
PW = getpass.getpass("Password : ")
 
 
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
    print "Interactive SSH session established"
    remote.send("\n")
    remote.send("show configuration\n")
    time.sleep(2)
    remote.send("sh cdp nei\n")
    remote.send("\n")
    time.sleep(2)
    buf = remote.recv(65000)
    print buf
    f = open('sshlogfile0010.txt', 'a')
    f.write(buf)
    f.close()
    twrssh.close()
