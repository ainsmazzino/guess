from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('3rd eye')
root.geometry("600x400")

def poe():
    os.system("c:/CODING/machinelearning/dist/mos/mos.exe")

but = Button(root, text="3rd eye", command=poe)
but.pack(pady=20)


root.mainloop()
