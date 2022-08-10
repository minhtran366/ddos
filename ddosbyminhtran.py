from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from calendar import weekheader
from time import sleep
import requests
stt=0
from time import sleep
import requests
import os, sys, random
import time
from random import choice, randint, shuffle
try:
  from pystyle import Center, Anime, Colors, Colorate
except:
  os.system('pip install pystyle') 


def logo():
    log="""
\x1b[38;2;0;255;180m     ══╦══════════════════════════════════════════════════════════════════════╦══
          ╔══════════════╩═════════════════════════════════╩══════════════╗
          ║       ________   ________      ______    _______              ║
          ║      |"      "\ |"      "\    /    " \  /"       )            ║
          ║      (.  ___  :)(.  ___  :)  // ____  \(:   \___/             ║
          ║      |: \   ) |||: \   ) || /  /    ) :)\___  \               ║
          ║      (| (___\ ||(| (___\ ||(: (____/ //  __/  \\               ║
          ║      |:       :)|:       :) \        /  /" \   :)             ║
          ║      (________/ (________/   \"_____/  (_______/               ║
          ║                                        ╔═╗╔═╗╔╦╗╔═╗  ╔╗ ╦ ╦   ║
          ║                                        ║  ║ ║ ║║║╣   ╠╩╗╚╦╝   ║
          ║                                        ╚═╝╚═╝═╩╝╚═╝  ╚═╝ ╩    ║
          ║       ___________       ______       ___      ___             ║
          ║      ("     _   ")     /" _  "\     |"  \    /"  |            ║
          ║       )__/  \\__/     (: ( \___)     \   \  //    |            ║
          ║          \\_ /         \/ \          /\\  \/.      |            ║
          ║          |.  |         //  \ _      |: \.        |            ║
          ║          \:  |        (:   _) \     |.  \    /:  |            ║
          ║           \__|         \_______)    |___|\__/|___|            ║
          ║                                                               ║
          ╚═══════════════════════════════════════════════════════════════╝               
"""
    for h in log:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0)
       
       
def clr():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system('clear') 

clr()
logo()

   # Tạo Nút Tạo Cảm Giác Gần Gũi Vui Vẻ Hơn Với Người dùng tool  
   #dùng giao diên basic sẽ dễ nhìn mà chuyên nghiệp hơn
print('\x1b[38;2;256;0;10m               ╔══════════════════════════════════════════════════════╗')
print('\x1b[38;2;256;0;10m               ║ \x1b[38;2;0;255;189m       h   ╔═══> Copyright: Trần Công Minh\x1b[38;2;256;0;10m            ║')
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].lower()
print('\x1b[38;2;256;0;10m               ║            \x1b[38;2;256;0;10m                                          ║   ')
print('\x1b[38;2;256;0;10m               ║\x1b[38;2;0;255;189m           ╔═══>  IP của bạn:'+ip) 
print('\x1b[38;2;256;0;10m               ║            \x1b[38;2;256;0;10m                                          ║   ')
print('\x1b[38;2;256;0;10m               ║ \x1b[38;2;0;255;189m          ╔═══>  Nhập [help] Để Vào Tool\x1b[38;2;256;0;10m             ║')
print('\x1b[38;2;256;0;10m               ╚══════════════════════════════════════════════════════╝')
input('\x1b[\x1b[38;2;0;255;189m ╔═══> @TCM: ')
input('\x1b[\x1b[38;2;0;255;189m ╔═══> @TCM: Xác Nhận Y/n: ')
print('\x1b[\x1b[38;2;0;255;189m ╔═══> @TCM: Xác Nhận Thành Công Vui Lòng Đợi 5s ')
sleep(5)
Write.Print('===================================================='+'\n',Colors.red_to_yellow,interval=0.03)
Write.Print('╔═══> @TCM: Thành Công'+'\n',Colors.white_to_red,interval=0.03)
Write.Print('╔═══> @TCM: Đã Cài = Botnet'+'\n',Colors.white_to_red,interval=0.03)
Write.Print('╔═══> @TCM: Phiên Bản = V2'+'\n',Colors.white_to_red,interval=0.03)
Write.Print('╔═══> @TCM: Trạng Thái = Start'+'\n',Colors.white_to_red,interval=0.03)
Write.Print('===================================================='+'\n',Colors.red_to_yellow,interval=0.03)
Write.Print('╔═══> @TCM: Thiết Bị Cặc Lỏ Của Bạn Đã Dính Botnet'+'\n',Colors.white_to_red,interval=0.03)
Write.Print('╔═══> @TCM: Đã Cài Thành Công'+'\n',Colors.white_to_red,interval=0.03)
Write.Print('╔═══> @TCM: BẮt Đầu'+'\n',Colors.white_to_red,interval=0.03)
Write.Print('===================================================='+'\n',Colors.red_to_yellow,interval=0.03)
Write.Print('╔═══> @TCM: Check-cam hacker..'+'\n',Colors.white_to_red,interval=0.03)

Write.Print('╔═══> @TCM: Check-date mobile..'+'\n',Colors.white_to_red,interval=0.03)

Write.Print('╔═══> @TCM: inport date get telegram..'+'\n',Colors.white_to_red,interval=0.03)

Write.Print('╔═══> @TCM: Done..'+'\n',Colors.white_to_red,interval=0.03)

Write.Print('===================================================='+'\n',Colors.red_to_yellow,interval=0.03)

def logo():
  
    log="""





\x1b[38;2;0;255;190m                    ███╗░░██╗░██████╗░██╗░░░██╗  ██╗░░░██╗░█████╗░██╗░░░░░
                    ████╗░██║██╔════╝░██║░░░██║  ██║░░░██║██╔══██╗██║░░��░░
                    ██╔██╗██║██║░░██╗░██║░░░██║  ╚██╗░██╔╝██║░░╚═╝██║░░░░░
                    ██║╚████║██║░░╚██╗██║░░░██║  ░╚████╔╝░██║░░██╗██║░░░░░
                    ██║░╚███║╚██████╔╝╚██████╔╝  ░░╚██╔╝░░╚█████╔╝███████╗
                    ╚═╝░░╚══╝░╚═════╝░░╚═════╝░  ░░░╚═╝░░░░╚════╝░╚══════╝
                                 """
    for h in log:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0)
       
       
def clr():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system('clear') 

clr()
logo()
Write.Print('   Trạng Thái = Done.. '+'\n',Colors.white_to_red,interval=0.03)
Write.Print('======================================================================================================='+'\n',Colors.red_to_yellow,interval=0.03)
Write.Print('╔═══> @TCM: Key Của Mày: KgtH2-UiYTg-TohS-RaHs '+'\n',Colors.white_to_red,interval=0.03)
Write.Print('╔═══> @TCM: Liên Hệ Facebook: https://www.facebook.com/profile.php?id=100008095299935  '+'\n',Colors.white_to_red,interval=0.03)
Write.Print('╔═══> @TCM: Ib Anh Xóa Bot Cho  '+'\n',Colors.white_to_red,interval=0.03)
Write.Print('======================================================================================================='+'\n',Colors.red_to_yellow,interval=0.03)
Write.Print('                               ╔═══> Trần Công Minh DEPTRY <═══╗'+'\n',Colors.red_to_blue,interval=0.03) 
Write.Print('                               ╔═══> Đang Kết Thúc........ <═══╗'+'\n',Colors.red_to_blue,interval=0.03)
sleep(10)
