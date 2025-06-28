import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Kiểm tra và cài đặt thư viện cần thiết
try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import pystyle
except ImportError:
    os.system("pip install faker requests colorama bs4 pystyle")
    os.system("pip3 install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()

# Tạo hoặc đọc khóa mã hóa bằng base64
secret_key = base64.urlsafe_b64encode(os.urandom(32))

# Mã hóa và giải mã dữ liệu bằng base64
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

# Màu sắc cho hiển thị
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
end = '\033[0m'

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""
\033[1;33m██╗░░░██╗███╗░░██╗░██████╗░██╗░░██╗██╗░█████╗░
\033[1;35m██║░░░██║████╗░██║██╔════╝░██║░░██║██║██╔══██╗
\033[1;36m██║░░░██║██╔██╗██║██║░░██╗░███████║██║███████║
\033[1;37m██║░░░██║██║╚████║██║░░╚██╗██╔══██║██║██╔══██║
\033[1;32m╚██████╔╝██║░╚███║╚██████╔╝██║░░██║██║██║░░██║
\033[1;31m░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝\n
\033[1;97mTool By: \033[1;32mUÔNG NGHĨA            \033[1;97mPhiên Bản: \033[1;32mV4    
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
print("\033[1;31m────────────────────────────────────────────────────────────")
print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║  Tool Spam Sms      ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════╝"))
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1.1\033[1;31m] \033[1;32mTOOL SPAM SMS \033[1;33m[\033[1;31mV1\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m1.2\033[1;31m] \033[1;32mTOOL SPAM SMS \033[1;33m[\033[1;31mV2\033[1;33m] ")
print("\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;31m[\033[1;33m00\033[1;31m] \033[1;32mTHOÁT TOOL")

print("\033[1;31m────────────────────────────────────────────────────────────")

chon = str(input('\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;37m: \033[1;33m'))


if chon == '00' :
    exec(requests.get('https://raw.githubusercontent.com/unghia11/gopv4/4f46ff6d1d92d529341c6185993a505692b8f480/00.py').text)
if chon == '1.1' :
    exec(requests.get('https://raw.githubusercontent.com/unghia11/gopv4/refs/heads/main/2.1.py').text)
if chon == '1.2' :
    exec(requests.get('https://raw.githubusercontent.com/unghia11/gop/refs/heads/main/2.2.py').text)
else:
    exit()
