meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

numero = -1

while numero != 0:
    numero = int(input("Elegir un número entre 1 y el 12 para el mes del año y cero para terminar: "))

    if numero == 0:
        print("Programa terminado.")
    else:
        if 1 <= numero <= len(meses):
            print(meses[numero - 1])
        else:
            print("Inserta un número entre 1 y", len(meses))
