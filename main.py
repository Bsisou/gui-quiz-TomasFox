from tkinter import *

from PIL import Image, ImageTk

class background(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("MAP.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

class startpage(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.background = background(self)
        self.startframe=Frame(app, self.background, padx=100, pady=100)
        self.startframe.grid()
        self.label = Label(self, text="Welcome to the game")
        self.label.pack()

        self.button = Button(self, text="Start", command=self.start)
        self.button.pack()

    def start(self):
        self.background.destroy()
        self.label.destroy()
        self.button.destroy()
        self.new_window = Tk()
        self.app = Game(self.new_window)
        self.app.pack()
        self.new_window.mainloop()


app = Tk()
app.title("Geography quiz")
app.geometry("900x600")
app.configure(background="black")
start=startpage(app)
start.place(x=0, y=0, width=900, height=600)
app.mainloop()