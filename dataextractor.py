"""
dataextractor.py will extract the data from the page source that is extracted by selenium.
"""

from html.parser import HTMLParser


class DataExtractor(HTMLParser):

    row_data_counter = 0
    theading_counter = 0
    tdata_counter = 0
    theading = []
    tdata = []
    data = []

    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            DataExtractor.row_data_counter += 1
        elif tag == 'th':
            DataExtractor.theading_counter += 1
        elif tag == 'td':
            DataExtractor.tdata_counter += 1

    def handle_endtag(self, tag):
        if tag == 'tr':
            DataExtractor.row_data_counter -= 1
        elif tag == 'th':
            DataExtractor.theading_counter -= 1
            DataExtractor.theading = list(filter(lambda x: x != '\n', DataExtractor.theading))
            DataExtractor.theading = ' '.join(DataExtractor.theading)
            DataExtractor.data.append(DataExtractor.theading)
            DataExtractor.theading = []
        elif tag == 'td':
            DataExtractor.tdata_counter -= 1
            DataExtractor.tdata = list(filter(lambda x: x != '\n', DataExtractor.tdata))
            DataExtractor.tdata = ' '.join(DataExtractor.tdata)
            DataExtractor.data.append(DataExtractor.tdata)
            DataExtractor.tdata = []

    def handle_data(self, data):
        if DataExtractor.row_data_counter == 1:
            if DataExtractor.theading_counter == 1:
                DataExtractor.theading.append(data)
            if DataExtractor.tdata_counter == 1:
                DataExtractor.tdata.append(data)

    @staticmethod
    def extracted():
        DataExtractor.data = [_.replace('\n', '') for _ in DataExtractor.data]
        DataExtractor.data = [_.replace('\xa0', ' ') for _ in DataExtractor.data]
        DataExtractor.data = [_.replace('[1]', '') for _ in DataExtractor.data]
        return DataExtractor.data

    def error(self, message):
        pass

    @staticmethod
    def reset_data():
        DataExtractor.data = []
        DataExtractor.tdata = []
        DataExtractor.theading = []
