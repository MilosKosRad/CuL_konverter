import string

NusicFajl = open("nusic-svet.txt", "r", encoding="utf-8")

#from string import maketrans

cirilica = "AбвгдђежзијклмнопрстћуфхцчшAБВГДЂЕЖЗИЈКЛМНОПРСТЋУФХЦЧШ"
latinica = "abvgdđežzijklmnoprstćufhcčšABVGDĐEŽZIJKLMNOPRSTĆUFHCČŠ"
konvertuj = str.maketrans(cirilica, latinica)

for red in NusicFajl:
   redcirilica = red.translate(konvertuj)
   redcirilica = redcirilica.replace("њ", "nj")
   redcirilica = redcirilica.replace("Њ", "Nj")
   redcirilica = redcirilica.replace("љ", "lj")
   redcirilica = redcirilica.replace("Љ", "Lj")
   redcirilica = redcirilica.replace("џ", "dž")
   redcirilica = redcirilica.replace("Џ", "Dž")

   cirilicaNusic = open("Nusic_cirilica.txt", "a+", encoding="utf-8")
   cirilicaNusic.write(redcirilica)
   cirilicaNusic.close()

NusicFajl.close()