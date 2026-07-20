import pyfiglet
import os
text = pyfiglet.figlet_format("NEVER MULTITOOL")
print(text)
print("EDUCATIONAL PURPOSES ONLYY!!!")
option = input("""1.NMAP PORT SCAN
         2.PINGER
         3. Close NEVER """)
if option == "1":
    target_ip = input("What is the target's ip")
    os.system("nmap " + target_ip)
elif option == "2":
    target_ip = input("What is the ip of the system you Wanna ping?")
    os.system("ping " + target_ip)
elif option == "3":
    exit()