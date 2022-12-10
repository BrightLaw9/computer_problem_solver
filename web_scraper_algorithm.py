from bs4 import BeautifulSoup
import requests 
import random

def print_hello_world():
    print('hello world')

def add_to_unique_list(website, unique_websites): 
    if website not in unique_websites: 
        unique_websites.append(website)

def remove_url_prefix(url):  
    if url.startswith("/url?q="): 
        url = url[7:] 
    return url

def find_websites_from_keyword(keyword): 
    #Args as a string
    unique_websites = []
   
    url = 'https://www.google.com/search?q=' + keyword + '&source=lnms&tbm=isch'
    page = requests.get(url) 
    soup = BeautifulSoup(page.content, 'html.parser') 
    for i in soup.find_all('a'): 
        link = i['href']
        mainPart = link.split("&")[0]
        mainPart = remove_url_prefix(mainPart)
        add_to_unique_list(mainPart, unique_websites)
    return unique_websites
        
def filter_by_domain(unique_websites): 
    domain_websites = []
    for website in unique_websites: 
        if ".org" in website or ".edu" in website or "w3schools" in website \
        or "codecademy" in website or "stackoverflow" in website and "wiki" not in website: 
            domain_websites.append(website)
    return domain_websites

def filter_quantity_of_websites(quantity, unique_websites): 
    websites_in_quantity = []
    selected_idxes = []

    if len(unique_websites) == 0: 
        return ["No websites found"]

    if len(unique_websites) <= quantity: 
        return unique_websites 
    
    for i in range(quantity): 
        selected_idx = random.randint(0, len(unique_websites)-1)
        selected_idxes.append(selected_idx)
        while selected_idx in selected_idxes: 
            # Reselect index if all ready selected before, until it is unique
           selected_idx = random.randint(0, len(unique_websites)-1) 

        #Get the website corresponding to the index 
        website = unique_websites[selected_idx]
        websites_in_quantity.append(website)
    
    return websites_in_quantity
    
        