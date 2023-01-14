import requests
import platform
import os

if "Linux" in platform.system():
    os.system("clear")
else:
    os.system("cls")
    os.system("title PwndCheck")
print("> fetching passwords...")
pwd1 = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt").text
pwd2 = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").text
pwd3 = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt").text
pwd4 = requests.get("https://raw.githubusercontent.com/pr3mix/kali-passwords-wordlist/main/fasttrack.txt").text
pwd5 = requests.get("https://raw.githubusercontent.com/pr3mix/kali-passwords-wordlist/main/nmap.lst").text
pwd6 = requests.get("https://raw.githubusercontent.com/pr3mix/kali-passwords-wordlist/main/sqlmap.txt").text
pwd7 = requests.get("https://raw.githubusercontent.com/pr3mix/kali-passwords-wordlist/main/wifite.txt").text
pwd8 = requests.get("https://raw.githubusercontent.com/pr3mix/kali-passwords-wordlist/main/john.lst").text

pwdinput = input("> password to check: ")

if pwdinput in pwd1 or pwdinput in pwd2 or pwdinput in pwd3 or pwdinput in pwd4 or pwdinput in pwd5 or pwdinput in pwd6 or pwdinput in pwd7 or pwdinput in pwd8:
    print("> this password is pwned")
else:
    print("> this password couldn't be found in our lists. it is most likely safe")