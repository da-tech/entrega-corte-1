#developer Daniel Zambrano
import random
import os

def game():

   print("::: HOLA :::")
   print("::: BIENVENIDO AL JUEGO DEL AHORCADO::::")
words:["hola","python","Django","java","framework","variable","cadenas","ciclos","listas"]
word = random.choice(words)

#comienzo del juego
right_letter = ""
all_letter = ""

star = True
while star :

   result = ""
    for word in words
   if word in right_letter:
      result += word
   else :
      result += "-"

   if result == word:
      prit("::: ganaste:::")
      break
   
###start
os.system ("cls")
key : input("press any key to start")
game()
