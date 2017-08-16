# A script that creates a histogram of host connections to Rabbit.
# Created: 16.08.2017

rabbitmqctl list_connections peer_host | sort -n | uniq -c | sort -n -r
