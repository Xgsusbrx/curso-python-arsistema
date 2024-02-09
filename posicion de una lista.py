lista_compras=["queso", "mani","platos", "frutas", "tenedores" ]
articulo=(input("verifica si tienes un articulo: "))
for i in range(len(lista_compras)):
    if lista_compras[i]==articulo:
        print("está en la posicion", i+1)
        break
else:
    print("no se encuentra")

 



