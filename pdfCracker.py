#pip3 install pikepdf tqdm
import pikepdf
from tqdm import tqdm
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PDFCracker")
print(ascii_banner)

passwords = [ line.strip() for line in open("wordlist.txt") ]
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open PDF file
        with pikepdf.open("locked.pdf", password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue
