lista=[]
pares=[]
cantidad_datos=int(input("ingresa la cantidad de datos:"))
for i in range(cantidad_datos):
    valor=int(input("ingrese un numero "+str(i+1)+": "))
    lista.append(valor)
    if valor %2==0:
        pares.append(valor)
print(pares)        
    
   
    
    
