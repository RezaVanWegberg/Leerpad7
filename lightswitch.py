import tkinter as tk
from turtle import bgcolor
window = tk.Tk()

def buttonFunction():
    if window['bg']=="black":
        window.config(bg="yellow")
        button.config(text="Switch light off")   
        print("light on")
    else:
        window.config(bg="black")
        button.config(text="Switch light on")
        print("light off")

button = tk.Button(text='click', bg="white", fg="black", command=buttonFunction)
button.pack(pady = 20, padx = 20)

window.mainloop()