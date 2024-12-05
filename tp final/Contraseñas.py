import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

if __name__ == "__main__":
    longitud = int(input("Ingrese la longitud de la contraseña del 1 al 10: "))
    contraseña = generar_contraseña(longitud)
    print(f"Su nueva contraseña es: {contraseña}")
