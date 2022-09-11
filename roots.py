#import tkinter
from tkinter import *


#define root
root = Tk()


#root properties
#root title
root.title("Hello world")
#root window size
root.geometry("400x400")
root.config(bg="white")
root.resizable(0,0)







#Labels
myLabel1 = Label(root,text="This is Label 1",bg="green",fg="orange",relief="raised")
myLabel1.pack()
myLabel2 = Label(root,text="This is Label 2",bg="green",fg="orange",relief="ridge")
myLabel2.pack()

