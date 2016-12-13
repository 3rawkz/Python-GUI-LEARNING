_author_ = 'Erick'
from tkinter import *
##########
# PART 1 #
#############
# root = Tk()
# mainloop()
#############
# PART 2.1 #
# root = Tk()
# root.title('MY PROG')
# root.geometry('600x500')
#
# mainloop()
root = Tk()
def window(main):
    main.title('MY PROG')
    main.update_idletasks()
    width = main.winfo_width()
    height = main.winfo_height()
    x = (main.winfo_screenmmwidth() // 2 ) - (width // 2)
    y = (main.winfo_screenheight() // 2 ) - (height // 2)

    main.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window(root)
mainloop()