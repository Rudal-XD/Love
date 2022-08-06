import os,sys,requests,bs4,json,time,datetime,subprocess


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
			print('[!] Jangan kosong mas');time.sleep(1);menu()
		elif masuk in ['1','01']:
			r=requests.get('https://github.com/Rudal-XD');time.sleep(1)
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
			exit('god bye bg')
		else:
			menu()

if __name__ == '__main__':
   os.system('git pull')
   menu()


