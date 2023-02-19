import random
import webbrowser
import time
import os

print("Giriş İçin Doğrulama Kodu Gerekmektedir Almak İçin 5 Sn Bekleyiniz ")
time.sleep(1)
print(5)
time.sleep(1)
print(4)
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print(0)
h = random.randint(0 , 500)
print(h)
dgrlm=int(input("Ekrandaki Kodu Giriniz: "))
if dgrlm == h:
    print("Giriş Yapıldı İşlem Sayfasına Yönlendiriliyorsunuz")
    print("Lütfen Bekleyin")
    time.sleep(1)
else:
    print("Kod Yanlış Girildi")

print("Ne Yapmak İstersiniz?")

print("""
1)Ortalam Hesaplama
2)Zar Oyunu İçin
3)SwazzBot
4)Salak Oyun
""")
selecte = input("Seçiniz")
if selecte =='1':
    os.system("python Ortalama.py")
if selecte =='2':
    os.system("python Zar.py")
if selecte =='3':
    os.system("SwazBot")
    os.system("SwazzBot-main")
    os.system("python bot.py")
if selecte =='4':
    os.system("python PET.py")


k=input("SwazzAtena#1889")