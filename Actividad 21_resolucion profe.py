from random import randint
#1.- Crear una colección con 100 num. del 0 al 10
numeros=[]
for i in range(100):
    numeros.append(randint(0,10))
print(numeros)

#2.- Mostrar solo los índices pares
for i in range(len(numeros)):
    if i%2==0:  #Solo se muestran índices pares
        print(f"[{i}] : {numeros[i]}")

#3.- Mostrar el número mayor
print("El número mayor es ", max(numeros))

#4.- ¿Dónde están los números mayores?
print("Índices donde se encuentra el número mayor")
for i in range(len(numeros)):
    if numeros[i]==max(numeros):
        print(i, end=" / ")
print(" ")

#5.- Mostrar el número menor
print("El número menor es ", min(numeros))

#6.- ¿Dónde están los números menores?
print("Índices donde se encuentra el número menor")
for i in range(len(numeros)):
    if numeros[i]==min(numeros):
        print(i, end=" / ")
print(" ")