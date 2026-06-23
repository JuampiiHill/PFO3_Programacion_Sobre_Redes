# PFO 3 - Sistema Distribuido Cliente-Servidor

## Descripción

Proyecto académico desarrollado en Python utilizando sockets TCP.

El sistema implementa una arquitectura cliente-servidor distribuida donde múltiples clientes pueden enviar tareas al servidor. El servidor recibe las solicitudes mediante sockets TCP y las distribuye a un conjunto de workers implementados mediante un pool de hilos, procesando las tareas y devolviendo los resultados correspondientes al cliente.

Además, se presenta un diseño de arquitectura distribuida que incluye balanceo de carga, cola de mensajes y almacenamiento distribuido.


## Instalación

Clonar el repositorio:

git clone https://github.com/JuampiiHill/PFO3_Programacion_sobre_Redes.git

Ingresar a la carpeta del proyecto:

cd PFO3_Programacion_sobre_Redes

## Ejecución

### Iniciar el servidor

python server.py

### Ejecutar el cliente

Abrir una nueva terminal y ejecutar:

python client.py

## Funcionalidades

El cliente puede enviar las siguientes tareas al servidor:

* Convertir texto a mayúsculas.
* Convertir texto a minúsculas.
* Invertir texto.
* Calcular la longitud de una cadena de texto.

Las tareas son enviadas en formato JSON y procesadas por los workers del servidor.


## Autor

Juan Pablo Hillcoat

Tecnicatura Superior en Desarrollo de Software

Programación sobre Redes - PFO 3
