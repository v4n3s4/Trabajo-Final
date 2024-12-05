
precios_frutas = {
    "manzana": 800,
    "banana": 1000,
    "cereza": 3000,
    "durazno": 2500,
    "pera": 2000
}

def calcular_precio_final(nombre_fruta, cantidad):
    if nombre_fruta in precios_frutas:
        return precios_frutas[nombre_fruta] * cantidad
    else:
        print(f"no hay esa fruta{nombre_fruta}.")
        return None


nombre_fruta = input("que frtas vas a llevar: ").lower()
cantidad = float(input("poner los kilos deseados(en kg): "))


precio_final = calcular_precio_final(nombre_fruta, cantidad)


if precio_final is not None:
    print(f"El precio final por {cantidad} kg de {nombre_fruta} es: ${precio_final:.2f}")

