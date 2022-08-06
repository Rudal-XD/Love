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
        [3] exit
        ''')
def pilih(self):
		usna = input('[+] choose : ')
		if usna in ['']:
			print('[!] Jangan kosong mas');time.sleep(2);menu()
		elif usna in ['1','01']:
		
		else:
                        menu()


if __name__ == '__main__':
   os.system('git pull')
   menu()


