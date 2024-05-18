import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
import yaml
from jinja2 import Environment,FileSystemLoader
env = Environment(loader=FileSystemLoader("."))
temp = env.get_template("pgb.j2")
temp1 = env.get_template("ospf.j2")
temp2 = env.get_template("static routing.j2 ")
inp = input("to run pgb enter 1 \n to run ospf enter 2 \n to run static routing enter 3 ")
if int(inp)==1:
     with open("pgb.yml") as pgb:
        date1 = yaml.full_load(pgb)
     output=temp.render(int=date1)

elif int(inp)==2:
     with open("ospf.yml") as ospf:
         date = yaml.full_load(ospf)
     output=temp1.render(int=date)
else:
     with open("static routing.yml") as file1:
         date3 = yaml.full_load(file1)
     output = temp2.render(int=date3)
print(output)

sh = input("to run netmiko enter 1 \n to run paramiko enter 2 ")
if int(sh)==1:
    from netmiko import ConnectHandler
    vxr=ConnectHandler(host="192.168.1.15",username="youssef",password="welcome",secret="1234",device_type="cisco_ios")
    print(vxr.find_prompt())
    vxr.enable()
    print(vxr.find_prompt())
    vxr.config_mode()
    print(vxr.find_prompt())
    show=vxr.send_command_timing(output)
    print(show)
else:
    ssh.connect(hostname='192.168.1.15',port=22,username='youssef',password='welcome')
    cli=ssh.invoke_shell()
    cli.send("en \n")
    cli.send("1234" + "\n")
    cli.send("config t \n")
    cli.send(output)
    time.sleep(6)
    er=cli.recv(999999).decode()
    print(er)