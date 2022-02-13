# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup


def get_soup(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            resp.encoding = 'utf-8'

            return BeautifulSoup(resp.text, 'lxml')

    except Exception as e:
        print(e)

    return None


if __name__ == '__main__':

    url = 'https://www.yahoo.com.tw'

    print(get_soup(url))


def get_chrome(url, path=r'c:\webdriver\chromedriver', hide=False):
    try:
        options = None

        if hide:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')

        chrome = webdriver.Chrome(path, options=options)
        chrome.implicitly_wait(10)
        chrome.get(url)

        return chrome
    except Exception as e:
        print(e)

    return None
