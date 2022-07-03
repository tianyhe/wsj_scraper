from datetime import datetime
import math
import requests
import time
from bs4 import BeautifulSoup

from .utils import now, begin_date, duration_in_days, add_to_json
from .parser import parse_thumbnails


def get_url(query, duration, page):
    """Return the url to scrape
    Args:
        query (str): the query to search for
        duration (int): the duration of the articles to search for
        num_articles (int): the number of articles to search for
    Returns:
        list: the thumbnails of the articles
    """
    search_url_base = "https://www.wsj.com/search?query={}&isToggleOn=true&operator=AND&sort=date-desc&duration={}&startDate={}%2F{}%2F{}&endDate={}%2F{}%2F{}&source=wsjie%2Cblog%2Cwsjvideo%2Cinteractivemedia%2Cwsjsitesrch%2Cwsjpro%2Cwsjaudio&page={}"

    end_date = now()
    start_date = begin_date(datetime.today(), duration_in_days(duration))
    url = search_url_base.format(query, duration, start_date[0], start_date[1],
                                 start_date[2], end_date[0], end_date[1],
                                 end_date[2], page)
    return url


def get_soup(url, headers=None, payload=None):
    """Returns a BeautifulSoup object of the url
    Args:
        url (str): the url to get the soup from
        headers (dict): the headers to send with the request
        payload (dict): the payload to send with the request
    Returns:
        BeautifulSoup: the soup of the url
    """
    if headers is None:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'
        }
    if payload is None:
        payload = {}
    response = requests.get(url, headers=headers, params=payload)
    return BeautifulSoup(response.text, 'html.parser')


def yield_thumbnails(soup):
    """Yield the thumbnails of the articles from the soup
    Args:
        soup (BeautifulSoup): the soup of the url
    Returns:
        json: the thumbnails of the articles as a json
    """
    try:
        return parse_thumbnails(soup)
    except:
        print("Error parsing thumbnails")
        return None


def scrape(output_file, query, duration, num_articles=20, sleep=5):
    """Scrape articles from the WSJ with given query, duration, and number of requested articles

    Args:
        output_file (json): the json file to write the thumbnails to
        query (string): the query to search for
        duration (string): the duration (date range) to search for
        num_articles (int): the number of articles to scrape
    """
    for i in range(1, math.ceil(num_articles / 20) + 1):
        time.sleep(sleep)
        url = get_url(query, duration, i)
        soup = get_soup(url)
        thumbnails = yield_thumbnails(soup)
        add_to_json(output_file, thumbnails)
        # print(f"{len(thumbnails)} retrieved")
