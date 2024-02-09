nombre=str(input("ingrese su nombre "))
cvocales=0
for letra in nombre:
    if letra in ["a","e","i","o","u","A","E","I","O","U"]:

      cvocales+=1
      
print(cvocales)