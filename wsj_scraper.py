"""The main program of the scraper"""

from datetime import datetime

from src.scraper import scrape
from src.export import to_csv


def main():
    """The main function of the scraper"""
    query = "cryptocurrency"  # single-term
    duration = '1y'  # '2d', '7d', '30d', '90d', '1y', '4y'
    num_articles = 50  # the number of articles to scrape

    scrape_time_str = datetime.today().strftime('%Y-%m-%d')
    json_outfile_name = f"./data/{scrape_time_str}.json"
    csv_outfile_name = f"./data/{scrape_time_str}.csv"

    scrape(json_outfile_name, query, duration, num_articles)
    to_csv(json_outfile_name, csv_outfile_name, num_articles)


if __name__ == "__main__":
    main()