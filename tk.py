from subprocess import call
from Tkinter import *
from math import *
def evaluate(event):
	call(["python", "filergui.py", "7894", "3", entry.get()])
    

w = Tk()
Label(w, text="Enter your (IP address):(portnumber)").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()
