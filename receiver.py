#!/usr/bin/env python
import pika, sys, os

def main():
    credentials = pika.PlainCredentials('vet_reader', 'reader.2022')
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.3.37', 5672, '/', credentials))
    channel = connection.channel()

    channel.queue_declare(queue='vet_events_queue', durable=True)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

    channel.basic_consume(queue='vet_events_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)