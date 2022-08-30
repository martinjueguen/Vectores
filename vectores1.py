i=1
V=[]
print("ingrese la cantidad de numeros a ingresar")
numE=int(input())
while i <= numE:
    print("ingrese un numero")
    elemento=int(input())
    V.append(elemento)
    i=i+1
print(V)