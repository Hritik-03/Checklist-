
from tkinter import *
root = Tk()
root.title("Buttons")
root.geometry("400x400")
root.resizable(0,0)
def sayHi():
    myLabel=Label(root,text="Hi"+ myInput.get())
    myLabel.pack()

myInput= Entry(root,width=50,font=("Ariel",10))
myInput.pack(pady=20)
myButton=Button(root,text="Click Me!",command=sayHi)
myButton.pack(pady=20)