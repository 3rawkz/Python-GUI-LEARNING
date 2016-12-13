_author_ = 'Erick'
from tkinter import *

imgdir = "/home/scriptso/PycharmProjects/pytk/pythonspot.com/"
master = Tk()
master.minsize(300, 100)
master.geometry("320x100")


def callback():
    print("click!")


photo = PhotoImage(file="download.png")
b = Button(master, image=photo, text="OK", command=callback, height=50, width=150, compound=LEFT)  # text="OK" added textto buton and compound the position

# b.pack()
b.place(x = 20, y = 20) #changes button position

mainloop()
