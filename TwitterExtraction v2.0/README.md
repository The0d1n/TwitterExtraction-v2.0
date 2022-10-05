# Twitter Extraction v2.0

Twitter Extraction v2.0 can be used to search for and display tweets containing custom keywords from user specified geographical locations.

This script uses Twint instead of the traditional Twitter API to extract tweets, replacing the use of longitude and latitude inputs for name of location.

The script uses a Flask webapp for user interaction.

## Advantage
Some of the benefits of using Twint vs Twitter API:

- Can fetch almost all Tweets (Twitter API limits to last 3200 Tweets- only);
- Fast initial setup;
- Can be used anonymously and without Twitter sign up;
- No rate limitations.

## Requirements

- twint
- Flask
- python3.6+
- aiohttp;
- aiodns;
- beautifulsoup4;
- cchardet;
- dataclasses
- elasticsearch;
- pysocks;
- pandas (>=0.23.0);
- aiohttp_socks;
- schedule;
- geopy;
- fake-useragent;
- py-googletransx.


## Usage

Run the script and open `http://127.0.0.1:3000` in your browser.