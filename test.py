from netmiko import ConnectHandler
vxr=ConnectHandler(host="192.168.126.206",username="youssef",password="Welcome@2024",device_type="cisco_ios")
print(vxr.find_prompt())
vxr.enable()
print(vxr.find_prompt())
vxr.config_mode()
print(vxr.find_prompt())
show=vxr.send_command_timing("do sh ip in br")
print(show)

print("hello")