from tkinter import *
root = Tk()
root.title("Menus")
root.geometry("400x400")
def new():
    pass
def cut():
    pass
def copy():
    pass
def paste():
    pass


#menu bar
mainMenu=Menu(root)
root.config(menu=mainMenu)


#create sub menus
#file menu
fileMenu=Menu(mainMenu,tearoff=0)
mainMenu.add_cascade(label="File",menu=fileMenu)

#Edit menu
editMenu=Menu(mainMenu,tearoff=0)
mainMenu.add_cascade(label="edit",menu=editMenu)

#adding file commands
fileMenu.add_command(label="New",command=new)
fileMenu.add_command(label="Exit",command=root.destroy)

#adding edit commands
editMenu.add_command(label="cut",command=cut)
editMenu.add_command(label="copy",command=copy)
editMenu.add_command(label="paste",command=paste)