#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
from pprint import pprint

# from send_messages import sendtext
# from writeout import write_out


def get_text_from_website(url):
    links = []
    html = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()
    soup = BeautifulSoup(html, 'html.parser')
    for line in soup.find_all('a'):
        links.append(line.get('href'))
    return len(links)


if __name__ == '__main__':
    x = get_text_from_website('https://www.datadoghq.com/jobs-engineering/')
    time.sleep(1)
    y = get_text_from_website('https://www.datadoghq.com/jobs-engineering/')
    print(x, y)
    print(x == y)
