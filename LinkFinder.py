# -*- coding: utf-8 -*-
"""
This script gets all the internal links within a website and saves them to OutputLinks.txt
Note this only works with the Simplifier website due to prefixing the links with https://simplifier.net, although very easily adapted for any other website.'''

"""


from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


'''retrieve all links within the page, including the banner, and filters to remove href="#" or external links and returning a list of valid links'''
def ListOfLinks(url):
    soup = RequestData(url)
    websites = []
    for link in soup.find_all('a'):
        site = link.get('href')
        if isinstance(site, str) and 'http' not in site and site!='#':
            websites.append(site)
    list_set = set(websites)
    unique_websites = list(list_set)
    return unique_websites

def RequestData(url):
    data  = requests.get(url).text
    soup = BeautifulSoup(data,"html.parser")
    return soup

def OutputLinks(url):
    unique_websites = ListOfLinks(url)
    unique_websites = sorted(unique_websites)
    a = open('OutputLinks.txt', 'w')
    for link in unique_websites:
        linkOutput = "https://simplifier.net"+link
        a.write(linkOutput+ '\n')
    a.close()
    
OutputLinks('https://simplifier.net/guide/uk-core-implementation-guide-stu3-sequence?version=current')