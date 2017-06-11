#!/usr/bin/env python
import pika
import ConfigParser

# get config from the config file
config = ConfigParser.ConfigParser()
config.readfp(open(r'config.cfg'))
username = config.get('credentials', 'username')
password = config.get('credentials', 'password')
host = config.get('connection', 'host')
port = int( config.get('connection', 'port') )
vhost = config.get('connection', 'vhost')

# open connection to Rabbit
credentials = pika.PlainCredentials(username=username, password=password)
parameters = pika.ConnectionParameters(host=host, port=port, virtual_host=vhost, credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# get details of the queue and the exchange from the config file
eavqueue = config.get('eavesdrop', 'queue')
queue_exists = True if config.get('eavesdrop', 'queue_exists') in ('y', 'yes') else False
eavexchange = config.get('eavesdrop', 'exchange')

# declare the queue
args = {}
if queue_exists:
    print("WARNING: Attaching to an existing queue!")
    args = {"passive": True}
else:
    args = {"auto_delete": True}
channel.queue_declare(queue=eavqueue, **args)

channel.queue_bind(queue=eavqueue, exchange=eavexchange, routing_key=eavqueue)

def callback(ch, method, properties, body):
    print(" [x] Received a message")
    print(" [x] Method: %r" % method)
    print(" [x] Properties: %r" % properties)
    print(" [x] Body %r" % body)

channel.basic_consume(callback, queue=eavqueue, no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
