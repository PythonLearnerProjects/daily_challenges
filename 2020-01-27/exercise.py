# This is the python default library for handling urls and web requests.
# It was picked because it doesn't require installing anything on most systems
# but you may want to look at requests 'python3 -m pip install requests` 
# for something that's nicer to use
from urllib import request
# This library is for reading and writing JSON data.
import json

# The day before yesterday we learned how to read an api and explore the data output.
# Today we're going to use that to build something interactive.

def url_to_dict(url):
    # Send the get request.
    response = request.urlopen(url)
    # Read the output.
    payload = response.read()
    # load JSON data from a string into a native python object.
    return json.loads(payload)


# The site 'metaweather.com' is a free api for weather data in some major locations.

# They have a search api
where = "Stockholm"
search_output = url_to_dict(f"https://www.metaweather.com/api/location/search/?query={where}")

# And will output weather predictions from various services for any given location.
woeid = "906057"
weather_there = url_to_dict(f"https://www.metaweather.com/api/location/{woeid}")

# Example of expected output
"""
Please enter a place to retrieve weather for:
$ Lon
Thanks. Looking it up now....
I didn't find "Lon" but I did find these:
0: London
1: Barcelona
2: Long Beach
Please enter a number to select one, or text to try searching again.
$ 0
Thanks, the weather for the next five days in London is:
Prediction          | Max | Min |
Heavy Rain          |  9c |  6c |
Light Rain          |  8c |  5c |
Light Rain          |  7c |  3c |
Light Cloud         |  8c |  3c |
Heavy Rain          | 11c |  4c |
Heavy Rain          | 12c |  8c |
"""

# You may want to read help(str), help(print), and help(str.rjust)
