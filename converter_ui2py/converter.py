import os
from tkinter import *
from tkinter import filedialog

def convert():
    name_of_converted = "design.py"
    current_dir = os.getcwd()

    filepath = filedialog.askopenfilename(initialdir=current_dir, title="Choose an ui file", filetypes=(("ui files","*.ui"), ("all files","*.*")))

    os.system(f'pyuic5 -x {filepath} -o {current_dir}/{name_of_converted}')

    print("The file was generated")
    win.quit()

if __name__ == "__main__":

    win=Tk()
    win.geometry("400x300")

    Label(win, text="Choose the ui file to convert", font='Arial 16 bold').pack(pady=15)

    button = Button(win, text="Choose file", command=convert)
    button.pack()

    win.mainloop()
