print("ingrese la cantidad de elementos de un vector")
N=int(input())
VEC = []
if N >= 1 and N<=200:
    for i in range(1,N+1):
        elemento = int( input("Ingrese Entero {0}: ".format(i)))
        VEC.append(elemento)
    i=0
    lista=[]
    for elemento in VEC:

        if elemento not in lista:
             lista.append(elemento)
        lista.sort()
print(lista)