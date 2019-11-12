import tkinter as tk


root = tk.Tk()
# Add elements here
def callback():
    ip = entry1.get()
    print(ip)


text1 = tk.Label(root,text="Enter a Ip Address to pingj")
entry1 = tk.Entry(root)
button1 = tk.Button(root,text="Submit Name",command=callback)
text1.pack()
entry1.pack()
button1.pack()

root.geometry("500x400")
root.title("Ip Ping machine")
root.mainloop()
# Hello Gamers
