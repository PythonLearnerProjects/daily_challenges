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



""" Commented out the process of exploration.
# First we can take a look at the data.
# Doing this in interactive mode with 'python3 -i exercise.py' can be useful
print(type(stackoverflow_trends))
# <class 'dict'> It's a dictionary, so it will have keys.

# Have a look at those:
for key in stackoverflow_trends.keys():
    print(key, type(stackoverflow_trends[key]), len(stackoverflow_trends[key]))

# Year <class 'list'> 137 
# Month <class 'list'> 137 
# TagPercents <class 'dict'> 2777

# So year and month are the same length...that's weird.
# TagPercents is a dict and it's much longer

# Look at the years and the months
print(stackoverflow_trends['Year'][:10])
print(stackoverflow_trends['Month'][:10])

# Oh, the years repeat and match up with the months.
# We're guessing the data is a series of lists of length 137, where
# The list index lines up for the year, month, and percentage.

# Look at some of the keys the Keys and one item for TagPercents.
list_of_keys = list(stackoverflow_trends['TagPercents'].keys())
print(list_of_keys[:10])
list_of_values = list(stackoverflow_trends['TagPercents'].values())
print(len(list_of_values[0]), list_of_values[0][:10])

"""

# Finally we print our answer.
year = stackoverflow_trends['Year'][-1]
month = stackoverflow_trends['Month'][-1]
popularity = stackoverflow_trends['TagPercents']['python'][-1]
print(f"The popularity of python for {year}-{month} is: {popularity:.3}%")
print("Go Python!")
