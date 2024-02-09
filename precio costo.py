cdi=int(input("¿cuantos ingredientes lleva su receta?"))
lista={}
for i in range(cdi):
    ing=str(input("ingrese el ingrediente: "))
    lista[i]=i*2
print(lista)


