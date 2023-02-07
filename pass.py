import time
from os import system
import os

def timerstart():
    system('cls') 
    meanwhile = time.process_time()
    print("Czas pracy:",meanwhile,"sek")
    

def check(chance, passw, x):
    temp = 0
    for z in range(len(passw)):
        if(passw[z]==chance[z]):
            temp+=1
    if(temp == len(passw)):
        end = time.process_time()
        system('cls') 
        print("HASLO TO:",passw)
        print(chance)
        print("Czas pracy:",end,"sek")
        os.system("PAUSE")
        exit(0)
    temp = 0
    if(x == 1):
        print(chance)

print("*****************Password Cracker*****************")
print("*                                                *")
print("*     Czy włączyć tryb podglądu? (wpisz cyfrę)   *")
print("*                  1. Tak (Wolniej)              *")
print("*                  2. Nie (Szybciej)             *")
print("*                                                *")
print("**************************************************")
x=0
while True:
    x=(int(input()))
    if(x == 1 or x == 2):
        break

lib = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
badlib = ",./;'[]<>?:|}{\"\\-_=+`~"
chance = []
flag = 0
passw = input("Podaj haslo: ")
while flag==0:
    if(len(passw)>15):
        passw=(input("Wprowadz haslo krotsze niz 15 znakow: "))
    else:
        flag=1
flag=0
while flag==0:
    temp=0
    for i in range(len(passw)):
        for j in range(len(badlib)):
            if(passw[i]==badlib[j]):
                temp=1
    if(temp==1):
        passw=(input("Twoje haslo nie moze zawierac takich znakow jak: , . / ; ' [ ] < > ? } { \ | \" - _ = + ~ ` :  "))
    else:
        flag=1
                

for i in range(len(passw)):
    chance.append('?')

start = time.process_time()

for k in range(len(chance)):
    if(k==0):
        for kk in range(len(lib)):
            chance[k] = lib[kk]
            check(chance, passw, x)
    if(k==1):
        for kk in range(len(lib)):
            chance[k-1] = lib[kk]
            for kk in range(len(lib)):
                chance[k] = lib[kk]
                check(chance, passw, x)
    if(k==2):
        for kk in range(len(lib)):
            chance[k-2] = lib[kk]
            for kk in range(len(lib)):
                chance[k-1] = lib[kk]
                for kk in range(len(lib)):
                    chance[k] = lib[kk]
                    check(chance, passw, x)
    if(k==3):
        for kk in range(len(lib)):
            chance[k-3] = lib[kk]
            timerstart()
            for kk in range(len(lib)):
                chance[k-2] = lib[kk]
                for kk in range(len(lib)):
                    chance[k-1] = lib[kk]
                    for kk in range(len(lib)):
                        chance[k] = lib[kk]
                        check(chance, passw, x)
    if(k==4):
        for kk in range(len(lib)):
            chance[k-4] = lib[kk]
            for kk in range(len(lib)):
                chance[k-3] = lib[kk]
                timerstart()
                for kk in range(len(lib)):
                    chance[k-2] = lib[kk]
                    for kk in range(len(lib)):
                        chance[k-1] = lib[kk]
                        for kk in range(len(lib)):
                            chance[k] = lib[kk]
                            check(chance, passw, x)
    if(k==5):
        for kk in range(len(lib)):
            chance[k-5] = lib[kk]
            for kk in range(len(lib)):
                chance[k-4] = lib[kk]
                for kk in range(len(lib)):
                    chance[k-3] = lib[kk]
                    timerstart()
                    for kk in range(len(lib)):
                        chance[k-2] = lib[kk]
                        for kk in range(len(lib)):
                            chance[k-1] = lib[kk]
                            for kk in range(len(lib)):
                                chance[k] = lib[kk]
                                check(chance, passw, x)
    if(k==6):
        for kk in range(len(lib)):
            chance[k-6] = lib[kk]
            for kk in range(len(lib)):
                chance[k-5] = lib[kk]
                for kk in range(len(lib)):
                    chance[k-4] = lib[kk]
                    for kk in range(len(lib)):
                        chance[k-3] = lib[kk]
                        timerstart()
                        for kk in range(len(lib)):
                            chance[k-2] = lib[kk]
                            for kk in range(len(lib)):
                                chance[k-1] = lib[kk]
                                for kk in range(len(lib)):
                                    chance[k] = lib[kk]
                                    check(chance, passw, x)
    if(k==7):
        for kk in range(len(lib)):
            chance[k-7] = lib[kk]
            for kk in range(len(lib)):
                chance[k-6] = lib[kk]
                for kk in range(len(lib)):
                    chance[k-5] = lib[kk]
                    for kk in range(len(lib)):
                        chance[k-4] = lib[kk]
                        for kk in range(len(lib)):
                            chance[k-3] = lib[kk]
                            timerstart()
                            for kk in range(len(lib)):
                                chance[k-2] = lib[kk]
                                for kk in range(len(lib)):
                                    chance[k-1] = lib[kk]
                                    for kk in range(len(lib)):
                                        chance[k] = lib[kk]
                                        check(chance, passw, x)
    if(k==8):
        for kk in range(len(lib)):
            chance[k-8] = lib[kk]
            for kk in range(len(lib)):
                chance[k-7] = lib[kk]
                for kk in range(len(lib)):
                    chance[k-6] = lib[kk]
                    for kk in range(len(lib)):
                        chance[k-5] = lib[kk]
                        for kk in range(len(lib)):
                            chance[k-4] = lib[kk]
                            for kk in range(len(lib)):
                                chance[k-3] = lib[kk]
                                timerstart()
                                for kk in range(len(lib)):
                                    chance[k-2] = lib[kk]
                                    for kk in range(len(lib)):
                                        chance[k-1] = lib[kk]
                                        for kk in range(len(lib)):
                                            chance[k] = lib[kk]
                                            check(chance, passw, x)
    if(k==9):
        for kk in range(len(lib)):
            chance[k-9] = lib[kk]
            for kk in range(len(lib)):
                chance[k-8] = lib[kk]
                for kk in range(len(lib)):
                    chance[k-7] = lib[kk]
                    for kk in range(len(lib)):
                        chance[k-6] = lib[kk]
                        for kk in range(len(lib)):
                            chance[k-5] = lib[kk]
                            for kk in range(len(lib)):
                                chance[k-4] = lib[kk]
                                for kk in range(len(lib)):
                                    chance[k-3] = lib[kk]
                                    timerstart()
                                    for kk in range(len(lib)):
                                        chance[k-2] = lib[kk]
                                        for kk in range(len(lib)):
                                            chance[k-1] = lib[kk]
                                            for kk in range(len(lib)):
                                                chance[k] = lib[kk]
                                                check(chance, passw, x)
    if(k==10):
        for kk in range(len(lib)):
            chance[k-10] = lib[kk]
            for kk in range(len(lib)):
                chance[k-9] = lib[kk]
                for kk in range(len(lib)):
                    chance[k-8] = lib[kk]
                    for kk in range(len(lib)):
                        chance[k-7] = lib[kk]
                        for kk in range(len(lib)):
                            chance[k-6] = lib[kk]
                            for kk in range(len(lib)):
                                chance[k-5] = lib[kk]
                                for kk in range(len(lib)):
                                    chance[k-4] = lib[kk]
                                    for kk in range(len(lib)):
                                        chance[k-3] = lib[kk]
                                        timerstart()
                                        for kk in range(len(lib)):
                                            chance[k-2] = lib[kk]
                                            for kk in range(len(lib)):
                                                chance[k-1] = lib[kk]
                                                for kk in range(len(lib)):
                                                    chance[k] = lib[kk]
                                                    check(chance, passw, x)
    if(k==11):
        for kk in range(len(lib)):
            chance[k-11] = lib[kk]
            for kk in range(len(lib)):
                chance[k-10] = lib[kk]
                for kk in range(len(lib)):
                    chance[k-9] = lib[kk]
                    for kk in range(len(lib)):
                        chance[k-8] = lib[kk]
                        for kk in range(len(lib)):
                            chance[k-7] = lib[kk]
                            for kk in range(len(lib)):
                                chance[k-6] = lib[kk]
                                for kk in range(len(lib)):
                                    chance[k-5] = lib[kk]
                                    for kk in range(len(lib)):
                                        chance[k-4] = lib[kk]
                                        for kk in range(len(lib)):
                                            chance[k-3] = lib[kk]
                                            timerstart()
                                            for kk in range(len(lib)):
                                                chance[k-2] = lib[kk]
                                                for kk in range(len(lib)):
                                                    chance[k-1] = lib[kk]
                                                    for kk in range(len(lib)):
                                                        chance[k] = lib[kk]
                                                        check(chance, passw, x)
    if(k==12):
        for kk in range(len(lib)):
            chance[k-12] = lib[kk]
            for kk in range(len(lib)):
                chance[k-11] = lib[kk]
                for kk in range(len(lib)):
                    chance[k-10] = lib[kk]
                    for kk in range(len(lib)):
                        chance[k-9] = lib[kk]
                        for kk in range(len(lib)):
                            chance[k-8] = lib[kk]
                            for kk in range(len(lib)):
                                chance[k-7] = lib[kk]
                                for kk in range(len(lib)):
                                    chance[k-6] = lib[kk]
                                    for kk in range(len(lib)):
                                        chance[k-5] = lib[kk]
                                        for kk in range(len(lib)):
                                            chance[k-4] = lib[kk]
                                            for kk in range(len(lib)):
                                                chance[k-3] = lib[kk]
                                                timerstart()
                                                for kk in range(len(lib)):
                                                    chance[k-2] = lib[kk]
                                                    for kk in range(len(lib)):
                                                        chance[k-1] = lib[kk]
                                                        for kk in range(len(lib)):
                                                            chance[k] = lib[kk]
                                                            check(chance, passw, x)
    if(k==13):
        for kk in range(len(lib)):
            chance[k-13] = lib[kk]
            for kk in range(len(lib)):
                chance[k-12] = lib[kk]
                for kk in range(len(lib)):
                    chance[k-11] = lib[kk]
                    for kk in range(len(lib)):
                        chance[k-10] = lib[kk]
                        for kk in range(len(lib)):
                            chance[k-9] = lib[kk]
                            for kk in range(len(lib)):
                                chance[k-8] = lib[kk]
                                for kk in range(len(lib)):
                                    chance[k-7] = lib[kk]
                                    for kk in range(len(lib)):
                                        chance[k-6] = lib[kk]
                                        for kk in range(len(lib)):
                                            chance[k-5] = lib[kk]
                                            for kk in range(len(lib)):
                                                chance[k-4] = lib[kk]
                                                for kk in range(len(lib)):
                                                    chance[k-3] = lib[kk]
                                                    timerstart()
                                                    for kk in range(len(lib)):
                                                        chance[k-2] = lib[kk]
                                                        for kk in range(len(lib)):
                                                            chance[k-1] = lib[kk]
                                                            for kk in range(len(lib)):
                                                                chance[k] = lib[kk]
                                                                check(chance, passw, x)
    if(k==14):
        for kk in range(len(lib)):
            chance[k-14] = lib[kk]
            for kk in range(len(lib)):
                chance[k-13] = lib[kk]
                for kk in range(len(lib)):
                    chance[k-12] = lib[kk]
                    for kk in range(len(lib)):
                        chance[k-11] = lib[kk]
                        for kk in range(len(lib)):
                            chance[k-10] = lib[kk]
                            for kk in range(len(lib)):
                                chance[k-9] = lib[kk]
                                for kk in range(len(lib)):
                                    chance[k-8] = lib[kk]
                                    for kk in range(len(lib)):
                                        chance[k-7] = lib[kk]
                                        for kk in range(len(lib)):
                                            chance[k-6] = lib[kk]
                                            for kk in range(len(lib)):
                                                chance[k-5] = lib[kk]
                                                for kk in range(len(lib)):
                                                    chance[k-4] = lib[kk]
                                                    for kk in range(len(lib)):
                                                        chance[k-3] = lib[kk]
                                                        timerstart()
                                                        for kk in range(len(lib)):
                                                            chance[k-2] = lib[kk]
                                                            for kk in range(len(lib)):
                                                                chance[k-1] = lib[kk]
                                                                for kk in range(len(lib)):
                                                                    chance[k] = lib[kk]
                                                                    check(chance, passw, x)

end = time.process_time()

print(end)