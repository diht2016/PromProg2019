#!/usr/bin/env python
import pika
import time
import random

conn_params = pika.ConnectionParameters('localhost', 5680)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='q')

while True:
    channel.basic_publish(exchange='', routing_key='q', body=srt(random.randrange(200)))
    time.sleep(random.randrange(2000))

connection.close()
