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

# create an eavesdropping queue using wildcards
# and attach the queue to the exchange you want to listen to
myqueue='event.sample.#'
eavexchange='ceilometer'
channel.queue_declare(queue=myqueue)
channel.queue_bind(queue=myqueue, exchange=eavexchange, routing_key=myqueue)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback, queue=myqueue, no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# clean up the queue, unbind it form the exchange and delete it
channel.queue_purge(queue=myqueue)
channel.queue_unbind(queue=myqueue, exchange=eavexchange, routing_key=myqueue)
channel.queue_delete(queue=myqueue,if_unused=True, if_empty=True)
