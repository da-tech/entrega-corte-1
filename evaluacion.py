#developer Daniel Zambrano
import os
from random import randint


def main():
    global players,box
    players = randint(2,4)
    print("number of players", players)
    level = randint(1,3)
    if level == 1:
        box = 20
    elif level == 2:
       box = 30
    else :
         box = 40
    print("Level:", level)
    print("you have to reach:", box)

#aqui los dados generean aleatoriamente un numero

def start():
    status = True
    i = 1
    while status :
        os.system("cls")
        print("press any key to player",i)
        KEY = ()
        D1 = randint(1,6)
        D2 = randint(1,6)
        T = D1+D2
        print("Dado1:", D1)
        print("Dado2:", D2)
        print("Total:",T)
        i = i + 1
        if i == players+1 :
            i = 1
        KEY = input("press any key to pass the turn")
        N= T + T #este hace que se sumen los totales
        if N != box :
            N += T
        elif N == box:
            print("you win")
       

       

#comienzo
os.system ("cls")
print("BIENVENIDO")
KEY = input("press any key to star the game")
main()
KEY = input("press any key to continius")
start()
KEY = input("press any key to start the game again")








