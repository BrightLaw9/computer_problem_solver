# Web scraper for getting and filtering websites from web
from tkinter import *

root = Tk()
mainframe = Frame(root)
pixel_font_large = ('Small Fonts', 50)
pixel_font_small = ('Small Fonts', 25)

titleLabel = Label(mainframe, text = 'Website Finder', font = pixel_font_large)
creatorsLabel = Label(mainframe, text = 'Gary, Rayan, Lawrence, Rohan', font = pixel_font_small)

user_amount = IntVar()
site_numbers = Scale(mainframe, from_=1, to=10, orient=HORIZONTAL, variable=user_amount, font=pixel_font_small)

#Gridding the widgets
root.minsize(450, 400)
mainframe.grid(padx = 50, pady = 50)
titleLabel.grid(row=1, column=1, columnspan=2)
creatorsLabel.grid(row=2, column=1, columnspan=2)



root.mainloop()

print('hello')