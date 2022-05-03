#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

name = input("enter your name : ")
channel.basic_publish(exchange='', routing_key='hello', body= name)
print("Sent {}".format(name))
connection.close()


