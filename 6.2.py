import requests
import time
import sys
import os 
import time
import json
import random
from time import sleep
try:    
    from tabulate import tabulate
    from art import *
    from colorama import Fore
except ImportError:
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        colors = [
                "\033[1;37mU\033[1;36mN\033[1;35mG \033[1;32mH\033[1;31mI\033[1;34mA",
                "\033[1;37mU\033[1;36mN\033[1;35mG \033[1;32mH\033[1;31mI\033[1;34mA",
                "\033[1;37mU\033[1;36mN\033[1;35mG \033[1;32mH\033[1;31mI\033[1;34mA",
                "\033[1;37mU\033[1;36mN\033[1;35mG \033[1;32mH\033[1;31mI\033[1;34mA",
                "\033[1;37mU\033[1;36mN\033[1;35mG \033[1;32mH\033[1;31mI\033[1;34mA",
                "\033[1;37mU\033[1;36mN\033[1;35mG \033[1;32mH\033[1;31mI\033[1;34mA",
                "\033[1;37mU\033[1;36mN\033[1;35mG \033[1;32mH\033[1;31mI\033[1;34mA",
        ]
        for color in colors:
            print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
            time.sleep(0.12)
                                  
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ",end = "\r")
from colorama import Fore
def INSTAGRAM():
    url1_2 = 'https://gateway.golike.net/api/instagram-account'
    checkurl1_2 = ses.get(url1_2,headers=headers).json()
    user_INS = []
    account_id1 = []
    account = []
    STT = []
    STATUS =[]
    tong = 0
    dem = 0
    i = 1
    for data in checkurl1_2['data'] :
        usernametk = data['instagram_username']
        user_INS.append(data['username'])
        account_id1.append(data['id'])
        STT.append(i)
        STATUS.append(Fore.GREEN+"Hoạt Động"+Fore.RED)
        account.append(usernametk)
        print(f'\033[1;97m•[🌸]➭\033[1;36m [{i}] \033[1;91m=> \033[1;97mTên Tài Khoản┊\033[1;32m🌸 :\033[1;93m {usernametk} \033[1;91m=> \033[1;97mStatus|\033[1;32m🌸 :\033[1;93m {STATUS[-1]}')      
        i += 1
    print(Fore.RED+'_________________________________________________________')    
    choose = int(input('\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  Nhập Tài Khoản : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_INS) :
        user_INS = user_INS[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_INS[0] 
        account_id = account_id1[0]
        checkfile2 = os.path.isfile('COOKIEINS'+str(account_id)+'.txt')
        if checkfile2 == False:
            banner()
            cookieX = input(Fore.GREEN+'\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  Nhập Cookie Instagram: ')
            createfile = open('COOKIEINS'+str(account_id)+'.txt','w')
            createfile.write(cookieX)
            createfile.close()
            readfile = open('COOKIEINS'+str(account_id)+'.txt','r')
            cookieINS = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIEINS'+str(account_id)+'.txt','r')
            cookieINS = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        banner()
        choose = int(input(Fore.RED+'\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  Nhập Số Lượng Job : '))
        headerINS = {
                'accept': '*/*',
                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                # 'content-length': '0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookieINS,
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/p/C9RAZEJNjPC/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                'x-asbd-id': '129477',
                'x-csrftoken': cookieINS.split('csrftoken=')[1].split(';')[0],
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR1Jw2LrciyrzAQskwSVGREElPZZJZjW74y38oTjDnNHOu9e',
                'x-instagram-ajax': '1014868636',
                'x-requested-with': 'XMLHttpRequest',
            }
        param = {
            'instagram_account_id': account_id,
            'data': 'null',
        }
        DELAY = int(input(Fore.RED+'\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  Nhập Delay : '))
        print("\033[97m════════════════════════════════════════════════")

        for i in range(choose):
            try:
                job = f'https://gateway.golike.net/api/advertising/publishers/instagram/jobs?instagram_account_id={account_id}&data=null'
                nos = ses.get(job, headers=headers, params=param).json()

                if nos['status'] == 200:
                    ads_id = nos['data']['id']
                    object_id = nos['data']['object_id']
                    job_type = nos['data']['type']

                    if job_type == 'follow':
                        url = f'https://www.instagram.com/api/v1/friendships/create/{object_id}/'
                        data = {
                            'container_module': 'profile',
                            'nav_chain': 'PolarisFeedRoot:feedPage:8:topnav-link',
                            'user_id': object_id,
                        }
                        response = requests.post(url, headers=headerINS, data=data).text
                        countdown(DELAY)
                        
                        if '"status":"ok"' in response:
                            url = 'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs'
                            json_data = {
                                'instagram_account_id': account_id,
                                'instagram_users_advertising_id': ads_id,
                                'async': True,
                                'data': 'null',
                            }
                            time.sleep(3)
                            response = requests.post(url, headers=headers, json=json_data).json()

                            if response.get('success') == True:
                                dem += 1
                                local_time = time.localtime()
                                h, m, s = [f"{t:02d}" for t in (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)]
                                prices = response['data']['prices']
                                tong += prices

                                chuoi = (
                                    f"\033[1;31m\033[1;36m{dem}\033[1;31m\033[1;97m | "
                                    f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                                    f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                    f"\033[1;31mfollow\033[1;31m\033[1;32m\033[1;97m | "
                                    f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                    f"\033[1;33m{tong} vnđ"
                                )
                                print(chuoi)
                            else:
                                # Xử lý skip job
                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                params = {
                                    'ads_id': ads_id,
                                    'account_id': account_id,
                                    'object_id': object_id,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': job_type,
                                }
                                checkskipjob = ses.post(skipjob, params=params).json()

                                if checkskipjob['status'] == 200:
                                    print(Fore.RED + str(checkskipjob['message']))

                        elif '"status":"fail"' in response and '"spam":true' in response:
                            print(Fore.RED + "Tài khoản này bị nhã Follow")
                        elif '"status":"fail"' in response and '"require_login":true' in response:
                            print('Cookie die rồi! Tôi rất tiếc')
                            os.remove(f'COOKIEINS{account_id}.txt')
                            return 0

                    elif job_type == 'like':
                        like_id = nos['data']['description']
                        url = f'https://www.instagram.com/api/v1/web/likes/{like_id}/like/'
                        response = requests.post(url, headers=headerINS).text
                        countdown(DELAY)

                        if '"status":"ok"' in response:
                            # Tương tự như trên với 'follow', xử lý 'like' công việc
                            url = 'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs'
                            json_data = {
                            'instagram_account_id': account_id,
                            'instagram_users_advertising_id': ads_id,
                            'async': True,
                            'data':'null',
                            }
                            time.sleep(3)
                            response = requests.post(
                            'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
                            headers=headers,
                            json=json_data,
                            ).json()
                            if response['success']==True:
                                dem += 1
                                local_time = time.localtime()
                                hour = local_time.tm_hour
                                minute = local_time.tm_min
                                second = local_time.tm_sec

                                # Định dạng giờ, phút, giây
                                h = f"{hour:02d}"
                                m = f"{minute:02d}"
                                s = f"{second:02d}"
                                prices =response['data']['prices']

                                # Cộng dồn giá trị prices vào tổng tiền
                                tong += prices

                                chuoi = (
                                    f"\033[1;31m\033[1;36m{dem}\033[1;31m\033[1;97m | "
                                    f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                                    f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                    f"\033[1;31mlike\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                    f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                    f"\033[1;33m{tong} vnđ"
                                )
                                print(chuoi) 
                            else:
                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                PARAMS = {
                                'ads_id' : ads_id,
                                'account_id' : account_id,
                                'object_id' : object_id ,
                                'async': 'true',
                                'data': 'null',
                                'type': type,
                                }
                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                if checkskipjob['status'] == 200:
                                    message = checkskipjob['message']
                                    print(Fore.RED+str(message))
                                    PARAMSr = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                        elif '"status":"fail"' in response and '"spam":true' in response:
                            print(Fore.RED + "Tài khoản này bị chặn like")
                        elif '"status":"fail"' in response and '"require_login":true' in response:
                            print('Cookie die rồi! Tôi rất tiếc')
                            os.remove(f'COOKIEINS{account_id}.txt')
                            return 0
                        # pass

                else:
                    print(nos['message'])
                    countdown(15)

            except Exception as e:
                print(f"Lỗi xảy ra: {str(e)}")
                continue
def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f"""
\033[1;33m██╗░░░██╗███╗░░██╗░██████╗░██╗░░██╗██╗░█████╗░
\033[1;35m██║░░░██║████╗░██║██╔════╝░██║░░██║██║██╔══██╗
\033[1;36m██║░░░██║██╔██╗██║██║░░██╗░███████║██║███████║
\033[1;37m██║░░░██║██║╚████║██║░░╚██╗██╔══██║██║██╔══██║
\033[1;32m╚██████╔╝██║░╚███║╚██████╔╝██║░░██║██║██║░░██║
\033[1;31m░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝\n
 
               BOX FB: https://www.facebook.com/ungnghiaA/
               ADMIN : UÔNG NGHĨA 
               YTB : ᰔᩚυиɢнĩα
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)

def LIST():
    banner()
    print("\033[1;32mNhập \033[1;31m1 \033[1;33mđể vào \033[1;34mTool Instagram\033[1;33m")
os.system('cls' if os.name== 'nt' else 'clear')
banner()
checkfile = os.path.isfile('user.txt')
if checkfile == False:
    AUTHUR = input(Fore.GREEN+'\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  \033[1;32mNHẬP Authorization Golike : ')
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
ses = requests.Session()
User_Agent=random.choice([
"android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9100 Build/KTU84P) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/50.0.3755.367 Mobile Safari/600.8",
"android|Mozilla/5.0 (Linux; Android 5.0; SM-N910V Build/LRX22C) AppleWebKit/601.33 (KHTML, like Gecko) Chrome/54.0.1548.302 Mobile Safari/537.0",
"android|Mozilla/5.0 (Linux; U; Android 7.1; Pixel C Build/NRD90M) AppleWebKit/600.2 (KHTML, like Gecko) Chrome/53.0.2480.357 Mobile Safari/600.7",
"android|Mozilla/5.0 (Linux; U; Android 7.0; Nexus 7 Build/NME91E) AppleWebKit/537.24 (KHTML, like Gecko) Chrome/55.0.1165.180 Mobile Safari/535.4",
"android|Mozilla/5.0 (Android; Android 4.4.4; IQ4502 Quad Build/KOT49H) AppleWebKit/603.22 (KHTML, like Gecko) Chrome/55.0.3246.371 Mobile Safari/535.0",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG SM-G925FQ Build/KOT49H) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/49.0.2349.273 Mobile Safari/533.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; SM-G935S Build/LMY47X) AppleWebKit/601.8 (KHTML, like Gecko) Chrome/51.0.1541.177 Mobile Safari/603.6",
"android|Mozilla/5.0 (Android; Android 7.1; Nexus 6 Build/NME91E) AppleWebKit/533.39 (KHTML, like Gecko) Chrome/52.0.3581.331 Mobile Safari/602.0",
"android|Mozilla/5.0 (Android; Android 7.1; Pixel C Build/NME91E) AppleWebKit/536.42 (KHTML, like Gecko) Chrome/47.0.2862.396 Mobile Safari/534.0",
"android|Mozilla/5.0 (Linux; Android 5.0.1; LG-D725 Build/LRX22G) AppleWebKit/603.18 (KHTML, like Gecko) Chrome/54.0.3919.385 Mobile Safari/601.9",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; Lenovo A7000-a Build/LRX21M;) AppleWebKit/600.8 (KHTML, like Gecko) Chrome/47.0.1683.316 Mobile Safari/534.4",
"android|Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925M Build/LRX22G) AppleWebKit/533.12 (KHTML, like Gecko) Chrome/48.0.3195.222 Mobile Safari/534.1",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; MOTOROLA XT1021 Build/LXB22) AppleWebKit/602.21 (KHTML, like Gecko) Chrome/51.0.3324.323 Mobile Safari/536.2",
"android|Mozilla/5.0 (Linux; Android 4.4; LG-D350 Build/KOT49I) AppleWebKit/601.4 (KHTML, like Gecko) Chrome/50.0.1490.201 Mobile Safari/602.6",
"android|Mozilla/5.0 (Linux; Android 7.0; Xperia Build/NDE63X) AppleWebKit/600.18 (KHTML, like Gecko) Chrome/48.0.3885.393 Mobile Safari/602.7",
"android|Mozilla/5.0 (Android; Android 7.1; Nexus 9X Build/NPD90G) AppleWebKit/536.38 (KHTML, like Gecko) Chrome/52.0.2441.242 Mobile Safari/601.0",
"android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9600 Build/KTU84P) AppleWebKit/602.14 (KHTML, like Gecko) Chrome/53.0.2318.108 Mobile Safari/534.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; MOTO XT1570 MOTO X STYLE Build/LMY47Z) AppleWebKit/534.48 (KHTML, like Gecko) Chrome/55.0.1855.292 Mobile Safari/602.5",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; HTC Butterfly S 919d Build/LRX22G) AppleWebKit/534.18 (KHTML, like Gecko) Chrome/50.0.1695.312 Mobile Safari/535.3",
"android|Mozilla/5.0 (Android; Android 4.4; MOTOROLA MOTOG Build/KVT49L) AppleWebKit/533.8 (KHTML, like Gecko) Chrome/55.0.3923.147 Mobile Safari/600.9",
"android|Mozilla/5.0 (Linux; U; Android 6.0; HTC One801e dual sim Build/MRA58K) AppleWebKit/536.39 (KHTML, like Gecko) Chrome/47.0.3811.339 Mobile Safari/601.7",
"android|Mozilla/5.0 (Linux; Android 6.0.1; HTC OneS Build/MRA58K) AppleWebKit/600.47 (KHTML, like Gecko) Chrome/51.0.1432.312 Mobile Safari/535.4",
"android|Mozilla/5.0 (Linux; U; Android 4.4.1; LG-H220 Build/KOT49H) AppleWebKit/600.42 (KHTML, like Gecko) Chrome/48.0.2208.322 Mobile Safari/601.2",
"android|Mozilla/5.0 (Linux; U; Android 7.0; Nexus 6 Build/NME91E) AppleWebKit/534.11 (KHTML, like Gecko) Chrome/54.0.3774.223 Mobile Safari/600.6",
"android|Mozilla/5.0 (Linux; U; Android 7.0; GT-I9800 Build/KTU84P) AppleWebKit/601.41 (KHTML, like Gecko) Chrome/50.0.1638.368 Mobile Safari/536.0",
"android|Mozilla/5.0 (Linux; Android 6.0; SM-D925S Build/MDB08I) AppleWebKit/533.20 (KHTML, like Gecko) Chrome/47.0.2004.347 Mobile Safari/537.9",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; LG-H900 Build/NRD90C) AppleWebKit/536.25 (KHTML, like Gecko) Chrome/48.0.2443.138 Mobile Safari/601.6",
"android|Mozilla/5.0 (Linux; Android 6.0; HTC One_M8 Build/MRA58K) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/47.0.3998.201 Mobile Safari/603.7",
"android|Mozilla/5.0 (Linux; U; Android 5.0; Nokia 1100 wifi Build/GRK39F) AppleWebKit/533.11 (KHTML, like Gecko) Chrome/54.0.1361.195 Mobile Safari/602.4",
"android|Mozilla/5.0 (Linux; U; Android 4.4.4; SGH-I337 Build/KOT49H) AppleWebKit/536.23 (KHTML, like Gecko) Chrome/51.0.1317.102 Mobile Safari/603.0",
"android|Mozilla/5.0 (Linux; Android 5.0; SM-N915G Build/LRX22C) AppleWebKit/533.5 (KHTML, like Gecko) Chrome/50.0.2825.177 Mobile Safari/602.4",
"android|Mozilla/5.0 (Android; Android 5.1; SM-G9350FG Build/LMY47X) AppleWebKit/533.11 (KHTML, like Gecko) Chrome/53.0.2999.116 Mobile Safari/601.3",
"android|Mozilla/5.0 (Android; Android 5.1; SAMSUNG SM-G9350M Build/LMY47X) AppleWebKit/534.37 (KHTML, like Gecko) Chrome/51.0.3632.269 Mobile Safari/533
