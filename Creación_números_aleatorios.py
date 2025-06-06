import random   #Librería para llamar y crear números al azar
#También se puede escribir 'from random import randint
numeros=[]

for i in range(100):    #Ciclo para repetir 100 las iteraciones
    n=random.randint(1,100) #Crea el número
    numeros.append(n)   #Guardamos en la lista los números

print(numeros)  #Vemos la lista