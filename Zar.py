import time
import random
from colorama import Fore, init
import os
os.system("pip install colorama")

bakiye=100

print(Fore.LIGHTRED_EX)
print("PythonX-Small23 E HOŞGELDİN!!")
time.sleep(1)
print("Yükleniyor...")
time.sleep(4)
print("Son Hazırlıklar")
time.sleep(2)
print("HOŞGELDİN DOSTUM İSMİNİ ÖĞRENEBİLİRMİYİM")
time.sleep(3)
print(Fore.BLUE)
gr=input("İsminizi Oluşturun: ")
time.sleep(2)
print("Ooooo Çok Havalı , Hoşgeldin " + gr)
print(Fore.LIGHTMAGENTA_EX)
print("Oyuna Başlamadan Önce Sana Bazı Şeyler Öğretmem Gerekiyor...")
time.sleep(2)
print(gr +" Oyuna 100PX Bakiyeyle Başlarsın Ve Oynadıkça Bakiyen Artar")
time.sleep(2)
print("Aşşağıda Paran , Şansın , Uyku Puanın Yazıyor Bunlara Dikkat Et!")
print("""
💵:100
🍀:10
🛏:100
""")
while True:
    print("""
1)Zar VS
2)Zar Tahmin
3)Paranın Hepsiyle Son Şans Oyna
4)Bakiye Sorgu
    """)
    k=input("Hangisini Oynamak İstersiniz")
    if k=='1':
        print("Oyunumuzda Rastgele Zar Atarsın 1 Ve 6 Arasına Karşındaki Rakiple Daha Yüksek Atan Paranın 2 Katını Alır")
        playerone=input("Zar Atmak İçin Bir Tuşa Basınız: ")
        print("🎲")
        print("🎲")
        print("🎲")
        print("Attığın Sayııııııı")
        time.sleep(2)
        print(Fore.YELLOW)
        x=random.randint(1, 6)
        print(x)
        time.sleep(2)
        playertwo=print("Zar Atılıyorrr")
        print("Rakibin Attığı Sayıııı")
        time.sleep(2)
        print(Fore.LIGHTYELLOW_EX)
        y=random.randint(1, 6)
        time.sleep(2)
        print(y)
        if x >= y:
            bakiye=bakiye * 2
            time.sleep(2)
            print("Bakiyeniz Aşşağıda Tebriklerr ")
            print(bakiye * 2)
            time.sleep(2)
        else:
            bakiye=bakiye / 2
            print("Bakiyeniz :(")
            print(bakiye / 2)
    if k=='2':
        print("Zar Tahmin Oyununa Hoş Geldiniz!")
        time.sleep(2)
        print("1 ile 6 arasında bir sayı seçin ve zar atın.")
        tahmin = int(input("Tahmininiz nedir? "))
        time.sleep(2)
        zar = random.randint(1, 6)
        print("Zar atıldı! Sonuç:", zar)
        time.sleep(2)
        if tahmin == zar:
                    print("Tebrikler, doğru tahmin ettininiz")
                    print("Bakiyeniz Aşşağıda")
                    print(bakiye ** 8)
                    bakiye=bakiye ** 8
        else:
                    print("Maalesef yanlış tahmin ettiniz!")
                    print("Bakiyeniz Aşşağıda")
                    print(bakiye / 2)
                    bakiye=bakiye / 2
        if bakiye=='0':
                    print("Battınız")
                    print(bakiye)
                    a=input("Çıkmak İçib Bir Tuşa Basınız")
                    exit()
    if k=='3':
        print("Son Şans'a Hoşgeldin Bu Seçeneği Seçtikten Sonra Dönüşün Yok...")
        print("1 İle 3 Arasında Çıkan Sayıyı Doğru Bilirsen Paran 4 Katına Çıkar")
        aa=input("Tahmin Edinizz: ")
        z = random.randint(0, 4)
        print("SAYIIIIIIII")
        print(z)
        if aa==z:
            print("PARANIZ 4 KATINA ÇIKTI")
            print("Bakiyeniz Aşşağıda")
            bakiye=bakiye*4
            print(bakiye*4)
        else:
            print("Paranız Aşşağıda")
            bakiye=bakiye*0
            print(bakiye*0)
            k=input("Çıkış İçin Bir Tuşa Basın: ")
            exit()
            break
    if k=='4':
        bakiye=bakiye
        print(bakiye)