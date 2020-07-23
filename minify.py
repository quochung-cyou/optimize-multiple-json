#!/usr/bin/env python3
"""JSON minify program. """

import json # import json library
import sys # import sys library
import os

path = os.getcwd()
filelist = os.listdir(path)

def minify(file_name):
    "Minify JSON"
    if file_name.endswith('.json'):
    	file_data = open(file_name, "r", 1).read() # store file info in variable
    	json_data = json.loads(file_data) # store in json structure
    	json_string = json.dumps(json_data, separators=(',', ":")) # Compact JSON structure
    	file_name = str(file_name).replace(".json", "") # remove .json from end of file_name string
    	new_file_name = "{0}.json".format(file_name)
    	open(new_file_name, "w+", 1).write(json_string) # open and write json_string to file
for file in filelist:
	try:
		minify(file)
		print("Minify " + file)
	except:
  		print("An exception occurred " + file)

ARGS = sys.argv[1:] # get arguments passed to command line excluding first arg
for arg in ARGS: # loop through arguments
    minify(arg)

