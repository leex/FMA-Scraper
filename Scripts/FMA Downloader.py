#!/usr/bin/env python3
import os, sys, requests, re

# The search string, you should change this to what you want to search for.
search_string = 'KEXP'

# Get the path where this script is currently executing
def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

# Remove the quotation marks at the end and beginning of the filename
def removeQuotationMarks(filename):
	return filename[1:-1]

# Create the output directory if it does not already exist
def createOutputDirectory(directory):
	if not os.path.exists(getScriptPath() + '\\' + directory):
		os.makedirs(directory)

URLs = []
files_in_working_directory = os.listdir(getScriptPath())

for file in files_in_working_directory:
	file_is_dot_fma = os.path.splitext(file)[1] == '.fma'

	if file_is_dot_fma:
		directory = 'songs'

		createOutputDirectory(directory)

		with open(file) as fma_file:
			URLs = fma_file.readlines()

		for URL in URLs:
			response = requests.get(URL.strip(), stream=True, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'})

			# If request is successful
			if response.status_code == 200:

				# Get the filename from the headers
				song_headers = response.headers['content-disposition']
				song_filename = re.findall("filename=(.+)", song_headers)
				song_filename = song_filename[0]

				song_filename = removeQuotationMarks(song_filename)

				# Write the song file
				with open('songs/' + song_filename, 'wb') as f2:
					f2.write(response.content);