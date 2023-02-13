# -*- coding: utf-8 -*-
""" 
This script checks all the pages within a website for any error messages
"""
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

with open('website.txt', 'r') as file:
    data = file.readline().strip('\n')
    
'''retrieve all links within the page, including the banner, and filters to remove href="#" or external links and returning a list of valid links'''
def ListOfLinks(url):
    soup = RequestData(url)
    websites = []
    print("webpages to check")
    for link in soup.find_all('a'):
        site = link.get('href')
        if isinstance(site, str) and 'http' not in site and site!='#':
            print(site)
            websites.append(site)
    print('\n\n')
    list_set = set(websites)
    unique_websites = list(list_set)
    return unique_websites

''' Interates over ListOfLinks returning any pages that have errors '''
def FindErrors(url):
    websites = ListOfLinks(url)
    for e in websites:
        url_check = 'https://simplifier.net'+ e
        data_check  = requests.get(url_check).text
        soup_check = BeautifulSoup(data_check,"html.parser")
        error = soup_check.find_all('div',{'class':"error"})
        if error:
            print(url_check)
            for err in error:
                print(err)
            print()
    print("Check Complete")
    
def RequestData(url):
    data  = requests.get(url).text
    soup = BeautifulSoup(data,"html.parser")
    return soup

FindErrors(data)
