#!/usr/bin/env python3
import sys, requests, re, codecs
import argparse

parser = argparse.ArgumentParser(description='Scrape download links from the FMA website.')
parser.add_argument('integers', metavar='N', default=10, type=int, nargs='*',
                    help='an integer stating how many links to ignore from the start of the scrape.')

### This scraper uses the search page to find tracks then creates a file with a list of download links
args = vars(parser.parse_args())

print("\nstarting scraping\n")

# The search string, you should change this to what you want to search for
search_string = 'KEXP'

# How many records to ignore at the beginning of the scrap (if you've already scraped some)
count_offset = args['integers']

print("offset set to " + str(count_offset) + ".")

# The name of the file to create
filename = 'scraped_download_links'

# The number of items to return in the search and scrape, I have tested up to 1000
number_of_items_to_search = '100'

# The regex to find the download link, you probably don't need to change this
regex_find_download_link = re.compile('((https:\/\/freemusicarchive.org\/music\/download\/)\w+)')

# Here we open the file we will write the links to
file = codecs.open(filename + '.fma', 'w+', 'utf-8')

URL = 'http://freemusicarchive.org/search/?quicksearch=' + search_string + '&per_page=' + number_of_items_to_search
r = requests.get(URL)
content = r.text
filteredContent = re.findall(regex_find_download_link, content)

scraped_links_count = str(len(filteredContent))

print("found " + scraped_links_count + " songs.")

# Write one line to the file for each link
count = 0
for item in filteredContent:
    # Ignore lines we don't want at the beginning
    count = count + 1
    if count <= count_offset:
        continue

    # Write to the file
    file.write(item[0])
    file.write('\n')

file.close()

print("file '" + filename + ".fma' created.")
print("processed " + str(int(scraped_links_count) - count_offset) + " links.")

print("\nending scraping\n")

# @todo use the search_string to create the file but first we need to escape bad characters
# @todo create offset to being downloading after first x songs