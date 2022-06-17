#!/usr/bin/env python
import channel as module_channel

module_channel.channel.basic_publish(
    exchange="", routing_key=module_channel.queue, body= module_channel.message_to_send
)
print(f" [x] Sent '{module_channel.message_to_send}'")

module_channel.connection.close()
