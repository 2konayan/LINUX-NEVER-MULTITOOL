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
    "Hackers rule the world, be a part of them.",
    "Keep calm and hack ethically."
]

print(Fore.YELLOW + random.choice(quotes))
print(Style.RESET_ALL)

option = input("""1.NMAP PORT SCAN
         2.PINGER
         3.SYN DOS
         4.MAC SPOOFING
         5.WHOIS INFO
         6.NSLOOKUP
         7.EXIT NEVER
         """)

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
    target_ip = input("What is the target's ip? ")
    os.system("whois " + target_ip)
elif option == "6":
    target_ip = input("What is the domain you want to lookup? ")
    os.system("nslookup " + target_ip)
elif option == "7":
    exit()