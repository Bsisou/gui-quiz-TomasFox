from tkinter import *

from PIL import Image, ImageTk
#this is the class for my first page#
class Startpage:
    def __init__(self, app):
    
        self.heading=Label(app, text="Welcome to the quiz",background="#e1d9bb", font=("comfortaa", 40))
        self.heading.place(x=100, y=10)
        self.label_username= Label(app, text="Enter your name: ", background="#e1d9bb", font=("arial", 18))
        self.label_username.place(x=250, y=200)
        self.name=Entry(app)
        self.name.place(x=285, y=245)
        


        

#this is my main window
app = Tk()
app.title("Geography quiz")
app.geometry("750x500")
#this is my background image#
bg = PhotoImage(file="MAP.png")
bglabel=Label(app, image=bg)
bglabel.place(x=0, y=0)
Startpage(app)
app.mainloop()

