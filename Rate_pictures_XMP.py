# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:57:36 2023

@author: paulg
"""

import numpy as np

import os 
import PIL
# from PIL import Image

import glob

from tkinter import *
from PIL import ImageTk, Image


import pyexiv2 as pyex





# FUNCTION GO DEFINITION

def go(img_no_rated, img_no, rating):

    global label


    
    if rating != []:

        remove_unused_exif_and_xmp(image_names[img_no_rated])
        pyex_img = pyex.Image(image_names[img_no_rated])
        tags=pyex_img.read_xmp()
        dict1={'Xmp.xmp.Rating':rating}
    
        pyex_img.modify_xmp(dict1)
        tags=pyex_img.read_xmp()

        pyex_img.close()

            
    # DISPLAY THE CURRENT IMAGE 
    label.place_forget()
    # top.pack_forget()

    try: 
        label_next.place_forget()
        label_previous.place_forget()
    except: 
        pass


    if img_no==-10:
        img_no = find_next_no_rating(img_no_rated)
    if img_no==-20:
        img_no = find_previous_no_rating(img_no_rated)
    if img_no==len(image_names):
        img_no = 0
    if img_no==-1:
        img_no = len(image_names)-1

    display_image(img_no)
    display_buttons(img_no)


    def right_arrow_pressed(event):
        go(img_no, img_no+1, [])
    root.bind('<Right>', right_arrow_pressed)

    def left_arrow_pressed(event):
        go(img_no, img_no-1, [])
    root.bind('<Left>', left_arrow_pressed)
    
    def one_pressed(event):
        go(img_no, img_no+1, 1)
    root.bind('1', one_pressed)

    def two_pressed(event):
        go(img_no, img_no+1, 2)
    root.bind('2', two_pressed)

    def three_pressed(event):
        go(img_no, img_no+1, 3)
    root.bind('3', three_pressed)

    def four_pressed(event):
        go(img_no, img_no+1, 4)
    root.bind('4', four_pressed)

    def five_pressed(event):
        go(img_no, img_no+1, 5)
    root.bind('5', five_pressed)

    


def display_buttons(img_no):
    global button_back_back
    global button_back
    global top


    pyex_img = pyex.Image(image_names[img_no])

    tags=pyex_img.read_xmp()



    button_forward_forward = Button(root, text=">>", width=9, height=2,bg='lightgrey',
            command=lambda: go(img_no, -10, []))

    button_back_back = Button(root, text="<<", width=9, height=2,bg='lightgrey',
            command=lambda: go(img_no, -20, []))


    button_back = Button(root, text="<", width=10, height=2,bg='lightgrey',
                        command=lambda: go(img_no, img_no-1, []))
    
    button_forward = Button(root, text=">",width=10, height=2,bg='lightgrey',
            command=lambda: go(img_no, img_no+1, []))
    

    button_one = Button(root, text="x", width=9, height=2,bg='lightgrey',
            command=lambda: go(img_no, img_no+1,1))

    button_two = Button(root, text="xx",width=9, height=2,bg='lightgrey',
            command=lambda: go(img_no, img_no+1,2))

    button_three = Button(root, text="xxx",width=9, height=2,bg='lightgrey',
            command=lambda: go(img_no, img_no+1,3))

    button_four = Button(root, text="xxxx", width=9, height=2,bg='lightgrey',
            command=lambda: go(img_no, img_no+1,4))

    button_five = Button(root, text="xxxxx",width=9, height=2,bg='lightgrey',
            command=lambda: go(img_no, img_no+1,5))

    if 'Xmp.xmp.Rating' in tags.keys():
        
        if int(tags['Xmp.xmp.Rating'])==1:
            button_one = Button(root, text="x", width=9, height=2, bg='lightblue',
                command=lambda: go(img_no, img_no+1,1))
            
        if int(tags['Xmp.xmp.Rating'])==2:
            button_two = Button(root, text="xx",width=9, height=2, bg='lightblue',
                command=lambda: go(img_no, img_no+1,2))
            
        if int(tags['Xmp.xmp.Rating'])==3:
            button_three = Button(root, text="xxx",width=9, height=2, bg='lightblue',
                command=lambda: go(img_no, img_no+1,3))
            
        if int(tags['Xmp.xmp.Rating'])==4:
            button_four = Button(root, text="xxxx", width=9, height=2, bg='lightblue',
                command=lambda: go(img_no, img_no+1,4))
    
        if int(tags['Xmp.xmp.Rating'])==5:
            button_five = Button(root, text="xxxxx",width=9, height=2, bg='lightblue',
                command=lambda: go(img_no, img_no+1,5))
    
    
    # # grid function is for placing the buttons in the frame
#     button_back_back.grid(row=0, column=0, padx = 20)
#     button_back.grid(row=0, column=1, padx = 20)
#     button_one.grid(row=0, column=2)
#     button_two.grid(row=0, column=3)
#     button_three.grid(row=0, column=4)
#     button_four.grid(row=0, column=5)
#     button_five.grid(row=0, column=6)
#     button_forward.grid(row=0, column=7, padx = 20)
#     button_forward_forward.grid(row=0, column=8, padx = 20)
    
#     textframe = Frame(root)
#     textframe.grid(in_=root, row=1, column=0, columnspan=3, sticky=NSEW)
#     root.columnconfigure(0, weight=1)
#     root.rowconfigure(1, weight=1)
    button_back_back.place(relx=0.28, rely=0.05, anchor=CENTER)
    button_back.place(relx=0.34, rely=0.05, anchor=CENTER)
    button_one.place(relx=0.4, rely=0.05, anchor=CENTER)
    button_two.place(relx=0.45, rely=0.05, anchor=CENTER)
    button_three.place(relx=0.5, rely=0.05, anchor=CENTER)
    button_four.place(relx=0.55, rely=0.05, anchor=CENTER)
    button_five.place(relx=0.6, rely=0.05, anchor=CENTER)
    button_forward.place(relx=0.66, rely=0.05, anchor=CENTER)
    button_forward_forward.place(relx=0.72, rely=0.05, anchor=CENTER)
    

    
def display_image(img_no):
    global label
    global label_next
    global label_previous
    global want_thumbnails

    
    PIL_image = Image.open(image_names[img_no])

    h_pix = 700
    small_image = PIL_image.resize((int(h_pix/PIL_image.size[1] * PIL_image.size[0]), int(h_pix)))

    tk_img = ImageTk.PhotoImage(small_image)
    label = Label(image=tk_img, borderwidth=0, highlightthickness=0)
    label.place(relx=.5, rely=.5,anchor= CENTER)
    label.image = tk_img
    root.title("img_no=%d/%d -- " %(img_no+1,len(image_names)) + image_names[img_no])
    
    
    
    ### option to have thumbnails of previous and next images on the side

    if want_thumbnails: 
        if img_no == len(image_names)-1:
            PIL_image = Image.open(image_names[0])
        else:
            PIL_image = Image.open(image_names[img_no+1])
    
        w_pix = 250
        small_image = PIL_image.resize((int(w_pix), int(w_pix/PIL_image.size[0] * PIL_image.size[1])), resample=Image.Resampling.LANCZOS, reducing_gap=1)
    
        tk_img_next = ImageTk.PhotoImage(small_image)
        label_next = Label(image=tk_img_next)
        label_next.place(relx=.9, rely=.7,anchor= CENTER)
        label_next.image = tk_img_next
        
    
        PIL_image = Image.open(image_names[img_no-1])
    
        small_image = PIL_image.resize((int(w_pix), int(w_pix/PIL_image.size[0] * PIL_image.size[1])), resample=Image.Resampling.LANCZOS, reducing_gap=1)    
        
        tk_img_previous = ImageTk.PhotoImage(small_image)
        label_previous = Label(image=tk_img_previous)
        label_previous.place(relx=.1, rely=.7,anchor= CENTER)
        label_previous.image = tk_img_previous


    
    
    
def find_next_no_rating(img_no):
    for i in np.arange(img_no,len(image_names)):
        pyex_img = pyex.Image(image_names[i])
        if 'Xmp.xmp.Rating' in pyex_img.read_xmp(): 
            continue
        else:
            img_no_next_no_rating = i
            break  
            
    return img_no_next_no_rating

def find_previous_no_rating(img_no):
    img_no_previous_no_rating=[]
    for i in np.flip(np.arange(0,img_no)):
        pyex_img = pyex.Image(image_names[i])
        if 'Xmp.xmp.Rating' in pyex_img.read_xmp(): 
            img_no_previous_no_rating = i+1
            break
        else:
            continue
    return img_no_previous_no_rating


def remove_unused_exif_and_xmp(image_name):
# image_name=image_names[0]
    # print(image_name)
    pyex_img = pyex.Image(image_name)
    
    exif_data=pyex_img.read_exif()
    # exist_rating_percent = False
    a=0
    b=0
    if "Exif.Image.RatingPercent" in exif_data:
        # exist_rating_percent = True
        #rating_percent = int(exif_data['Exif.Image.RatingPercent'])
        del exif_data['Exif.Image.RatingPercent']
        a=1
        # print('Deleted exif rating percent')

    
    if "Exif.Image.Rating" in exif_data:
        del exif_data['Exif.Image.Rating']
        # print('Deleted exif rating')
        b=1


    
    if a+b>0: #to avoid writing stuff if nothing has changed
        pyex_img.clear_exif()
        pyex_img.modify_exif(exif_data)
    # exif_data=pyex_img.read_exif()

    #xmp
    tags=pyex_img.read_xmp()
    
    # print(tags)
    c=0 
    if "Xmp.MicrosoftPhoto.Rating" in tags:
        print('hello')
        del tags['Xmp.MicrosoftPhoto.Rating']
        c=1
        # print('Deleted MicrosoftPhoto rating')
    
    if c>0:  #to avoid writing stuff if nothing has changed
        pyex_img.clear_xmp()
        pyex_img.modify_xmp(tags)
    
    
    pyex_img.close()



# importing the tkinter module and PIL that
# is pillow module

want_thumbnails = False
x=input('Do you want thumbnails (cooler but more time consuming)?\n')
if x in ['y','Y', 'Yes', 'yes', 'YES']: 
    want_thumbnails=True

user_input_dir=input('Input the directory where the picture are located\n')
os.chdir(user_input_dir)

# Calling the Tk (The initial constructor of tkinter)
root = Tk()

root.configure(bg="white")

# We will make the title of our app as Image Viewer - will change later
root.title("Image Viewer")

# Setting geometry to size of the current screen
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))


#finding all the jpgs in the current folder
image_names = glob.glob('*.jpg') + glob.glob('*.jpeg') + glob.glob('tests/*.JPG')

#sorting jpgs based on creation time
image_names.sort(key=os.path.getctime)

#initialization at 0th image (first image of the list)
img_no = 0


display_image(img_no)

display_buttons(img_no)


def right_arrow_pressed(event):
    go(img_no, img_no+1, [])
root.bind('<Right>', right_arrow_pressed)

def left_arrow_pressed(event):
    go(img_no, img_no-1, [])
root.bind('<Left>', left_arrow_pressed)

def one_pressed(event):
    go(img_no, img_no+1, 1)
root.bind('1', one_pressed)

def two_pressed(event):
    go(img_no, img_no+1, 2)
root.bind('2', two_pressed)

def three_pressed(event):
    go(img_no, img_no+1, 3)
root.bind('3', three_pressed)

def four_pressed(event):
    go(img_no, img_no+1, 4)
root.bind('4', four_pressed)

def five_pressed(event):
    go(img_no, img_no+1, 5)
root.bind('5', five_pressed)


root.mainloop()