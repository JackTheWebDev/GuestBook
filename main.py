import tkinter as tk


root = tk.Tk()
# Add elements here
def callback():
    name = entry1.get()
    text2 = tk.Label(root,text=name)
    text2.pack()


text1 = tk.Label(root,text="Please Enter your name.")
entry1 = tk.Entry(root)
button1 = tk.Button(root,text="Submit Name",command=callback)
text1.pack()
entry1.pack()
button1.pack()

root.geometry("500x400")
root.title("Ip Ping machine")
root.mainloop()
