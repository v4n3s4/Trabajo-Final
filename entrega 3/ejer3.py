
numeros = (1, 3, 5, 7, 3, 9, 3, 2, 3, 6, 8, 3)

numero_buscado = int(input("Introduce un número para ver cuántas veces se repite en la tupla: "))

contador = numeros.count(numero_buscado)


print(f"El número {numero_buscado} se repite {contador} veces en la tupla.")
