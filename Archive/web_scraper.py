# Web scraper for getting and filtering websites from web
from tkinter import *
from web_scraper_algorithm import *
from bs4 import BeautifulSoup
#import requests 


global value, unique_websites, first_time
value = 1
first_time = True

def go_back():
    global value
    value -= 1
    if value == 2:
        call_search()
    elif value == 1:
        title_menu()

def destroy_menu1():
    titleLabel.destroy()
    creatorsLabel.destroy()
    start_search.destroy()

def destroy_menu2():
    user_choice.destroy()
    start_search.destroy()
    site_numbers.destroy()
    keyword_entry.destroy()
    keyword_label.destroy()
    back_button.destroy()

def destroy_menu3():
    site_header.destroy()
    site_label.destroy()

def title_menu():
    global first_time
    if first_time == False:
        destroy_menu2()
    first_time = False
    titleLabel.grid(row=1, sticky=NSEW, padx=275)
    creatorsLabel.grid(row=2, sticky=NSEW, padx=275)
    start_search.grid(row=3, sticky=NSEW, padx=275, pady=25)

def convert_website_list_to_string(final_websites): 
    website_display_string = ''
    for website in final_websites: 
        website_display_string += website + "\n"

    return website_display_string    

def generate_sites():
    global unique_websites, value
    final_websites = call_filter()


    #To string for label display
    final_website_string = convert_website_list_to_string(final_websites)

    site_label.config(text=final_website_string)
    
    destroy_menu2()
    site_header.grid(row=1, column=1, sticky=NSEW, padx=25, columnspan=2)
    site_label.grid(row=2, column=1, sticky=NSEW, padx=25)
    back_button.grid(row=2, column=2, sticky=NSEW, padx=25) 

def call_filter():

    #Keyword filter
    user_keyword = keyword.get()
    unique_websites = find_websites_from_keyword(user_keyword)

    #Domain filter
    unique_websites = filter_by_domain(unique_websites)

    #Quantity displayed filter
    num_to_display = list_amount.get()
    final_websites = filter_quantity_of_websites(num_to_display, unique_websites)
    
    return final_websites
    

def call_search():
    # NEW LAYOUT 
    global value

    if value == 1:
        destroy_menu1()
    else:
        destroy_menu3()


    keyword_label.grid(row=1, column=1, sticky=NSEW, padx=225, columnspan=2)
    keyword_entry.grid(row=2, column=1, sticky=NSEW, padx=225, columnspan=2)
    user_choice.grid(row=3, column=1, sticky=NSEW, padx=225, columnspan=2)
    site_numbers.grid(row=4, column=1, sticky=NSEW, padx=225, columnspan=2)
    #site_question.grid(row=5, sticky=NSEW, pady=50)
    generate_list_button.grid(row=5, column=1, pady=20, padx = (110, 0))    
    back_button.grid(row=5, column=2, sticky = W, ipadx = 50)

#     for i in range(1, 6):
#         name = 'button' + str(i)
#         eval(name).grid()   

# def check(value):
#     value != value
#     dark_blue = "#00004D"
#     light_blue = "#5BD1FF"
#     if value:
#         button = 'button' + value
#         eval(button).config(bg = dark_blue, fg = light_blue)
#     else:
#         eval(button).config(bg = light_blue, fg = dark_blue)
        

root = Tk()
mainframe = Frame(root)
bg_purple = "#3a0aba"
root.config(bg = bg_purple)
mainframe.config(bg=bg_purple)
dark_blue = "#00004D"
light_blue = "#5BD1FF"
white = "#EFFFFF"
dark_pink = "#F20082"
bright_pink = "#FF00CB"
black = "#1F201F"

pixel_font_large = ('Terminal', 50)
pixel_font_small = ('Terminal', 25)

titleLabel = Label(mainframe, text = 'Website Finder', font = pixel_font_large, bg=bg_purple, fg=bright_pink)
creatorsLabel = Label(mainframe, text = 'Gary, Rayan, Lawrence, Rohan', font = pixel_font_small, bg=bg_purple, fg=bright_pink)
#v = Scrollbar(root, orient='vertical')
#v.config(command=t.yview)

#Asking the user for the number of sites they want us to find
user_choice = Label(mainframe, text= "How many websites do you want to see?", font=pixel_font_small, bg=bg_purple, fg=bright_pink)
start_search = Button(mainframe, text='START', command = call_search, bg=bg_purple, fg=bright_pink)

list_amount = IntVar()
site_numbers = Scale(mainframe, from_=1, to=10, orient=HORIZONTAL, variable=list_amount, font=pixel_font_small, length = 200, \
                     bg=bg_purple, fg=bright_pink)

#Asking the user for their specific problem
keyword = StringVar()
keyword_label = Label(mainframe, text="Which topic do you want to look for?", font=pixel_font_small, bg=bg_purple, fg=bright_pink) 
keyword_entry = Entry(mainframe, textvariable=keyword, bg=white, fg=bright_pink) 

generate_list_button = Button(mainframe, text="Generate Sites", command = generate_sites, bg=dark_pink, fg=bright_pink)

back_button = Button(mainframe, text="Go Back", command=go_back, bg=dark_pink)

site_header = Label(mainframe, text="Here's the list of websites:")
site_label = Label(mainframe, bg=bg_purple, fg=light_blue)

#Asking the user which site in particular they would want to look at
#site_question = Label(mainframe, text="Check off the sites you would like to see.")

#button_sites = ["W3 Schools", "Stack Overflow", "Codecademy", "Khan Academy", "GeeksForGeeks"]


# b1 = False
# b2 = False
# b3 = False
# b4 = False
# b5 = False

# button1 = Button(mainframe, text = button_sites[0], command = check(b1))  
# button2 = Button(mainframe, text = button_sites[1], command = check(b2))  
# button3 = Button(mainframe, text = button_sites[2], command = check(b3))  
# button4 = Button(mainframe, text = button_sites[3], command = check(b4))  
# button5 = Button(mainframe, text = button_sites[4], command = check(b5))


#Gridding the widgets
root.minsize(1000, 550)
root.maxsize(1000, 550)
mainframe.grid(ipadx = 50, pady = 75)


title_menu()

root.mainloop()

    
    
# v.grid(row=1, column=1, rowspan = 3)