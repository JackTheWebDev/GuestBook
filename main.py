import tkinter as tk
import os

root = tk.Tk()
def load():
    def callback3():
        root3.destroy()
    f = open("names.txt","r")
    contents = f.read()
    text2 = tk.Label(root,text=contents)
    text2.pack()
    f.close()
    root3 = tk.Tk()
    textRoot3 = tk.Label(root3,text="Loaded")
    buttonRoot3 = tk.Button(root3,text="Ok",command=callback3)
    root3.geometry("200x50")
    textRoot3.pack()
    buttonRoot3.pack()
def save():
    def callback2():
        root2.destroy()
    f = open("names.txt","a")
    name = entry1.get()
    writeme = name+"\n"
    f.write(writeme)
    f.close()
    root2 = tk.Tk()
    textRoot2 = tk.Label(root2,text="Saved")
    buttonRoot2 = tk.Button(root2,text="Ok",command=callback2)
    textRoot2.pack()
    buttonRoot2.pack()
    root2.geometry("200x50")
    root2.mainloop()

text1 = tk.Label(root,text="Please Enter your name.")
entry1 = tk.Entry(root)
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
