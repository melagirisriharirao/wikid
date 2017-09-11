"""
extractsource.py will extract the complete webpage using selenium webdriver.
"""

from selenium import webdriver


class ExtractSource:

    url = ''
    css_selector = ''
    xpath = ''
    html_source = ''
    v_card = ''
    links = set()

    def __init__(self, url, css_selector, xpath):
        ExtractSource.url = url
        ExtractSource.css_selector = css_selector
        ExtractSource.xpath = xpath

    # this function extracts html-source of entire web-page
    @staticmethod
    def html_page_source():
        try:
            browser = webdriver.PhantomJS()
            browser.get(ExtractSource.url)
            ExtractSource.html_source = browser.page_source
            browser.quit()
        except Exception as e:
            print(e)
        return ExtractSource.html_source

    # this function extracts only v-card part present in wikipedia page
    @staticmethod
    def extract_vcard(vc_link):
        try:
            browser = webdriver.PhantomJS()
            browser.get(vc_link)
            print(vc_link)
            v_card_source = browser.find_element_by_css_selector(ExtractSource.css_selector)
            ExtractSource.v_card = v_card_source.get_attribute('innerHTML')
            browser.quit()
        except Exception as e:
            print(e)
        return ExtractSource.v_card

    # this function extracts links from the xpath provided
    @staticmethod
    def extract_ul():
        try:
            browser = webdriver.PhantomJS()
            browser.get(ExtractSource.url)
            ul_source = browser.find_elements_by_xpath(ExtractSource.xpath)
            for data in ul_source:
                ExtractSource.links.add(data.get_attribute('href'))
            browser.quit()
        except Exception as e:
            print(e)
        return ExtractSource.links
