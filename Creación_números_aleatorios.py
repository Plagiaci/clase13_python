from random import randint

numeros=[]

try:
    print("================================================================================================")
    for i in range(100):
        n=randint(0,10)
        numeros.append(n)
    print(numeros)
    print("================================================================================================")
    for i in range(len(numeros)):
        if i%2==0:
            print(f"{i}.- {numeros[i]}")
    print("================================================================================================")
    print(f"Número mayor : {max(numeros)}")
    print("El número mayor se repite en las posiciones : ")
    for i in range(len(numeros)):
        if numeros[i]==max(numeros):
            print(":", i,end=" : ")
    print(" ")
    print("================================================================================================")
    print(f"Número menor : {min(numeros)}")
    print("El número menor se repite en las posiciones : ")
    for i in range(len(numeros)):
        if numeros[i]==min(numeros):
            print(":", i,end=" : ")
    print(" ")
    print("================================================================================================")
except Exception as e:
    print(f"Error, {e}")