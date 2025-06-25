import time
from time import strftime
import os
import sys
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import base64
import requests
import os
import subprocess
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
# màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
os.system("cls" if os.name == "nt" else "clear")

# đánh dấu bản quyền
ndp_tool = "\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

def banner():
    banner = f"""
\033[1;33m██╗░░░██╗███╗░░██╗░██████╗░██╗░░██╗██╗░█████╗░
\033[1;35m██║░░░██║████╗░██║██╔════╝░██║░░██║██║██╔══██╗
\033[36m██║░░░██║██╔██╗██║██║░░██╗░███████║██║███████║
\033[1;37m██║░░░██║██║╚████║██║░░╚██╗██╔══██║██║██╔══██║
\033[1;32m╚██████╔╝██║░╚███║╚██████╔╝██║░░██║██║██║░░██║
\033[1;31m░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝\n
\033[1;97mTool By: \033[1;32mUNGHIA            \033[1;97mPhiên Bản: \033[1;32mV4    
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;95m FB\033[1;31m : \033[1;36mhttps://www.facebook.com/ungnghiaA/
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;93m YOUTUBE\033[1;31m : \033[1;32mᰔᩚυиɢнĩα
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;32m ADMIN\033[1;31m : \033[1;33mUNGHIA
\033[97m════════════════════════════════════════════════  
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)

os.system("cls" if os.name == "nt" else "clear")
banner()
print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║Tool Aotu Golike         ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════════╝"))
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1.1\033[1;31m] \033[1;32mTool Auto TikTok")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1.2\033[1;31m] \033[1;32mTool Auto Instagram ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1.3\033[1;31m] \033[1;32mTool Auto Twitter")
if chon == '1.1' :  
    exec(requests.get('https://raw.githubusercontent.com/unghia11/gopv4/refs/heads/main/6.1.py').text)
if chon == '1.2' :
    exec(requests.get('https://raw.githubusercontent.com/unghia11/gopv4/refs/heads/main/6.2.py').text)
if chon == '1.3' :
     exec(requests.get('https://raw.githubusercontent.com/unghia11/gopv4/refs/heads/main/6.3.py').text)
else:
  exit()
