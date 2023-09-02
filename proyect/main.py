import random

vidas = 5

puntos = 0

while vidas!=0:

    num = random.randint(0,9)
    
    if num != 0:
        puntos+=1
        print("Tienes ", puntos," puntos")
    else:
        vidas-=1
        print("Te quedan ", vidas," vidas")
