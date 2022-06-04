import channel as module_channel

import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=module_channel.host))
    channel = connection.channel()

    channel.queue_declare(queue=module_channel.queue)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue=module_channel.queue, on_message_callback=callback, auto_ack=True)

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