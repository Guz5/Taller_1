# Taller: crear un programa en consola que pida un número al usuario y:
# 1). imprima los números impares entere -número y nýumero
# 2). Imprima los números primos entre 0 y número*100

# El programa debe garantizar que el usuario ingrese un número >0

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def imprimir_impares_entre(num):
    print("Números impares entre -{} y {}:".format(num, num))
    for i in range(-num, num + 1):
        if i % 2 != 0:
            print(i, end=" ")

def imprimir_primos_entre(num):
    limite_superior = num * 100
    print("\nNúmeros primos entre 0 y {}:".format(limite_superior))
    for i in range(limite_superior + 1):
        if es_primo(i):
            print(i, end=" ")

def main():
    while True:
        try:
            numero = int(input("Ingrese un número mayor que 0: "))
            if numero > 0:
                imprimir_impares_entre(numero)
                imprimir_primos_entre(numero)
                break
            else:
                print("El número debe ser mayor que 0. Inténtelo de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()