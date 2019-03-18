from tkinter import *

def button_exit():
    exit(0)
root=Tk()

button = Button(root, bg="lilac", text="Exit", command=button_exit)
button.pack()
root.mainloop()