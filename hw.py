from tkinter import *

def button_exit():
    exit(0)

def button_hello():
    print("Hello!")

def button_help():
    print("Click green button to print 'Hello!'\nClick red button to exit\n")
root=Tk()

button1 = Button(root, bg="red", width=15, height=5, command=button_exit)
button2 = Button(root, bg="green", width=15, height=5, command=button_hello)
button3 = Button(root, bg="silver", text="Help", width=35, height=5, fg="dark blue", command=button_help)
button3.pack(side="top")
button1.pack(side="left")
button2.pack(side="right")
root.mainloop()