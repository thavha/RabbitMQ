import channel

channel.channel.basic_publish(exchange='',
                      routing_key=channel.queue,
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

channel.connection.close()