*BEWARE: WORK IN PROGRESS*

# Installation
1. Copy the example config file to `config.cfg` (important!) and add your configuration.
2. (Recommended) Create a separate virtenv.
3. Run `pip install -r requirements.txt` to install dependencies.
4. Run the script.

# Known issues
* The name of the config file -- `config.cfg` -- is hard-coded for now.
* The config file has to be in the current directory (so just `cd` here before running the script).
* (IMPORTANT!) To clean up the queue, comment out `channel.basic_consume()` and `channel.start_consuming()`.
