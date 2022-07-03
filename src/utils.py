import json
from datetime import datetime, timedelta


def format_date(date):
    """Returns the time in the format:
    (YYYY, MM, DD) as a tuple of strings
    
    Args:
        date (datetime object): the time to format
    Returns:
        tuple: the formatted time
    """
    return (date.strftime('%Y'), date.strftime('%m'), date.strftime('%d'))


def now():
    """
    Returns the current time in the format:
    (YYYY, MM, DD) as a tuple of strings
    """
    return format_date(datetime.today())


def duration_in_days(duration):
    """Return the duration in number of days

    Args:
        duration (string): a time duration ('2d', '7d', '30d', '90d', '1y', '4y')
                           
    Returns:
        int: the duration in days
    """
    if duration == '2d':
        return 2
    elif duration == '7d':
        return 7
    elif duration == '30d':
        return 30
    elif duration == '90d':
        return 90
    elif duration == '1y':
        return 365
    elif duration == '4y':
        return 365 * 4
    else:
        return None


def begin_date(end_date, duration):
    """Return the begin data given the end data and duration
    in the format:
    (YYYY, MM, DD) as a tuple of strings

    Args:
        end_date (datetime): the end date to substract the duration from
        duration (int): the duration in days
    Returns:
        datetime: the begin date
    """
    begin_date = end_date - timedelta(days=duration)
    return format_date(begin_date)


def add_to_json(json_file, elements):
    """Append a list of elements to a json file, if the file does not exist, create it and add the elements

    Args:
        json_file (json): the file path of the json file
        elements (List): a list of elements to append to the json file
    """
    try:
        with open(json_file, 'r+') as outfile:
            j = json.load(outfile)
            outfile.seek(0)
            for element in elements:
                j.append(element)
            json.dump(j, outfile, indent=4)
    except FileNotFoundError:
        with open(json_file, 'w') as outfile:
            json.dump(elements, outfile, indent=4)