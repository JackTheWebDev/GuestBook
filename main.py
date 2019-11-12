import tkinter as tk
import os

root = tk.Tk()
# Add elements here
def callback():
    name = entry1.get()
    text2 = tk.Label(root,text=name)
    text2.pack()

def load():
    f = open("names.txt","r")
    contents = f.read()
    text2 = tk.Label(root,text=contents)
    text2.pack()
    f.close()
def save():
    f = open("names.txt","a")
    name = entry1.get()
    writeme = name+"\n"
    f.write(writeme)

text1 = tk.Label(root,text="Please Enter your name.")
entry1 = tk.Entry(root)
button1 = tk.Button(root,text="Submit Name",command=callback)
button2 = tk.Button(root,text="Load Names",command=load)
button3 = tk.Button(root,text="Save Names",command=save)
text1.pack()
entry1.pack()
button1.pack()
button2.pack()
button3.pack()

root.geometry("500x400")
root.title("Guest Book")
root.mainloop()
