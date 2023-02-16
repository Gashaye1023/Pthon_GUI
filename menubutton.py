from tkinter import*
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

root=Tk()
titlespace= " "
root.title(102*titlespace + "Python GUI")
root.geometry("800x600+100+10")
mb=Menubutton(root, text="Student", relief=RAISED)
mb.grid()
#creat object menu
mb.menu= Menu (mb, tearoff=0)
mb["menu"]=mb.menu
#declar variable mvar 1 and mbar2
mvar1=IntVar()
mvar2=IntVar()
#add variable into menue
mb.menu.add_checkbutton(label="Gadissa",variable=mvar1)
mb.menu.add_checkbutton(label="Gashaye",variable=mvar2)

mb.pack()
root.mainloop()