"""
wikid is a web scrapper that scrapes the wikipedia info-boxes from wikipedia pages.
You need to provide the link that has list of all the wikipedia pages that has infoboxes.
"""

from extractsource import ExtractSource
from dataextractor import DataExtractor

URL = input('Enter url of wikipedia page that has list of names: ')
# example: 'https://en.wikipedia.org/wiki/List_of_Indian_film_actors'
CSS_SELECTOR = 'table.infobox.biography.vcard'
XPATH = "//div[@class='div-col columns column-width']/ul/li/a"

page_source = ExtractSource(URL, CSS_SELECTOR, XPATH)
links = page_source.extract_ul()

print(len(links))
print(sorted(links))

data_extractor = DataExtractor()

for link in sorted(links):
    v_card_source = page_source.extract_vcard(link)
    data_extractor.feed(v_card_source)
    data = data_extractor.extracted()
    data_extractor.reset_data()
    print(data)


