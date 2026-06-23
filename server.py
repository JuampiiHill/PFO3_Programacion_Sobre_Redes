# Importamos las librerías necesarias
import socket
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Configuración del servidor
HOST = "localhost"
PORT = 5000

# Cantidad de workers/hilos que tendrá el servidor para procesar tareas
MAX_WORKERS = 3


# Función para guardar un registro de cada tarea procesada
def guardar_log(addr, tarea, resultado):
    registro = {
        "fecha": datetime.now().isoformat(),
        "cliente": str(addr),
        "tarea": tarea,
        "resultado": resultado
    }

    with open("tareas_log.jsonl", "a", encoding="utf-8") as archivo:
        archivo.write(json.dumps(registro, ensure_ascii=False) + "\n")


# Función que procesa la tarea recibida
def procesar_tarea(tarea):
    try:
        comando = tarea.get("comando")
        dato = tarea.get("dato")

        if not comando or dato is None:
            return {
                "status": "error",
                "mensaje": "La tarea debe incluir comando y dato"
            }

        if comando == "mayuscula":
            resultado = dato.upper()

        elif comando == "minuscula":
            resultado = dato.lower()

        elif comando == "invertir":
            resultado = dato[::-1]

        elif comando == "longitud":
            resultado = len(dato)

        else:
            return {
                "status": "error",
                "mensaje": "Comando no válido"
            }

        return {
            "status": "success",
            "resultado": resultado
        }

    except Exception as e:
        return {
            "status": "error",
            "mensaje": str(e)
        }


# Función que maneja la conexión con cada cliente
def manejar_cliente(conn, addr, executor):
    print(f"Conectado desde: {addr}")

    try:
        while True:
            data = conn.recv(1024)

            if not data:
                break

            mensaje = data.decode("utf-8")

            if mensaje.lower() == "exito":
                break

            print(f"Tarea recibida desde {addr}: {mensaje}")

            try:
                tarea = json.loads(mensaje)

            except json.JSONDecodeError:
                respuesta = {
                    "status": "error",
                    "mensaje": "Formato JSON inválido"
                }

                conn.sendall(json.dumps(respuesta).encode("utf-8"))
                continue

            # Enviamos la tarea al pool de workers
            future = executor.submit(procesar_tarea, tarea)

            # Esperamos el resultado
            resultado = future.result()

            # Guardamos un log de auditoría básico
            guardar_log(addr, tarea, resultado)

            # Respondemos al cliente
            conn.sendall(json.dumps(resultado).encode("utf-8"))

    except Exception as e:
        print(f"Error con el cliente {addr}: {e}")

    finally:
        print(f"Conexión cerrada con {addr}")
        conn.close()


# Función principal del servidor
def iniciar_servidor():
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            try:
                s.bind((HOST, PORT))

            except Exception as e:
                print(f"Error al hacer bind: {e}")
                return

            s.listen(5)

            print(f"Servidor escuchando en {HOST}:{PORT}")
            print(f"Pool de workers iniciado con {MAX_WORKERS} hilos")

            while True:
                conn, addr = s.accept()

                # Cada cliente es atendido por el pool de hilos
                executor.submit(manejar_cliente, conn, addr, executor)


if __name__ == "__main__":
    iniciar_servidor()