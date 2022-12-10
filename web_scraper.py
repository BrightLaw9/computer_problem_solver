# Web scraper for getting and filtering websites from web
from tkinter import *
from web_scraper_algorithm import *
from bs4 import BeautifulSoup
#import requests 

menu = 0

unique_websites = []
def generate_sites():
    user_keyword = 
    find_websites_from_keyword(unique_websites, user_keyword)

def call_filter():
    user_site = site.get() 
    filter_by_domain(user_site, unique_websites)

def call_search():

root = Tk()
mainframe = Frame(root)
pixel_font_large = ('Small Fonts', 50)
pixel_font_small = ('Small Fonts', 25)

titleLabel = Label(mainframe, text = 'Website Finder', font = pixel_font_large)
creatorsLabel = Label(mainframe, text = 'Gary, Rayan, Lawrence, Rohan', font = pixel_font_small)
v = Scrollbar(root, orient='vertical')
#v.config(command=t.yview)

user_choice = Label(mainframe, text= "How many websites would you like us to search?", font=pixel_font_small)
start_search = Button(mainframe, text='START', command = call_search)

user_amount = IntVar()
site_numbers = Scale(mainframe, from_=1, to=10, orient=HORIZONTAL, variable=user_amount, font=pixel_font_small)

site_question = Label(mainframe, text="Which site would you want to look at?")

site = StringVar()
site_entry = Entry(mainframe, textvariable=site)

generate_list_button = Button(mainframe, text="Generate Sites", command = generate_sites)

#Gridding the widgets
root.minsize(450, 400)
mainframe.grid(padx = 50, pady = 50)

if menu == 0:
    titleLabel.grid(row=1, column=1, columnspan=2)
    creatorsLabel.grid(row=2, column=1, columnspan=2)

if menu == 1:
user_choice.grid(row=3, column=1, columnspan=2)
site_numbers.grid(row=4, column=1, columnspan=2)
v.grid(row=1, column=1, rowspan = 3)

root.mainloop()
