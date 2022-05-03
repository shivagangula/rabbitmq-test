import pika
import sys
import os

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def Subscriber(ch, method, properties, body):
    print("Recevied Content {}".format(body.decode()))


channel.basic_consume(
    queue='hello', on_message_callback=Subscriber, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()

