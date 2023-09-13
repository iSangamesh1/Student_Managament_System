import tkinter
import os
from tkinter import messagebox
from subprocess import call
window = tkinter.Tk()
window.title("Login Page using Python")
window.geometry('750x550')
window.configure(bg='light blue') 
frame = tkinter.Frame(bg='light blue')
login_label = tkinter.Label(frame, text="Login Menu", bg='blue', fg="white", font=("Arial", 30), relief='groove', bd=10)

def login():
    username = "KushalM"
    password = "Helloworld"
    def menu():
        call(['python', 'Menu.py'])
        # filename = 'Menu.py'
        # os.system(filename)
        # os.system('notepad'+filename)
    
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
        menu()
        window.destroy()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

username_label = tkinter.Label(frame, text="Username", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))
password_label = tkinter.Label(frame, text="Password", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg="navy blue", fg="white", font=("Arial", 16), command=login)
login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
frame.pack()
window.mainloop()