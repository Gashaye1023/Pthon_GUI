from tkinter import*
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

root=Tk()
titlespace= " "
root.title(102*titlespace + "Python GUI")
root.geometry("800x600+100+10")


B=tkinter.Button(root,bd=5,text="Name")
B.pack()

C=tkinter.Canvas(root,bg="blue",height=300,width=300)
coord=10,50,300,205
arc=C.create_arc(coord,start=0, extent=156, fill="red")
C.pack()
root.mainloop()
