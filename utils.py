import os
import tkinter as tk
from tkinter import filedialog

def select_folder(title=None, initialdir=None):
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title=title, initialdir=initialdir)
    return os.path.normpath(folder)


def select_file(title=None, initialdir=None, filetypes=None):
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename(
        title=title, initialdir=initialdir, filetypes=filetypes)
    return os.path.normpath(file)
