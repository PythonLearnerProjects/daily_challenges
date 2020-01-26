# This is the python default library for handling urls and web requests.
# It was picked because it doesn't require installing anything on most systems
# but you may want to look at requests 'python3 -m pip install requests` 
# for something that's nicer to use
from urllib import request
# This library is for reading and writing JSON data.
import json

# Send the get request.
response = request.urlopen("https://insights.stackoverflow.com/trends/get-data")
# Read the output.
payload = response.read()
# load JSON data from a string into a native python object.
stackoverflow_trends = json.loads(payload)
