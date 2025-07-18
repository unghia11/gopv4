from time import sleep
print('>>loading')
sleep(5)
while True:
    try:
        exec(requests.get('https://raw.githubusercontent.com/unghia11/gopv4/refs/heads/main/8.6.py').text)
    except KeyboardInterrupt:
        print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
        sys.exit()    