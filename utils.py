import os

try:
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    has_tkinter = False
else:
    has_tkinter = True

def select_folder(title=None, initialdir=None):
    if has_tkinter:
        root = tk.Tk()
        root.withdraw()
        folder = filedialog.askdirectory(title=title, initialdir=initialdir)
    else:
        folder = input(f'{title} :\n')

    return os.path.normpath(folder)


def select_file(title=None, initialdir=None, filetypes=None):
    if has_tkinter:
        root = tk.Tk()
        root.withdraw()
        file = filedialog.askopenfilename(
            title=title, initialdir=initialdir, filetypes=filetypes)
    else:
        file = input(f'{title} :\n')

    return os.path.normpath(file)
