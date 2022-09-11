from tkinter import *
root = Tk()
root.title("Buttons")
root.geometry("400x400")
root.resizable(0,0)
def buttonclicked():
    root.config(bg="orange")
    myLabel=Label(root,text="Hello!",font=("Ariel",20,"bold","italic","underline"]),fg="black")
    myLabel.pack(pady=20)

myButton = Button(root,text = "Click Me",font = ("Ariel",20),bg="green",command=buttonclicked)
myButton.pack(pady=20)







root.mainloop()