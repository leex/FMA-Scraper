# FMA-Scraper
A collection of scripts to assist in scraping the FreeMusicArchive. This scraper specifically scrapes the Search page of the FMA website using a given search string. To see an example of downloading music by genre then see https://github.com/Kickball/FMA-Scraper which this project was based off.

You are responsible for checking license and song usage on the FMA website.

## Table of Contents

1. Overview
2. Installation
3. Usage
4. Credit

## Overview

This is a collection of scripts to aid in scraping the FMA's website for music. The first script, FMA Downloader.py should be able to scrape song download URLs from the search page given the particular search term. The second part of the script will take any '.fma' files in it's directory and process them for downloading.

## Installation

*Please note these scripts have only been tested on OSX 10.14 running Python 3.7.2

### Prerequisites

You will require:
* Python 3
* Requests
* Re
* Codecs
* Os
* Sys
* Wget
* Argparse

Most of these modules come preinstalled with Python nowadays.

## Usage

1. Copy the script files into the directory you wish for the music to be downloaded into.
2. Ensure you have write permission in that directory.
3. Run 'FMA Scraper.py', this will create a list of download URLs for songs.
4. Run 'FMA Downloader.py', this will download any lists of songs found into a directory.

## Credit

Thanks to the following parties:
* [Kickball](https://github.com/Kickball/FMA-Scraper) - for mulitple accounts of troubleshooting help.
* [AndyR207](https://github.com/AndyR207) - for mulitple accounts of troubleshooting help.

This work is based off the work done by Kickball on FMA-Scraper although no original code really exists.