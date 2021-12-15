from tkinter import *
import tkinter.messagebox
from PIL import Image
from random import randint

# I want to program a guessing game basing on the image of the flags from different countries.
#There are 6 countries which I picked. The user will have maximum 3 turns, if they are wrong 3 times, the game will be end
#The user cannot move to the next image until they guess correct the current image right.

#create the function instruction
def instruction():
    tkinter.messagebox.showinfo('Welcome To the Flag Guessing Game',
                                'You have 3 attempts to play this game '
                                'There are 6 countries in this game '
                                'you can answer AU for Australia,  JP for Japan , '
                                'NO for Norway,'
                                ' NRA for Nigeria, '
                                'NL for Netherland, '
                                'UK for United Kingdom'
                                )


#create the function for show the picture on frame
def image_start():
    first_image = Label(frame1, image=Image1)
    first_image.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')

def image_two():
    second_image = Label(frame1, image=Image2)
    second_image.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')

def image_three():
    second_image = Label(frame1, image=Image3)
    second_image.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')

def image_forth():
    second_image = Label(frame1, image=Image4)
    second_image.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')

def image_fifth():
    second_image = Label(frame1, image=Image5)
    second_image.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')

def image_sixth():
    second_image = Label(frame1, image=Image6)
    second_image.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.6, anchor='n')

def guessright():
    tkinter.messagebox.showinfo('Answer', 'Congratulation, you got it!')

def guesswrong():
    tkinter.messagebox.showinfo('Answer', 'You are wrong')
turns = 3

#Create the function for button and check the entry,
def flag_check(entry):
    # create the global variable turns
    global turns,n
    if turns>0:

        if n==1:
            if entry == "AU":
                guessright()
                image_two()
                n+=1

            else:
                guesswrong()
                turns -= 1
        elif n==2:
            if entry == "JP":
                guessright()
                image_three()
                n+=1

            else:
                guesswrong()
                turns -= 1
        elif n==3:
            if entry == 'Netherlands' or entry == 'NL':
                guessright()
                image_forth()
                n+=1

            else:
                guesswrong()
                turns -= 1
        elif n==4:
            if entry == 'Nigeria' or entry == 'NRA':
                guessright()
                image_fifth()
                n+=1

            else:
                guesswrong()
                turns -= 1
        elif n==5:
            if entry == 'United Kingdom' or entry == 'UK':
                guessright()
                image_sixth()
                n+=1

            else:
                guesswrong()
                turns -= 1
        elif n==6:
            if entry == 'Norway' or entry == 'NO':
                guessright()
            else:
                guesswrong()
                turns -= 1
    else:
        tkinter.messagebox.showerror("Finished","You have no more turn")
    entry_user.delete(0,END)


n=1
#create the root windows
root = Tk()
width = 1000
height = 800


Image1 = PhotoImage(file='Australia.png')
Image2 = PhotoImage(file='Japan.png')
Image3 = PhotoImage(file='Netherlands.png')
Image4 = PhotoImage(file='Nigeria.png')
Image5 = PhotoImage(file='UK.png')
Image6 = PhotoImage(file='Norway.png')

#create the canvas with the height and width we want, here I use 1000 and 800 which stored in the variable above
canvas = Canvas(root, height = height, width = width)
canvas.pack()

#create the background of the game by using PhotoImage
background = PhotoImage(file='USA.png')
label_background = Label(root, image=background)
label_background.place(relwidth=1, relheight=1)

#create the frame on the top which content the question and instruction for game
frame1 = Frame(root, bg='#0a202b', bd=10)
frame1.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.7, anchor='n')
label = Label(frame1)
label.place(relwidth=1, relheight=1)


#create the button and entry in frame2 for user can submit the answer
frame2 = Frame(root, bg='#0a202b', bd=10)
frame2.place(relx=0.5, rely=0.8, relwidth=0.85, relheight=0.15, anchor='n')
entry_user = Entry(frame2, font=40)
entry_user.place(relwidth=0.6, relheight=1)

button = Button(frame2, text="Submit", font=12, bg = 'grey', command=lambda: flag_check(entry_user.get()))
button.place(relx=0.65, relwidth=0.35, relheight=1)

image_start()

title = Label(root, text="Welcome To the Flag Guessing Game", font=120, bg= 'white')
title.place(relx=0.5, rely=0.1, relwidth=0.6, relheight=0.05, anchor='n')

#info = Button(root, text="Welcome To the Flag Guessing Game", font=100, command=instruction)

info = Button(root, text="Click here for instruction", font=100,bg = 'grey', command=instruction)
info.place(relx=0.5, rely=0.65, relwidth=0.2, relheight=0.05, anchor='n')

textbox = Label(frame2, text="Your answer: ", font=100,bg = 'white')
textbox .place(relx=0.02, rely = 0.03, relwidth=0.3, relheight=0.2)

#call the first image show on frame1


root.mainloop()
