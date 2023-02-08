import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


def create_widgets():
    source_label = Label(root, text="Files to copy: ")
    source_label.grid(row=1, column=0, padx=10, pady=10)

    root.sourceText = Entry(root, width=50, textvariable=sourceLocation)
    root.sourceText.grid(row=1, column=1, padx=10, pady=10, columnspan=1)

    source_button = Button(root, text="Browse ", command=source_browse, width=15)
    source_button.grid(row=1, column=2, padx=10, pady=10, columnspan=3)


def source_browse():
    root.files_list = list(filedialog.askdirectory(initialdir="C:/", mustexist=True))
    root.sourceText.insert('1', root.files_list)


# main window
root = tk.Tk()
root.minsize(800, 500)
# root.geometry("800x500")
# root.resizable(False, False)
root.title("CopyMoveGUI")

# tkinter vars for locations
sourceLocation = StringVar()
destLocation = StringVar()

create_widgets()

root.mainloop()
