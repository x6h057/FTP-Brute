# FTPBrute - FTP Brute Force Tool

`FTPBrute` is a Python script that allows you to brute-force FTP login credentials using either custom usernames and passwords or a list of common built-in credentials. The script can also use a wordlist to perform brute-force attacks on FTP servers.

## Features

- Brute-force FTP login using custom or built-in credentials.
- Support for specifying the FTP server's hostname and port.
- Ability to use a wordlist for usernames and passwords.
- Custom error handling for FTP connection and login failures.
  
## Installation

1. Clone the repository or download the script file:
   ```bash
   git clone https://github.com/x6h057/FTP-Brute.git
   ```

2. Make sure you have Python 3 installed.

3. Install the necessary Python modules (if not already installed):
   ```bash
   pip install ftplib argparse
   ```

## Usage

### Basic Usage

```bash
python ftpBrute.py --host <hostname> --port <port> [-u <username>] [-p <password>] [-w <wordlist>]
```

### Arguments

- `--host`: **Required** - Specify the target FTP server hostname (e.g., `192.168.1.1`).
- `--port`: **Required** - Specify the FTP port (default is `21`).
- `-u, --username`: **Optional** - Provide a custom username for the brute-force attack.
- `-p, --password`: **Optional** - Provide a custom password for the brute-force attack.
- `-w, --wordlist`: **Optional** - Provide a wordlist file to attempt brute-forcing usernames (one per line).

### Example Commands

1. **Bruteforce with custom credentials:**

   ```bash
   python ftpBrute.py --host 192.168.1.1 --port 21 -u admin -p secret
   ```

2. **Bruteforce with built-in usernames and passwords (default list):**

   ```bash
   python ftpBrute.py --host 192.168.1.1 --port 21
   ```

3. **Bruteforce using a wordlist for usernames:**

   ```bash
   python ftpBrute.py --host 192.168.1.1 --port 21 -w wordlist.txt
   ```

4. **Bruteforce with custom credentials and wordlist:**

   ```bash
   python ftpBrute.py --host 192.168.1.1 --port 21 -u user -p password -w wordlist.txt

   python ftpBrute.py --host 192.168.1.1 --port 21 -u user -w wordlist.txt

   python ftpBrute.py --host 192.168.1.1 --port 21 -p password -w wordlist.txt


   ```

## How It Works

1. The script first checks if custom credentials (`-u` for username and `-p` for password) are provided. If provided, it attempts to login using those credentials.
2. If custom credentials are not provided, the script uses a built-in list of common usernames (`ftp`, `anonymous`, `admin`) and passwords (`ftp`, `anonymous`, `admin`, and an empty password).
3. If a wordlist file is provided using the `-w` option, the script will attempt each line from the wordlist as a username, combined with the common password list.

## Error Handling

The script handles connection and login errors gracefully, printing failure messages for each attempt. If the FTP server is unreachable or login fails, an error message will be displayed.

### Example output:
```
Bruteforcing: ftp:ftp
Failed: ftp:ftp - [Errno 111] Connection refused
Bruteforcing: anonymous:ftp
Success: anonymous:ftp
```

## Contributing

Feel free to open issues and pull requests if you'd like to contribute to the project. Suggestions, bug reports, and improvements are always welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
