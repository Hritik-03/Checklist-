from tkinter import *
root = Tk()
root.title("Frames")
root.geometry("500x500")
root.config(bg="white")
root.resizable(0,0)
root.config(bg="#3b5998")


def disable1():
    label1.config(state="disabled")
    label1.config(state="normal")
def disable2():
    label2.config(state="disabled")
    label1.config(state="normal")


#creating frames
labelFrame=Frame(root,width=400,height=200,bg="#3b5998")
buttonFrame=Frame(root,width=400,height=200,bg="#3b5998")
labelFrame.pack(pady=20)
buttonFrame.pack(pady=20)


#create labels
label1=Label(labelFrame,text="This is Label 1",font=("Ariel",40))
label2=Label(labelFrame,text="This is Label 2",font=("Ariel",40))
label1.pack(pady=20)
label2.pack(pady=20)

# create buttons
disable1button = Button(buttonFrame,text="Disable 1",font=("Ariel",20),command=disable1)
disable2button = Button(buttonFrame,text="Disable 1",font=("Ariel",20),command=disable2)
disable1button.grid(row=0,column=0,padx=20)
disable2button.grid(row=0,column=1,padx=20)



