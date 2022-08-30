suma=0.0
media=0.0
C=0
Temp=[]
print("ingrese la cantidad de temperaturas")
N=int(input())
for i in range(N):
    temperatura = float( input("Ingrese Temperatura {0}: ".format(i + 1) ))
    Temp.append(temperatura)
    suma=suma+Temp[i]
media=suma/N
for temperatura in Temp:
    if temperatura >= media:
        C=C+1
        print(temperatura)
print ("La media es ", media)
print ("Total de temperaturas >= a la media es", C)