



         #исправленный вариант 1
while True:
    try:
    
        a = int(input("Введите целое число => "))
        break
    except ValueError:
        print("Это не целое число")

if a == 0:
    print("Нет смысла ничего делать с нулём")
else:
    print("Введено целое число:", a)







#from datetime import *
#from random import *


#for j in range(1,11):
#    for i in range (1,11):
#        print({j*i:4}end=" ")
#    print()   
 




#from datetime import *
#from random import *

#algsumma=float(input("Mis summa paneme panka?"))
#alg=Lõppsumma=algsumma
#intress=randint(1,10)
#print(f"paned panka summa, mis võrdub{algsumma}. Intress on {intress} ")
#aastad=int(input("Mitmeks aastaks"))
#for i in range(1,aastad+1):
#    print(i)
#    intsumma=(algsumma*intress)/100  
#    Lõppsumma=algsumma+intsumma
#    print(f"{i} {algsumma} {intsumma} {Lõppsumma}")
#    algsumma=Lõppsumma
#print(f"Summa kokku: {Lõppsumma} Eur")
#print(f"Kasum: {Lõppsumma-alg} Eur")
    














#print("Arv ruut Kuup")
#print()
#print("-------------")
#print()

#for i in range(1,11):
#    ruut = i ** 2 
#    kuup = i ** 3 
#    print(f"{i:2} {ruut:2} {kuup:3}")






#11
#from random import *
#from termios import *
#number=randint
#katsed=3
#while katsed>0:
#    külaline = int(input("Угадайте число от 1 до 100: "))
#    if külaline == number:
#        print("Поздравляю, вы угадали число!")
#    else:
#        katsed -= 1 
#        print(f"Неверно. У вас осталось {katsed} попыток")
#        if katsed == 0:
#            print(f"Извините, вы израсходывали все свои попытки. Загаданное число было {number}.")
#            veelkord = input("Хотите ли угадать: ").lower
#            if veelkord.lower()=="нет":
#               break
#            else:
#               katsed=3












#paaris=0
#paaritu=0
#for i in range(1,101):
#    if i%2==0:
#        print(f"{i}-paaris")
#        paaris+=1
#    else:
#        print(f"{i}-paaris")
#        paaris+=1

#print(f"Paarisarvude arv: paaris")
#print(f"Paaritute arvude arv: {paaritu}")






#15
#katsed = 0
#while True:
#    vastus = input("Osta elevant ära! Kirjuta 'elevant': ")
#    katsed += 1 


#    if vastus.lower() == 'elevant':
#       print(f"Õige! Ostsid elevanti ära {katsed} katsega")
#       break
#    else:
#        print("Vale vastus. Proovi uuesti")









#4 Решено 2 способами

#arv=["1","2","3","4","5","6","7","8","9","10"]
#for i in range(10):
# print(f"{arv[i]}")


#for i in range(1,11):   #взяты числа от 1 до 10
#   tulemus =(i)    # i умножаем на 5 (1,11)
#   print(f"{i}")



#from datetime import *
#from random import *
#k=0
#while True:
#    k+=1
#    a=randint(1,50)
#    b=randint(1,50)
#    p=0
#    while p!=3:
#        p+=1
#        v=int(input("Millega võrdub {0}+{1}= ".format(a,b)))
#        if v==a+b:
#            print("Tubli!")
#            break
#        else:
#            print("Mõtle veel!")
#    print("{0}+{1}={2}".format(a,b,a+b))
#    if k==5:break








#from datetime import *
#from random import *


#summa=0
#for i in range(10):
#    arv=float(input("Sisesta arv: "))
#    summa+=arv
#print(summa)
#summa=0
#i=0
#while True:
#    i+=1
#    arv=float(input("Sisesta arv: "))
#    summa+=arv
#    if i==10: break
#print(summa)







##sum_arvud = 0
##while True:
#    try:
#        input_str = input("Sisestage arv (või vajutage lõpetamiseks Enter): ")
#        if not input_str:
#            break  # Прерываем цикл, если введенная строка пуста (Enter)
#        number = float(input_str)
#        sum_arvud += number
#    except ValueError:
#        print("Viga! Sisestage õige numbe.")





#1
#from random import *
#from datetime import *
#nimi=input("Mis on sinu nimi?").capitalize
#mitu=int(input("Mitu korda tervitada?"))
#for i in range(1,mitu+1):
#    print("Ole tervitatud, "+nimi+", "+str(i)+". korda.")





#Таблица умножения на 5
#from random import *
#from datetime import *

#korrutamine=["5"]
#arv=["1","2","3","4","5","6","7","8","9","10"]
#for i in range(10):
#   tulemus = int(arv[i]) * 5
#   print(f"{arv[i]} * 5 = {tulemus}")




#korrutamine=5

#for i in range(1,11):   #взяты числа от 1 до 10
#   tulemus =(i) * 5     # i умножаем на 5 (1,11)
#   print(f"{i} * 5 = {tulemus}")






#from random import *
#from datetime import *
##komm
#print("1. variandt -while True-")
#while True:
#    v=input("Tahan komme!").lower()
#    if v=="komm": break


#print("2. variandint -while tingimusega-")
#v=""
#while v!="komm":
#     v=input("Tahan komme!").lower()







#from random import *
#from datetime import *

#paevad=["Esmapäev","Tesipäev","Kolmapäev","Neljapäev","Reede","Laupäev","Pühapäev"]
#tunnid=["8 tundi","9 tundi","2 tundi","7 tundi","4 tundi","tuni pole","tundi pole"] 
#for i in range(7):
#    print(paevad[i]+"-"+tunnid[i])








#from random import *
#from datetime import *
#arve_nr=datetime.now() #date.today()
#print(arve_nr)
#tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0
#tooded=["Piim","Leib","Komm"] #index 0-1-2
#for i in range(3): #Первое число равно 3 второе число равно 2 и третье число равно 1
#    toode="piim"[i]
#    hind=randint(50,150)/100
#    v=input("Toode:"+toode+ " Hind "+str(hind)+ "\nKas tahad osta?").lower()
#    if v=="jah":
#       mitu=int(input("Mitu?"))
#       tsekk+=toode+ " "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#       summa+mitu*hind


#tsekk+="Kokku maksta: "+str(summa)
