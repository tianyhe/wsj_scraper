import re
from bs4 import BeautifulSoup


def parse_thumbnails(soup):
    """Parse BeatifulSoup format article thumbnails to a list of dict
    Args:
        soup (BeautifulSoup object): articles thumbnails as soup object
    Returns: 
        A list of dicts of the article thumbnails
    """
    thumbnails = []

    def to_thumbnail(article):
        return {
            'category': parse_category(article),
            'title': parse_title(article),
            'byline': parse_byline(article),
            'summary': parse_summary(article),
            'link': parse_link(article)
        }

    for article in soup.find_all('article'):
        thumbnails.append(to_thumbnail(article))
    return thumbnails


def parse_category(article):
    """Parse the category of an article
    Args:
        article (BeautifulSoup object): an article as soup object
    Returns:
        The category of the article
    """
    try:
        return article.find('li').get_text()
    except:
        return ''


def parse_title(article):
    """Parse the title of an article
    Args:
        article (BeautifulSoup object): an article as soup object
    Returns:
        The title of the article
    """
    try:
        return article.find('span').get_text()
    except:
        return ''


def parse_summary(article):
    """Parse the summary of an article
    Args:
        article (BeautifulSoup object): an article as soup object
    Returns:
        The summary of the article
    """
    try:
        return article.find('p').get_text()
    except:
        return ''


def parse_byline(article):
    """Parse the byline of an article
    Args:
        article (BeautifulSoup object): an article as soup object
    Returns:
        The byline of the article
    """
    try:
        return article.find(
            'p', class_=re.compile('^(WSJTheme--byline)')).get_text()
    except:
        return ''


def parse_link(article):
    """Parse the link of an article
    Args:
        article (BeautifulSoup object): an article as soup object
    Returns:
        The link of the article
    """
    try:
        return article.find('a').get('href')
    except:
        return ''
