from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    top.configure(bg = "blue")
    l2 = Label(top, text = "this is a toplevel window")
    
    top.mainloop()

l = Label(root, text = "this is root window")
btn = Button(root, text = "click here to open another window", command = topwin)

l.pack()
btn.pack()
root.mainloop()