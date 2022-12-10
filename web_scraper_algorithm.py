from bs4 import BeautifulSoup
import requests 
import os 
from collections import defaultdict 

# Unlimited arguments can be passed into this function, following this format (keyword=category_name)
# Note: Category_name will be the folder which the images will be inserted into 


def print_hello_world():
    print('hello world')

def add_to_unique_list(website, unique_websites): 
    if website not in unique_websites: 
        unique_websites.append(website)

def remove_url_prefix(url):  
    if url.startswith("/url?q="): 
        url = url[7:] 
    return url

def find_websites_from_keyword(unique_websites, *args): 
    #Args as a string
    for word in args:
        url = 'https://www.google.com/search?q=' + word + '&source=lnms&tbm=isch'
        page = requests.get(url) 
        soup = BeautifulSoup(page.content, 'html.parser') 
        for i in soup.find_all('a'): 
            link = i['href']
            mainPart = link.split("&")[0]
            mainPart = remove_url_prefix(mainPart)
            add_to_unique_list(mainPart, unique_websites)
        
def filter_by_domain(domain, unique_websites): 
    domain_websites = []
    for website in unique_websites: 
        if website.startswith(f"https://{domain}"): 
            domain_websites.append(website)
    
    return domain_websites
