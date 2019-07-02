#Simple text editor
from tkinter import *
from tkinter import filedialog

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close

def saveAs():

    t = text.get(0.0, END)
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()
    try:
        f.write(t.rstrip())
    except:
        showerror(title = "Error", message = "Unable to save file...")

def openFile():
    f = askopenfile(mode = 'r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)



root=Tk("Python Notepad")
root.title("Python Notepad")
root.minsize(width = 300, height = 400)
root.maxsize(width = 1000, height = 1000)

text=Text(root)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open...", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)

filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
