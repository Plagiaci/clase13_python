import random   #Librería para llamar y crear números al azar
#También se puede escribir 'from random import randint
numeros=[]

for i in range(10):    #Ciclo para repetir 100 las iteraciones
    n=random.randint(1,100) #Crea el número
    numeros.append(n)   #Guardamos en la lista los números

print(numeros)  #Vemos la lista

#Contador de números pares
cont=0
for i in range(len(numeros)):
    if numeros[i]%2==0:
        cont+=1
print(f"Cantidad de números pares : {cont}")