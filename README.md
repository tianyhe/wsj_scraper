# WSJ Recent Headlines Thumbnail Scraper

The body of the Wall Street Journal (WSJ) is not scrapped as it is a news site that requires subscriptions.

Scraped thumbnail contains:

- Category of the headline
- The title of the headline
- The byline (author) of the headline
- The summary of the headline
- The link of the headline

The scraped thumbnails will be stored as both a json and a csv file for further parsing and analysis.

---

## Output

**Example of json output file:**

```
{
    "category": "Finance",
    "title": "Coinbase Launches Derivatives Product in Crowded Market",
    "byline": "Paul Vigna",
    "summary": "Coinbase just introduced a derivatives product, its latest attempt to move into a new field and offset weakness in its core spot-trading business. It has a lot of competition.",
    "link": "https://www.wsj.com/articles/coinbase-launches-derivatives-product-in-crowdedand-depressedmarket-11656763202?mod=Searchresults_pos1&page=1"
},
...
```

**Example of csv output file:**

```
category,title,byline,summary,link

Finance,Coinbase Launches Derivatives Product in Crowded Market,Paul Vigna,"Coinbase just introduced a derivatives product, its latest attempt to move into a new field and offset weakness in its core spot-trading business. It has a lot of competition.",https://www.wsj.com/articles/coinbase-launches-derivatives-product-in-crowdedand-depressedmarket-11656763202?mod=Searchresults_pos1&page=1

...
```

---

## Script

**Parameters for the scrape**
| Argument | type | note |
| ------------- | ------------- | ------------- |
| query | string | the keyword to search for |
| duration | string | the data range of the search <br> option: '2d', '7d', '30d', '90d', '1y', '4y'</br>|
| num_articles | int | the number of headline to scrape (default to 20 entries) |

---

## Future Improvements

- Still unable to extract the timestamp from the thumbnails (need to be fixed)
- Export to database (probably after I take some classes on it)
