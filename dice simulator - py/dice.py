import random
from time import sleep
import os
A = True
while A == True:
    menor,maior = 1,int(input("Informe quantos lados tem seu dado: "))
    print("Jogando dado...")
    sleep(2)
    print("O dado caiu em: {}".format(random.randint(menor,maior)))
    A = int(input("Jogar denovo? (1-sim/2-não): "))
    if A == 1: 
        A == True
        os.system("CLS")
    if A == 2 :
        print("Fechando o programa em 5 segundos!")
        sleep(5)
        quit()
