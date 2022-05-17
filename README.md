# RabbitMQ ejemplos para CPATU

Hay dos scripts para el ejemplo: 
* **sender.py**: envia un mensaje random a la cola **vet_events_queue** en cada ejecución.
* **receiver.py**: se ejecuta y queda escuchando la cola **vet_events_queue** en loop.


Adjunto video para ejemplo (test.mp4).


La dirección del servidor rabbitmq es:
* host: 192.168.3.37
* port: 5672
* virtual host: '/'
* exchange: vet_events
* queue: vet_events_queue

Usuarios:
* vet_reader / reader.2022 
* vet_writer / writer.2022

Autoflot debe conectarse como consumidor a la queue y vet como publicador va a enviar a esa cola a través del exchange.

En resumen, Autoflot debe implementar el comportamiento de **receiver.py** y puede hacer pruebas con el **sender.py**