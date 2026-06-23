# Importamos las librerías necesarias
import socket
import json

# Configuración del servidor
HOST = "localhost"
PORT = 5000


# Función para enviar una tarea al servidor
def enviar_tarea(comando, dato):
    """
    Esta función arma una tarea en formato JSON,
    la envía al servidor y espera la respuesta.
    """

    # Creamos la tarea como diccionario
    tarea = {
        "comando": comando,
        "dato": dato
    }

    # Creamos el socket del cliente
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Nos conectamos al servidor
        s.connect((HOST, PORT))

        # Convertimos el diccionario a JSON y lo enviamos codificado
        s.sendall(json.dumps(tarea).encode("utf-8"))

        # Recibimos la respuesta del servidor
        respuesta = s.recv(1024).decode("utf-8")

        # Convertimos la respuesta JSON a diccionario
        return json.loads(respuesta)


# Función principal del cliente
def main():
    """
    Menú principal del cliente.
    Permite enviar tareas al servidor.
    """

    while True:
        print("\n--- Cliente de tareas distribuidas ---")
        print("1. Convertir texto a mayúsculas")
        print("2. Convertir texto a minúsculas")
        print("3. Invertir texto")
        print("4. Calcular longitud")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            texto = input("Ingrese el texto: ")
            respuesta = enviar_tarea("mayuscula", texto)
            print("Respuesta del servidor:", respuesta)

        elif opcion == "2":
            texto = input("Ingrese el texto: ")
            respuesta = enviar_tarea("minuscula", texto)
            print("Respuesta del servidor:", respuesta)

        elif opcion == "3":
            texto = input("Ingrese el texto: ")
            respuesta = enviar_tarea("invertir", texto)
            print("Respuesta del servidor:", respuesta)

        elif opcion == "4":
            texto = input("Ingrese el texto: ")
            respuesta = enviar_tarea("longitud", texto)
            print("Respuesta del servidor:", respuesta)

        elif opcion == "5":
            print("Cliente finalizado")
            break

        else:
            print("Opción no válida")


# Punto de entrada del programa
if __name__ == "__main__":
    main()