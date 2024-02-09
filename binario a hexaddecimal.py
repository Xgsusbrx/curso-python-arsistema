def bin_to_hex(binary_number):
    decimal=int(binary_number, 2)  # Convertir el número binario a decimal
    hexadecimal=hex(decimal)  # Convertir el decimal a hexadecimal
    return hexadecimal

# Interacción con el usuario
binary_input = input("Ingresa un número binario: ")

try:
    # Verificar que el número binario es válido
    int(binary_input, 2)
    result = bin_to_hex(binary_input)
    print(f"El número binario {binary_input} en hexadecimal es: {result}")
except ValueError:
    print("Ingresa un número binario válido.")
 

