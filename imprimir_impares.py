def imprimir_impares(num):
    for i in range(-num, num + 1):
        if i % 2 != 0:
            print(i)

# Solicitar al usuario que ingrese el número
num = int(input("Ingrese un número entero positivo: "))

# Llamar a la función para imprimir los números impares
print("Los números impares desde -{} hasta {} son:".format(num, num))
imprimir_impares(num)
