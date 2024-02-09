nombre=str(input("ingrese su nombre "))
cvocales=0
for i in nombre:
    if i=="a"or i=="e"or i=="i"or i=="o" or i=="u":
      cvocales+=1
      
print(cvocales)