import pickle
import sys
import os
import random

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def generar_numero_ticket():
    return random.randint(1000, 9999)

def guardar_ticket(archivo, ticket):
    with open(archivo, "wb") as f:
        pickle.dump(ticket, f)

def cargar_ticket(archivo):
    with open(archivo, "rb") as f:
        return pickle.load(f)

def verificar_archivo(ruta):
    return os.path.isfile(ruta)

def alta_ticket():
    print("\nIngresar los datos para generar un nuevo Ticket")
    nombre = input(" Ingresar Nombre: ")
    sector = input(" Ingresar sector: ")
    asunto = input("Ingresar asunto: ")
    mensaje = input("Ingresar mensaje: ")

    numero_ticket = generar_numero_ticket()
    ticket = {
        "Nombre": nombre,
        "Sector": sector,
        "Asunto": asunto,
        "Mensaje": mensaje
    }
    
    archivo = f"ticket_{numero_ticket}.pkl"
    guardar_ticket(archivo, ticket)
    
    print("\nSe generó el siguiente Ticket")
    print(f"Ticket N°: {numero_ticket}")
    print(f"Su nombre: {nombre}")
    print(f"Sector: {sector}")
    print(f"Asunto: {asunto}")
    print(f"Mensaje: {mensaje}")
    print("Por favor, acuérdese del número de ticket.\n")

def leer_ticket():
    numero_ticket = int(input("Ingrese el número de ticket: "))
    archivo = f"ticket_{numero_ticket}.pkl"
    
    if verificar_archivo(archivo):
        ticket = cargar_ticket(archivo)
        print("\nTicket encontrado:")
        print(f"Ticket N°: {numero_ticket}")
        print(f"Su nombre: {ticket['Nombre']}")
        print(f"Sector: {ticket['Sector']}")
        print(f"Asunto: {ticket['Asunto']}")
        print(f"Mensaje: {ticket['Mensaje']}\n")
    else:
        print("No se encontró un ticket con ese número.\n")

def menu():
    while True:
        limpiar_pantalla()
        print("Hola, bienvenidos al sistema Ticket")
        print("1- Generar un Ticket")
        print("2- Leer un Ticket")
        print("3- Salir")
        opcion = int(input("Seleccione: "))

        if opcion == 1:
            while True:
                alta_ticket()
                otra_vez = input("¿Desea crear otro ticket? (si/no): ").lower()
                if otra_vez != "si":
                    break
        elif opcion == 2:
            while True:
                leer_ticket()
                otra_vez = input("¿Desea leer otro ticket? (si/no): ").lower()
                if otra_vez != "si":
                    break
        elif opcion == 3:
            confirmar = input("¿Está seguro que desea salir? (si/no): ").lower()
            if confirmar == "si":
                print("El programa se ha cerrado.")
                sys.exit()
            else:
                continue
        else:
            print("Error. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()
