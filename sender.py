#!/usr/bin/env python

#pip install pika
import pika

from random import randrange

credentials = pika.PlainCredentials('vet_writer', 'writer.2022')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.3.37', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='vet_events_queue', durable=True)

value = str(randrange(10))
r = channel.basic_publish(exchange='vet_events', routing_key='', body='Hello World! ' + value)
print(" [x] Sent 'Hello World! "+ value + "'")
print(r)
connection.close()