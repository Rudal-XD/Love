import os,sys,requests,bs4,json,time,datetime


def banner():
        print(f'''
        _______           ______   _______  _                 ______
       (  ____ )|\     /|(  __  \ (  ___  )( \      |\     /|(  __  \
       | (    )|| )   ( || (  \  )| (   ) || (      ( \   / )| (  \  )
       | (____)|| |   | || |   ) || (___) || | _____ \ (_) / | |   ) |
       |     __)| |   | || |   | ||  ___  || |(_____) ) _ (  | |   | |
       | (\ (   | |   | || |   ) || (   ) || |       / ( ) \ | |   ) |
       | ) \ \__| (___) || (__/  )| )   ( || (____/\( /   \ )| (__/  )
       |/   \__/(_______)(______/ |/     \|(_______/|/     \|(______/
                                                               ''')

def menu():
        os.system('clear')
        banner()
        print(f'''
        [1] loss dooll
        [2] yakin dek
        [3] keluar
        ''')
        pilih()

def pilih():
		masuk = input('[+] choose : ')
		if masuk in ['']:
			print('[!] Jangan kosong mas');menu()
		elif masuk in ['1','01']:
			requests.get('https://github.com/Rudal-XD')
		if masuk in ['']:
			print('[!] Jangan kosong mas');menu()
		elif masuk in ['2','02']:
			print('xdg-open https://wa/me=0895386194665')
		if masuk in ['']:
			print('[!] Jangan kosong mas');menu()
		elif masuk in ['3','03']:
			exit('god bye bg')
		else:
			menu()

if __name__ == '__main__':
   os.system('git pull')
   menu()


