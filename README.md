*BEWARE: WORK IN PROGRESS*

# Installation
1. Copy the example config file to `config.cfg` (important!) and add your configuration.
2. (Recommended) Create a separate virtenv.
3. Run `pip install -r requirements.txt` to install dependencies.
4. Run the script.

# Tracing messages
https://www.rabbitmq.com/firehose.html
Log in to your Rabbit host and run:
`rabbitmqctl trace_on`
to enable the tracing plugin.
In the config file set `exchange` to `amq.rabbitmq.trace` and `queue` to `publish.exchangename` to see messages entering the "exchangename" exchange or `deliver.queuename` to get a CC of messages directed to the "queuename" queue.

# Usage
Run:
`python attach_to_topic_exchange.py`
to start listening.

# Known issues
* The name of the config file -- `config.cfg` -- is hard-coded for now.
* The config file has to be in the current directory (so just `cd` here before running the script).
