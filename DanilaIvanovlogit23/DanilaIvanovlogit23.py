
#ИНДЕКС МАССЫ ТЕЛА


from operator import length_hint


print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis on sinu nimi? ").capitalize()
print("oi kui ilus nimi! " +nimi+ "!")
indeks=input("Kas leian Sinu keha indeksi? 0-ei, 1-jah =>").capitalize()

length = len(nimi)
mass = float(input("Öelge oma kehakaal:" ))
if mass > 200:
  print("Seda on liiga palju!")
  i = mass / (0.01 * length) ** 2
  print(nimi + "Teie keha indeks", i)
    if i < 16:
        print("Ebapiisav kaal")
    elif 16 <= i < 25:
        print("Ebapiisav kaal")
    elif 19 <= i < 45:
        print("Normaalne kaal")
    elif 25 <= i < 50:
        print("Normaalne kaal")
    elif 30 <= i < 40:
        print("suur kaal")
    elif 35 <= i < 60:
        print("suur kaal")
    else:
        print("ohtlik kaal tervisele")
  else:
    print("Жалко! see on väga oluline.")
print("Näeme hiljem, ", name ,"! sinu sõber!!")









#14
#from random import *
#from datetime import *
#a=10             #int
#b=2.3            #float
#c="programma"    #str
#d="proga1"       #str
#print(b.is_integer())    #False
#print(c.isalpha())       #True
#print(d.isalpha())       #False
#print(d.isnumeric())     #False
#print(d.isdigit())       #False
#print(d.isdecimal())     #False


#13 Улучшенный код 
#try:
#    gender=input("Sugu: ")
#    if gender.isalpha() and (gender.lower()=="naine" or gender.lower()=="mees"):
#        if gender.lower()=="naine":
#            print("Ei soobi")
#        else:
#            try:
#                age=int(input("Vanus:"))
#                if 16<=age<=18:
#                    print("Oled meeskonnas")
#                else:
#                    print("Vanus ei soobi!")
#            except:
#                print("Vale vanus! Viga andmetüübiga!")
#    else:
#        print("Sisesta õige tekst!")
#except :
#    print("Viga andmetüübiga")






#try:
#    s1 = float(input("Введите длину первой стороны квадрата: "))
#    s2 = float(input("Введите длину второй стороны квадрата: "))

#    if s1 == s2:
#        print("Это квадрат!")
#    else:
#        print("Это не квадрат!")
#except :
#    print("Где-то оишкбка")









###12
#try:
#    hind = float(input("Sisesta toote hind:"))
#    if hind <=10:

#       soodustus = hind * 0.1
#    elif hind > 165:
#            print("Hind on liiga kõrge!")
#    else:
#        soodustus = hind * 0.2
#    if okonnelik_hind < 0:
#        print("Hind on alla nulli!")
#    print("Lõplik hind on", okonnelik_hind, "$")

#except:
#        print("Kusagil andmete viga!")









##13
#gender=input("Kas sa oled mees v´õi naine?")
#if gender.lower()=="naine":
#    print("Kahjuks, otsime ainult mehi")
#else:
#     age=int(input("Palun märkige oma vanus"))
#     if age>=16 and age <=18:
#         print("Sa sobid meie meeskonda")
#     else:
#        print("Kahjuks sa ei sobi meie meeskonda")







#8
#from random import *
#from datetime import *
#arve_nr=datetime.now() #date.today()
#print(arve_nr)
#import datetime

#x = datetime.datetime.now()

#tsekk="Arve: 12345\nToode Hind Kogus Summa"
#summa=0
#toode="piim"
#hind=randint(50,150)/100
#v=input("Toode:"+toode+ " Hind "+str(hind)+ "\nKas tahad osta?").lower()
#if v=="jah":
#  mitu=int(input("Mitu?"))
#  tsekk+=toode+" "+str(hind)+" "+str(mitu)+ " "+str(mitu*hind)+ "\n"
#  summa+=mitu*hind
#toode="leib"
#hind=randint(50,150)/100
#v=input("Toode:"+toode+ " Hind "+str(hind)+ "\nKas tahad osta?").lower()
#if v=="jah":
#  mitu=int(input("Mitu?"))
#  tsekk+=toode+" "+str(hind)+" "+str(mitu)+ " "+str(mitu*hind)+ "\n"
#  summa+=mitu*hind
#toode="saia"
#hind=randint(50,150)/100
#v=input("Toode:"+toode+ " Hind "+str(hind)+ "\nKas tahad osta?").lower()
#if v=="jah":
#  mitu=int(input("Mitu?"))
#  tsekk+=toode+" "+str(hind)+" "+str(mitu)+ " "+str(mitu*hind)+ "\n"
#  summa+=mitu*hind
#  tsekk+="Kokku maksta: "+str(summa)





#7
#sugu=input("Kas sa oled mees või naine").lower()
#if sugu=="naine" or sugu=="n" :
#    l1=135
#    l2=180
#    l3=200
#elif  sugu=="mees" or sugu=="m" :
#    l1=150
#    l2=165
#    l3=180
#else:
#    l1=0
#    print("Viga")
#    if l1!=0:
#try:
#    pikkus=int(input("Sisesta oma pikkus: "))
#    if pikkus>29 and pikkus<l1:
#      vastus="luhike"
#    elif pikkus>=l1 and pikkus>l2:
#      vastus="keskmine"
#    elif pikkus>l2 and pikkus<=l3:
#      vastus="pikk" 
#    else:
#         vastus="tundmatu"
#    print("Sinu pikkus on {0}".format(vastus))
#except :
#    print("Неправильный формат")





##6

#try:
#    hight=int(input("Какого ты роста?"))
#    if hight>0 and hight<100:
#      print ("Ты низкого роста")
#    elif 80 < hight <= 135 :
#      print ("Ты среднего роста")
#    elif 165 < hight <= 180 :
#      print ("Ты высокого роста")
#    elif 180 < hight <= 200 :
#        vastus="pikk"
#    else:
#         vastus="tundmatu"
#    print("Твой рост {0}".format(vastus))
#except :
#    print("Неправильный формат")
