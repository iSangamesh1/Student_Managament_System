# import tkinter
from tkinter import *

root = Tk()
root.title("Home Page")
root.geometry('1370x760')
root.config(bg='light yellow')
studenttitle = Label(root, text="Student Management System", bg='blue', fg="white", font=("Arial", 30), relief=GROOVE, bd=10)
studenttitle.grid(row=0, column=0, columnspan=2, sticky=N, pady=40)
page2frame = Frame(root, bg='light yellow', cursor='star')
studentpro = Label(root, text="Student Profile", bg='light blue', fg="white", font=("Arial", 30), relief=GROOVE, bd=10)
studentpro.grid(row=1, column=0, sticky='w', padx=500, pady=200)
Feerep = Label(root, text="Fee report", bg='light blue', fg="white", font=("Arial", 30), relief=GROOVE, bd=10)
Feerep.grid(row=2, column=0, sticky=W, padx=50)

root.mainloop()