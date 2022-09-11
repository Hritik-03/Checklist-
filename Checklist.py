from tkinter import *
root = Tk()


# root properties
root.title("My Checklist App")
root.geometry("500x500")
root.resizable(0,0)



# setting up general fonts and colours
myFont = ("Times New Roman",12)
rootColour = "#3b5998"
buttonColour = "#f7f7f7"
root.config(bg=rootColour)

def addItem():
    if listEntry.get() == "":
        messagebox.showinfo("Illegal Entry in the List","Cannot enter blank items in list box")
    else:
     listBox.insert(END,listEntry.get())
     listEntry.delete(0,END)
def removeItem():
    listBox.delete(ANCHOR)

def clearList():
    listBox.delete(0,END)

def saveList():
    #we will open a file (in write mode)and write required contents into it
    #with checklist.txt opened in write mode named as f for your future refrences
    with open("checklist.txt","w") as f:
        
        listTuple = listBox.get(0,END)
        
        for items in listTuple:
            f.write(items+"\n")
            
   #functions to recall stored elements in text file
def openList():
        try:
             with open("checklist.txt","r") as f:
                 for line in f:
                     listBox.insert(END,line)
        except:
             pass
        
        

#creating layout of the app
#create frames
inputFrame = Frame(root,bg=rootColour)
outputFrame = Frame(root,bg=rootColour)
buttonsFrame = Frame(root,bg=rootColour)
inputFrame.pack()
outputFrame.pack()
buttonsFrame.pack()

#create layout of elements in input frame - entry widget,add item button
listEntry = Entry(inputFrame,width = 30,borderwidth = 3,font=myFont)
listAddButton = Button(inputFrame,text="Add Item",borderwidth=2,font=myFont,bg=buttonColour,command=addItem)
listEntry.grid(row=0,column=0,padx=5,pady=5)
listAddButton.grid(row=0,column=1,padx=5,pady=5)

#create layout of elements in output frame = listbox and scrolbar
scrollBar = Scrollbar(outputFrame)
listBox = Listbox(outputFrame,height=15,width=35,borderwidth=3,font=myFont,yscrollcommand=scrollBar.set)
scrollBar.config(command=listBox.yview)
listBox.grid(row=0,column=0)
scrollBar.grid(row=0,column=1,sticky="NS")

#create layout of elements in button frame-list remove,list clear,save,quit
listRemoveButton = Button(buttonsFrame,text="Remove Item",borderwidth=2,font=myFont,bg=buttonColour,command=removeItem)
listClearButton = Button(buttonsFrame,text="Clear List",borderwidth=2,font=myFont,bg=buttonColour,command=clearList)
saveButton = Button(buttonsFrame,text="Save",borderwidth=2,font=myFont,bg=buttonColour,command=saveList)
quitButton = Button(buttonsFrame,text="Exit",borderwidth=2,font=myFont,bg=buttonColour,command=root.destroy)
listRemoveButton.grid(row=0,column=0,padx=2,pady=10)
listClearButton.grid(row=0,column=1,padx=2,pady=10,ipadx=7)
saveButton.grid(row=0,column=2,padx=2,pady=10,ipadx=17)
quitButton.grid(row=0,column=3,padx=2,pady=10,ipadx=17)




#main loop
openList()
root.mainloop()

