from tkinter import*
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

root=Tk()
titlespace= " "
root.title(102*titlespace + "Python GUI")
root.geometry("800x600+100+10")

#creat lable
lab=Label(root, text="Student Name",fg="Blue", font=34)
lab.pack(side=LEFT)
#creat entry
ent=Entry(root, bd=5)
ent.pack(side=RIGHT)
var1=StringVar() #DECLAR VARIABLE VAR1
lable=Label(root, textvariable=var1,relief=RAISED)
var1.set("Student ID")#set value for variable var1
lable.pack()


root.mainloop()