#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import Request, urlopen
import time
from pprint import pprint


# from send_messages import sendtext
# from writeout import write_out


def get_text_from_website(url):
    html = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()
    soup = BeautifulSoup(html, 'html.parser')
    return "".join(soup.get_text())


if __name__ == '__main__':
    x = re.sub(' +', ' ', get_text_from_website('https://www.warbyparker.com/jobs'))
    # time.sleep(3)
    y = re.sub(' +', ' ', get_text_from_website('https://www.warbyparker.com/jobs'))
    pprint(x)

