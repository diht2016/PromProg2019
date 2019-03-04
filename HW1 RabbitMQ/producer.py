#!/usr/bin/env python
import pika
import time
import random

time.sleep(45)

conn_params = pika.ConnectionParameters('rabbit', 5680)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='q')

while True:
    channel.basic_publish(exchange='', routing_key='q', body=str(random.randrange(200)))
    time.sleep(random.random())

connection.close()
