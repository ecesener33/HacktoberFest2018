
#GÖREV: Baş bırakılan yerleri doldurunuz:
#Girdileri alıyoruz:
kenar1 = int(intput("1.kenarı giriniz:"))
kenar2 = int(intput("2.kenarı giriniz:"))
kenar3 = int(intput("3.kenarı giriniz:"))

#Prizmanın hacmini cm^3 cinsinden giriniz:
hacimCM3 = kenar1 * kenar2 * kenar3

#Prizmanın hacmini litre cinsinden heaplıyoruz:
hacimL = hacimCM3/1000.0

#Çıktıyı alıyoruz:
print("Litre cinsinden hacmimiz: ", hacimL)
