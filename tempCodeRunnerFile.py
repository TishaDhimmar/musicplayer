from tkinter import *
from tkinter import font
root = Tk()
fonts = list(font.families())
for items in fonts:
    print(items)

root.mainloop()