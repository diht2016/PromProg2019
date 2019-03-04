#!/usr/bin/env python
import pika
import time

time.sleep(45)

conn_params = pika.ConnectionParameters('rabbit', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='q')

def callback(ch, method, properties, body):
    print(body)

channel.basic_consume(callback, queue='q')

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
except Exception:
    channel.stop_consuming()
