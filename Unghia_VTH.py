from datetime import datetime
import random
import hashlib
from collections import Counter
import statistics
import platform
from datetime import datetime
import base64
import urllib.parse
import requests
import string
import math
import json
import os
import time
from colorama import Fore, Style, init

room_names={
    1: 'Nhà kho',
    2: 'Phòng họp',
    3: "Phòng Giám đốc",
    4: 'Phòng trò chuyện',
    5: 'Phòng Giám sát',
    6: 'Văn phòng',
    7: 'Phòng Tài Vụ',
    8: 'Phòng Nhân sự'
}
init(autoreset=True)
def clear_screen():
    os.system('cls' if platform.system() == "Windows" else 'clear')
def prints(r, g, b, text="text", end="\n"):
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m", end=end)

def top10_vth(s,headers,Coin):
    params = {
        'asset': Coin,
    }
    try:
        response = s.get('https://api.escapemaster.net/escape_game/recent_10_issues', params=params, headers=headers).json()
        ki=[]
        phong=[]
        for i in response['data']:
            ki.append(i['issue_id'])
            phong.append(i['killed_room_id'])
        return ki,phong
    except Exception as e:
        prints(247, 30, 30,f'LỖI khi lấy dữ liệu {e}')
        time.sleep(5)
        top10_vth(s,headers,Coin)
def load_data_vth():
    if os.path.exists('data-xw-vth.txt'):
        prints(0, 255, 243,'Bạn có muốn sử dụng thông tin đã lưu không? (y/n): ',end='')
        x=input()
        if x=='y':
            with open('data-xw-vth.txt','r',encoding='utf-8') as f:
                return json.load(f)
        prints(247, 255, 97,"═" * 47)
    str="""
Hướng dẫn lấy link:
    0. Mở chrome
    1. Truy cập website xworld.io
    2. Đăng nhập vào tài khoản
    3. Tìm và nhấp vào Vua thoát hiểm
    4. Nhấn lâp jtucs truy cập
    5. Sao chép link website và dán vào đây
"""
    prints(218, 255, 125,str)
    prints(247, 255, 97,"═" * 47)
    prints(125, 255, 168,'📋Nhập liên kết của bạn:',end=' ')
    link=input()
    user_id=link.split('&')[0].split('?userId=')[1]
    user_secretkey=link.split('&')[1].split('secretKey=')[1]
    prints(218, 255, 125,f'    Your user id is {user_id}')
    prints(218, 255, 125,f'    Your user secret key is {user_secretkey}')
    json_data={
        'user-id':user_id,
        'user-secret-key':user_secretkey,
    }
    with open('data-xw-vth.txt','w+',encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    return json_data
def kiem_tra_kq_vth(s,headers,ki,bot_chon,Coin,tg):
    try:
        start_time=time.time()
        while True:
            if time.time()<=tg+60:
                prints(255,255,0,f'Đang chờ kết quả {time.time()-start_time:.0f}...',end='\r')
                time.sleep(1)
            data_top10=top10_vth(s,headers,Coin)
            prints(255,255,0,f'Đang chờ kết quả {time.time()-start_time:.0f}...',end='\r')
            if data_top10[0][0]==int(ki):
                prints(15, 87, 219,f'Kẻ giết người đã vào phòng số {data_top10[1][0]} : {room_names[data_top10[1][0]]}')
                if int(bot_chon)==int(data_top10[1][0]):
                    prints(255, 0, 38,'Bạn thua rồi. Chúc bạn may mắn lần sau nhé...')
                    time.sleep(10)
                    return False,time.time()
                else:
                    prints(0, 255, 102,' Xin chúc mừng, bạn đã thắng')
                    time.sleep(10)
                    return True,time.time()
            time.sleep(1)
    except Exception as e:
        prints(255,0,0,f'Lỗi khi kiểm tra kết quả: {e}')
        return kiem_tra_kq_vth(s,headers,ki,bot_chon,Coin,tg)
def chon_phong1(data_top10,data_top100):
    while True:
        result=random.randint(1,8)
        if result!=data_top10[1][0]:
            return result
def chon_phong(data10,data100,hisory,trap):
    x=1
    if len(hisory)>=1:
        if hisory[0]['kq']==False:
            x=trap
    bot_chon=chon_phong1(data10,data100)
    return bot_chon,x
def bet_vth(s,user_id,user_secretkey,room_id,Coin,bet_amount):
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'vi,en;q=0.9',
            'cache-control': 'no-cache',
            'country-code': 'vn',
            'origin': 'https://xworld.info',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://xworld.info/',
            'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'user-id': user_id,
            'user-login': 'login_v2',
            'user-secret-key': user_secretkey,
            'xb-language': 'vi-VN',
        }
        json_data = {
            'asset_type': Coin,
            'user_id': user_id,
            'room_id': room_id,
            'bet_amount': float(bet_amount),
        }
        response = s.post('https://api.escapemaster.net/escape_game/bet', headers=headers, json=json_data).json()
        prints(255,255,0,response)
        if response['code']==0 and response['msg']=='ok':
            prints(0, 149, 255,f' Đã đặt {bet_amount} {Coin} vào phóng số {room_id}')
            return bet_amount
        else:
            prints(255,0,0,response['msg'])
            return bet_amount
    except Exception as e:
        prints(255, 0, 4,f' {e}')
        return bet_amount
def user_asset(s,headers):
    try:
        json_data = {
            'user_id': int(headers['user-id']),
            'source': 'home',
        }

        response = requests.post('https://wallet.3games.io/api/wallet/user_asset', headers=headers, json=json_data).json()
        asset={
            'USDT':response['data']['user_asset']['USDT'],
            'WORLD':response['data']['user_asset']['WORLD'],
            'BUILD':response['data']['user_asset']['BUILD']
        }
        return asset
    except Exception as e:
        prints(255,0,0,f'Error when getting balance: {e}')
        prints(255,0,0,f'Vui lòng lấy lại link và thử lại')
        return user_asset(s,headers)
def print_stats(s, stats, headers, Coin):
    asset = user_asset(s, headers)
    prints(5,255,0,f'{asset['USDT']:.2f}USDT - {asset['WORLD']:.2f}WORLD - {asset['BUILD']:.2f}BUILD')
    prints(66, 239, 245,F'Thắng: {stats['win']}/{stats['win']+stats['lose']}')
    prints(66, 239, 245,F'Lời: {asset[Coin]-stats['asset0']}')
    prints(66, 239, 245,F'Chuỗi thắng: {stats['streak']} (MAX: {stats['max_streak']})')
    total_games = stats['win'] + stats['lose']
    win_rate = (stats['win'] / total_games * 100) if total_games > 0 else 0
    earn = asset[Coin] - stats['asset0']
    if earn > 0:
        color = 0x00FF00  # Xanh lá (lãi)
        earn_emoji = "📈"
    elif earn < 0:
        color = 0xFF0000  # Đỏ (lỗ)
        earn_emoji = "📉"
    else:
        color = 0xFFFF00  # Vàng (hòa vốn)
        earn_emoji = "➡️"

    WEBHOOK_URL = "https://discord.com/api/webhooks/1403691626194272296/pxMiyq4MaKAM0GXHGebxBmTRArPIIR2vFO7C4GGOm6AdelgmpVkBugW01XbD_xP662R9"

    embed = {
        "title": "🎯 XWORLD BOT - BÁO CÁO THỐNG KÊ",
        "description": f"📊 **Tổng quan hoạt động bot trading**\n⏰ Cập nhật lúc: <t:{int(datetime.now().timestamp())}:F>",
        "color": color,
        "thumbnail": {
            "url": "https://i.postimg.cc/ZYWn7VFX/unnamed.png"
        },
        "fields": [
            {
                "name": "👤 Thông tin tài khoản",
                "value": f"🆔 **User ID:** ||{headers.get('user-id', 'N/A')}||\n",
                "inline": False
            },
            {
                "name": "💼 Tài sản hiện tại",
                "value": f"💵 **USDT:** `{asset['USDT']:.4f}`\n🌍 **WORLD:** `{asset['WORLD']:.4f}`\n🏗️ **BUILD:** `{asset['BUILD']:.4f}`",
                "inline": True
            },
            {
                "name": "🏆 Thống kê chiến thắng",
                "value": f"✅ **Thắng:** `{stats['win']}`\n❌ **Thua:** `{stats['lose']}`\n📊 **Tỷ lệ thắng:** `{win_rate:.1f}%`",
                "inline": True
            },
            {
                "name": f"{earn_emoji} Lợi nhuận",
                "value": f"💰 **Tổng earn:** `{earn:.10f} {Coin}`\n{'🚀' if earn > 0 else '⚠️' if earn < 0 else '💫'} **Trạng thái:** {'Đang lãi' if earn > 0 else 'Đang lỗ' if earn < 0 else 'Hòa vốn'}",
                "inline": True
            },
            {
                "name": "🔥 Chuỗi thắng",
                "value": f"⚡ **Hiện tại:** `{stats['streak']}`\n🏅 **Cao nhất:** `{stats['max_streak']}`",
                "inline": True
            },
            {
                "name": "📈 Phân tích",
                "value": f"🎮 **Tổng ván:** `{total_games}`\n⚖️ **W/L Ratio:** `{stats['win']}:{stats['lose']}`",
                "inline": True
            }
        ],
        "footer": {
            "text": "XWORLD BOT | Powered by Công • Cập nhật tự động",
            "icon_url": "https://i.postimg.cc/ZYWn7VFX/unnamed.png"
        },
        "timestamp": datetime.now().isoformat()
    }
    if stats['streak'] >= 5:
        embed["image"] = {
            "url": "https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif"
        }

    payload = {
        "username": "🤖 XWORLD Analytics",
        "avatar_url": "https://i.postimg.cc/ZYWn7VFX/unnamed.png",
        "embeds": [embed],
        "content": f"{'🎉 **STREAK CAO!**' if stats['streak'] >= 5 else '📊 **Báo cáo định kỳ**'} - Bot đang hoạt động {'🟢' if earn >= 0 else '🔴'}"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
    except Exception as e:
        pass
def top100_vth(s,headers,Coin):
    params = {
        'asset': Coin,
    }
    try:
        response = s.get('https://api.escapemaster.net/escape_game/recent_100_issues', params=params, headers=headers).json()
        return response['data']['room_id_2_killed_times']
    except Exception as e:
        prints(247, 30, 30,f'LỖI khi lấy dữ liệu {e}')
        time.sleep(5)
        return top100_vth(s,headers,Coin)
def banner():
    banner_text = """
    ╔═════════════════════════════════════════╗
    ║    🚀 TOOL TỰ ĐỘNG CÀY BUILD XWORLD 🚀  ║
    ╠═════════════════════════════════════════╣
    ║👤 Bản quyền: UnghiaTool                 ║
    ║📞 Facebook: Uông Văn Nghĩa              ║
    ║📺 Tiktok: tiktok.com/unghia._           ║
    ║🌐 Shop: shoptununghia.github.io         ║
    ╚═════════════════════════════════════════╝
    """

    r, g, b = 255, 255, 255
    for line in banner_text.split('\n'):
        for char in line:
            prints(r, g, b, char, end='')
            time.sleep(0.0005)
            r = max(50, r - 5)
            b = max(50, b - 1)
        r, g, b = 255, 255, 255
        print()

    prints(247, 255, 97, "✨" + "═" * 60 + "✨")
    prints(32, 230, 151, "🌟 XWORLD AUTOMATION TOOL 🌟".center(62))
    prints(247, 255, 97, "═" * 62)

    prints(247, 255, 97, "═" * 62)
    print()
def main():
    banner()
    s=requests.Session()
    data=load_data_vth()
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9',
        'cache-control': 'no-cache',
        'country-code': 'vn',
        'origin': 'https://xworld.info',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://xworld.info/',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'user-id': data['user-id'],
        'user-login': 'login_v2',
        'user-secret-key': data['user-secret-key'],
        'xb-language': 'vi-VN',
    }
    asset=user_asset(s,headers)
    prints(5,255,0,f'BALANCE: {asset['USDT']:.2f}USDT - {asset['WORLD']:.2f}WORLD - {asset['BUILD']:.2f}BUILD')
    prints(5,255,0,"""
        1. BUILD
        2. USDT
        3. WORLD
        """)
    prints(255,255,0,f'Chọn loại tiền bạn muốn chơi (1/2/3): ',end='')
    Coin=input()
    if Coin=='1':
        Coin='BUILD'
    elif Coin=='2':
        Coin='USDT'
    elif Coin=='3':
        Coin='WORLD'
    prints(255,255,0,f'Nhập số lương {Coin} để đặt (Gợi ý: {asset[Coin]/111:.2f}): ',end='')
    bet_amount0=float(input())
    prints(255,255,0,f'Ví dụ khi bạn đặt hệ số cược là 10 thì nếu ván này bạn đặt 100 build và đã thua thì ván sau mức cược sẽ tăng x10, sẽ đặt 1000 build')
    trap=float(input('Nhập hệ số cược sau khi thua: '))
    delay1=int(input('Sau bao nhiêu ván thì tạm nghỉ (Nhập 999 nếu không muốn tạm nghỉ): '))
    delay2=int(input(f'Sau {delay1} ván thì tạm nghỉ bao nhiêu ván (Nhập 0 nếu không muốn nghỉ): '))
    hisory=[]
    stats={
        'win':0,
        'lose':0,
        'asset0':asset[Coin],
        'streak':0,
        'max_streak':0,
    }
    tg=time.time()-60
    clear_screen()
    banner()
    tong=0
    while True:
        try:
            tong+=1
            prints(247, 255, 97,"═" * 47)
            data10=top10_vth(s,headers,Coin)
            data100=top100_vth(s,headers,Coin)
            bot_chon=chon_phong(data10,data100,hisory,trap)
            ki=data10[0][0]+1
            print_stats(s,stats,headers,Coin)
            prints(5,255,0,f'Dự đoán cho kì {ki} : {bot_chon[0]} - {room_names[int(bot_chon[0])]}')
            cycle = delay1 + delay2
            pos = (tong - 1) % cycle
            if pos < delay1:
                stop=False
                bet_amount=bet_vth(s,data['user-id'],data['user-secret-key'],bot_chon[0],Coin,float(bet_amount0) if bot_chon[1]==1 else float(hisory[0]['bet_amount'])*bot_chon[1])
            else:
                stop=True
                prints(255,255,0,f'Ván này tạm nghỉ')
                bet_amount=bet_amount0
            result,tg=kiem_tra_kq_vth(s,headers,ki,bot_chon[0],Coin,tg)
            if result==True:
                stats['win']+=1
                stats['streak']+=1
                stats['max_streak']=max(stats['max_streak'],stats['streak'])
            elif result==False:
                stats['lose']+=1
                stats['streak']=0
            if stop==False:
                hisory.insert(0, {'bot_chon': bot_chon[0], 'kq': result,'bet_amount':bet_amount})
        except KeyboardInterrupt:
            prints(5,255,0,f'Bạn đã dùng chương trình')
            exit(0)

main()
