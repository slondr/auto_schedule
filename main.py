import sys
if sys.version_info < (3, 0):
    # Python 2
    from Tkinter import *
else:
    # Python 3
    from tkinter import *

import pyautogui
import time


def type_courses(courses):
    courses = courses.split(",")

    time.sleep(5)

    for c in courses:
        pyautogui.typewrite(c)
        pyautogui.typewrite(["tab"])

    pyautogui.typewrite(["enter"])



def show_entry_fields():
   print(e1.get())
   type_courses(e1.get())


master = Tk()

Label(master, text="Enter call numbers comma seperated (no sapces)").pack()

e1 = Entry(master)
e1.pack()

Button(master, text='GO', command=show_entry_fields).pack()

Label(master, text="Created by Jesse Stevenson (jesse-stevenson.com)").pack()

mainloop()