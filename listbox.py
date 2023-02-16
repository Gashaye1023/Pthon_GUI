from tkinter import*
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

root=Tk()
titlespace= " "
root.title(102*titlespace + "Python GUI")
root.geometry("800x600+100+10")
lab1=Label(root,text="List of computer programing")
lab1.pack()
lb=Listbox(root)
lb.insert(1,"Python")
lb.insert(2,"Java ")
lb.insert(3,"C++")
lb.insert(4,"C# ")
lb.insert(5,"PHP")

lb.pack()


root.mainloop()