from tkinter import *

root=Tk()
bg = PhotoImage(file="MAP.png")
bglabel=Label(root, image=bg)
bglabel.place(x=0, y=0)
root.title("geography quiz")
root.geometry( "750x500" )
root.mainloop()