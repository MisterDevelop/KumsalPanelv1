import random
import time

uyuma_saat = [2,3,4,5,6,7]
random_uyuma = random.choice(uyuma_saat)

guvenme_sekli = ["Yavuz sizi ekti(onun için kek yapmıştınız).","Yaman sırasını değiştirdi.","Hamza planlara dahil edilmedi.","Yaman ona yalan söyledi."]
random_guvenme = random.choice(guvenme_sekli)


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




while True:
    print(" ")
    print("HAMZA PANEL V1 💀")
    print(" ")
    print("KIZINIZIN ADINI KOYMAK İÇİN - 1")
    print("MARTI SESİ ÇIKARMAK İÇİN - 2")
    print("MAL MAL SİNİRLENMEK İÇİN - 3")
    print("TAVUKLU BÖREK İKRAM ETMEK İÇİN - 4")
    print("UYUMAK İÇİN - 5")
    print("BİRİNE GÜVENMEK İÇİN - 6")
    print("BİRİNE ÇIKMA TEKLİFİ ETMEK İÇİN - 7")
    print(" ")
    secim = int(input("Seçiminiz?: "))
    if secim == 1:
        kiziniz = str(input("Kızınızın adını giriniz: "))
        if kiziniz == "kumsal":
            print("Doğru seçim! kızınızın ismi kumsal!")
        else:
            print("Yanlış seçim! Kumsal olmalıydı!")
        devam_etme()
    elif secim == 2:
        print("Başarıyla martı sesi çıkardınız! Sınıfın çoğu seni oruspu evladı olarak nitelendiriyor.")
        devam_etme()
    elif secim == 3:
        print("Başarıyla mal mal sinirlendiniz! Tüm sınıf seni ucube bir oruspu evladı olarak görüyor!")
        devam_etme()
    elif secim == 4:
        print(
            "Yavuza tavuklu börek ikram ettin! Yavuz emin ile böreğini paylaştı! herkes mutlu ve aranızdaki bağ güçlendi!")
        devam_etme()
    elif secim == 5:
        print(f"Başarıyla uykuya daldınız. Bütün sınıf sen uyurken anana sövdü. Uyuma süreniz: {random_uyuma} ders.")
        devam_etme()
    elif secim == 6:
        print(f"Başarıyla güvendiniz. Olay: {random_guvenme}")
        devam_etme()
    elif secim == 7:
        isim = str(input("Kime çıkma teklifi edeceksiniz?: ")).lower()
        if isim == "kumsal":
            print("Kumsal sizi işletti ve reddetti.")
        elif isim == "duru":
            print("Çıkma teklifiniz kabul edildi.")
        elif isim == "yaman":
            print("Are you gay?")
            secim_1 = str(input("Seçiminiz?: "))
            if secim_1 == "evet":
                print("Vayoc reddedildin.")
            else:
                print("ozaman sg oc")
        else:
            print(f"Çıkma teklifiniz {isim} tarafından reddedildi.")
        devam_etme()



