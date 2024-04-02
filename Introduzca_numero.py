def pedir_numero():
    while True:
        try:
            numero = int(input("Por favor, ingresa un número entero mayor que 0: "))
            if numero > 0:
                return numero
            else:
                print("El número debe ser mayor que 0. Intenta nuevamente.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

numero_ingresado = pedir_numero()
print("Has ingresado el número:", numero_ingresado)
