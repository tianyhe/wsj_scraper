"""This program exports the data from json file to a csv file"""

import json
import csv


def to_csv(input_file, output_file, num_articles):
    """Convert the input json file for articles thumbnails to csv file with corresponding headers.
    
    Args:
        input_file (json): the name of the json file to be converted
        output_file (csv): the name of the csv file to write to
        num_articles (int): the number of articles to write to the csv file
    """
    header = ['category', 'title', 'byline', 'summary', 'link']
    with open(input_file, 'r') as json_f:
        articles = json.load(json_f)
    with open(output_file, 'w', encoding='UTF8') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(header)
        for num in range(num_articles):
            writer.writerow([
                articles[num]['category'], articles[num]['title'],
                articles[num]['byline'], articles[num]['summary'],
                articles[num]['link']
            ])