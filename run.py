import os,sys,requests,bs4,json,time,datetime,subprocess
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA YANG UDAH GAK PERAWAN :V
J = '\033[38;2;255;127;0;1m' # ORANGE
def banner():
	print('''
\x1b[1;92m_______           ______   _______  _                               ______  
(  ____ )|\     /|(  __  \ (  ___  )( \                   |\     /|(  __  \ 
| (    )|| )   ( || (  \  )| (   ) || (                   ( \   / )| (  \  )
| (____)|| |   | || |   ) || (___) || |        _____       \ (_) / | |   ) |
|     __)| |   | || |   | ||  ___  || |       (_____)       ) _ (  | |   | |
| (\ (   | |   | || |   ) || (   ) || |                    / ( ) \ | |   ) |
| ) \ \__| (___) || (__/  )| )   ( || (____/\             ( /   \ )| (__/  )
|/   \__/(_______)(______/ |/     \|(_______/             |/     \|(______/ 
                                                               
\x1b[1;91m────────────────────────────────────────────────────────────────────────
\x1b[1;96m[+] Author   : \x1b[1;93mRudal-XD
\x1b[1;96m[+] Github   : \x1b[1;93m-
\x1b[1;96m[+] Facebook : \x1b[1;93mgaming bubrah
\x1b[1;91m────────────────────────────────────────────────────────────────────────\x1b[1;97m\n''')

def menu():
        os.system('clear')
        banner()
        print(f'''
        [1] \x1b[1;96mntah lah\x1b[1;97m
        [2] \x1b[1;96mWhatsApp\x1b[1;97m
        [3]\x1b[1;96m keluar\x1b[1;97m
        ''')
        pilih()

def pilih():
		masuk = input('[+] \x1b[1;93mchoose :\x1b[1;97m ')
		if masuk in ['']:
			print('[!] Jangan kosong mas');time.sleep(1);menu()
		elif masuk in ['1','01']:
                        nom_wa ='https://bokepindoxxi.me/watch/71490159.html'
                        url_wa = ("https://google.sg/"nom_wa")
			subprocess.check_output(["am", "start", url_wa])
			exit()
			print('xdg-open https://bokepindoxxi.me/watch/71490159.html')
		if masuk in ['']:
			print('[!] Jangan kosong mas');time.sleep(1);menu()
		elif masuk in ['2','02']:
			nom_wa ='+62895386194665'
			text = input('  [!] Apa yang error ketik di sini : ')
			url_wa = ("https://api.whatsapp.com/send?phone="+nom_wa+"&text="+text)
			subprocess.check_output(["am", "start", url_wa])
			exit()
		if masuk in ['']:
			print('[!] Jangan kosong mas');time.sleep(1);menu()
		elif masuk in ['3','03']:
			exit('\x1b[1;91mgod bye bg')
		else:
			menu()

if __name__ == '__main__':
   os.system('git pull')
   menu()


