from tkinter import*
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

root=Tk()
titlespace= " "
root.title(102*titlespace + "Python GUI")
root.geometry("800x600+100+10")

#creat checkbutton
CB=Checkbutton(root,text = "Animal")
CB1=Checkbutton(root,text = "Human")
CB.pack()
CB1.pack()
root.mainloop()