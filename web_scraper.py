# Web scraper for getting and filtering websites from web
from tkinter import *
from web_scraper_algorithm import *
from bs4 import BeautifulSoup
import requests 
import os 
from collections import defaultdict 

unique_websites = []

#find_websites_from_keyword(unique_websites, "python_keywords")

print(unique_websites)

root = Tk()
mainframe = Frame(root)
pixel_font_large = ('Small Fonts', 50)
pixel_font_small = ('Small Fonts', 25)

titleLabel = Label(mainframe, text = 'Website Finder', font = pixel_font_large)
creatorsLabel = Label(mainframe, text = 'Gary, Rayan, Lawrence, Rohan', font = pixel_font_small)
v = Scrollbar(root, orient='vertical')
#v.config(command=t.yview)

user_choice = Label(mainframe, text= "How much ")


user_amount = IntVar()
site_numbers = Scale(mainframe, from_=1, to=10, orient=HORIZONTAL, variable=user_amount, font=pixel_font_small)



#Gridding the widgets
root.minsize(450, 400)
mainframe.grid(padx = 50, pady = 50)
titleLabel.grid(row=2, column=1, columnspan=2)
creatorsLabel.grid(row=2, column=1, columnspan=2)
site_numbers.grid(row=4, column=1, columnspan=2)
v.grid(row=1, column=1, rowspan = 3)

root.mainloop()
