import pika
import os

host = os.environ.get("RABBITMQ_HOST")
queue = os.environ.get("RABBITMQ_QUEUE")

connection = pika.BlockingConnection(pika.ConnectionParameters(host))
channel = connection.channel()
channel.queue_declare(queue = queue)