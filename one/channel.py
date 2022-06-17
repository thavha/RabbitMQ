#!/usr/bin/env python
import pika
import os

host = os.environ.get("RABBITMQ_HOST", "localhost")
queue = os.environ.get("RABBITMQ_QUEUE", "hello")
message_to_send = os.environ.get("RABBITMQ_MESSAGE", "Hello World!")

connection = pika.BlockingConnection(pika.ConnectionParameters(host))
channel = connection.channel()


