numeros = []

while True:
    numero = int(input("Introduce un número para la lista y cero para terminar: "))
    if numero == 0:
        break
    numeros.append(numero)

numeros.sort()
print("Números ordenados de menor a mayor:", numeros)
