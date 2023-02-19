import pywhatkit as kit
import pyttsx3
from pyfiglet import Figlet
import webbrowser
import qrcode
import os
from colorama import Fore, init
while True:
    init(autoreset=True)
    print(Fore.YELLOW + "SwazzAtena#1889")
    print(Fore.BLACK + "SwazzAtena#1889")
    print(Fore.BLUE + "SwazzAtena#1889")
    print(Fore.GREEN+ "SwazzAtena#1889")
    print(Fore.LIGHTRED_EX + "SwazzAtena#1889")
    print(Fore.LIGHTMAGENTA_EX + "SwazzAtena#1889")
    print(Fore.LIGHTGREEN_EX + "SwazzAtena#1889")
    print(Fore.LIGHTBLUE_EX + "SwazzAtena#1889")
    print(Fore.LIGHTYELLOW_EX + "SwazzAtena#1889")
    print(Fore.LIGHTWHITE_EX + "SwazzAtena#1889")
    print(Fore.MAGENTA + "SwazzAtena#1889")

    print("""
1)QR CODE MAKE
2)Tiktok Bot Basma
3)Metini Sese Çevirme
4)Discord Adresimiz
5)Çıkış
      """)

    islemno = input("İstediğiniz Nedir: ")
    if islemno=="1":
        data=input("Qrccode siteyi giriniz: ")
        img = qrcode.make(data)
        qrcode.make("data")
        imgg= input("Kaydedilecek dosya adı : ")
        img.save(imgg+".png")
    if islemno=="2":
        webbrowser.open("freer.in")
    if islemno=="3":
        Metin = input("Konuşturulacak Metni Seçiniz: ")
        engine = pyttsx3.init()
        engine.say(Metin)
        engine.runAndWait()
    if islemno=="5":
        f = Figlet(font='standard')
        print(f.renderText(' By Swazz'))
        break
    if islemno=="4":
        webbrowser.open("https://discord.gg/F3ddWkB6")
        break
