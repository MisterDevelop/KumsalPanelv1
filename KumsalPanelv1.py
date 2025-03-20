import random
import time

def devam_etme():
    devam = str(input("Çıkmak için T devam etmek D: ")).lower()
    if devam == "t":
        print("Çıkılıyor.. 3")
        time.sleep(1)
        print("Çıkılıyor.. 2")
        time.sleep(1)
        print("Çıkılıyor.. 1")
        time.sleep(1)
        exit()

ekler=[1,2,3,4,5,6]
random_ekler=random.choice(ekler)

print(" ")
print("KUMSAL PANEL v1")
print(" ")
print("ÇIKMA TEKLİFİ REDDETME - 1")
print("İNSTA STORY ATMAK İÇİN(dolandırıcı) - 2")
print("GÜNER ELAYA OROSPU DEMEK İÇİN - 3")
print("SINIFTAKİLERİ BOYAMAK İÇİN - 4")
print("KEKOLARLA TAKILMAK İÇİN - 5")
print("EKLER ALMAK İÇİN - 6")
print("TRİP ATMAK İÇİN - 7")
print("ENGELLEMEK İÇİN - 8")
print(" ")
secim = int(input("Seçim: "))
if secim == 1:
    print(" ")
    print("ŞUANKİ ÇIKMA TEKLİFLERİ")
    print("Hamza, Yaman")
    print(" ")
    reddet = str(input("Kimi reddedeceksiniz?: ")).lower()
    if reddet == "hamza":
        print("Hamza başarıyla reddedildi!")
    elif reddet == "yaman":
        print("Yaman başarıyla reddedildi!")
    devam_etme()

if secim == 2:
    print(" ")
    print("Başarıyla insta story atıldı! Yavuz ve yiğit seni dolandırıcı olarak adlandırdı!")
    devam_etme()

if secim == 3:
    print(" ")
    print("İzin veremiyoz.")
    devam_etme()

if secim == 4:
    print(" ")
    boya=str(input("Kimi boyayacaksınız?:"))
    print(boya,"Başarıyla boyandı!(sonradan hepsini sildiler)")
    devam_etme()

if secim == 5:
    print(" ")
    print("Başarıyla kekolar ile takıdınız!(bölündünüz)")
    devam_etme()

if secim == 6:
    print(" ")
    print(f"Başarıyla {random_ekler} kadar ekler satın alındı ve yarısı yavuz yada yiğite verildi!")
    devam_etme()

if secim == 7:
    print(" ")
    trip = input("Hangi sebeble trip atıcaksınız?: ")
    kime = str(input("Kime trip atacaksınız?: "))
    print(f"{kime} isimli kişiye {trip} sebebinden ötürü trip atıldı!")
    devam_etme()

if secim == 8:
    engel = input("Hangi sebeble engel atıcaksınız?: ")
    kime = str(input("Kime atacaksınız?: "))
    print(f"{kime} isimli kişiye {engel} sebebinden ötürü engel atıldı!")
    devam_etme()
        

else:
    print("Geçersiz işlem!")
    devam_etme()
