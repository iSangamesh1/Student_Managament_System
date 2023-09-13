from tkinter import *
import tkinter.messagebox
import os
import random
from subprocess import call

def main():
    root = Tk()
    app = Window_1(root)

class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title('School Management System')
        self.master.geometry('1370x750+100+50')
        self.master.config(bg='green')
        self.Frame = Frame(self.master, bg='green')
        self.Frame.pack()

        # Input Variables
         
        self.Username = StringVar()
        self.Password = StringVar()

    

        # ================= Heading =====================
        
        self.label_title = Label(self.Frame, text='Login Menu', font=('arial', 55, 'bold'), bg='green', fg='black')
        self.label_title.grid(row=0, column=0, pady=40)
        
        #  ================= Label =======================

        self.login_frame_1 = LabelFrame(self.Frame, width=1350, height=600, relief='ridge', bg='green', bd=15, font=('arial', 15, 'bold'))
        self.login_frame_1.grid(row=1, column=0)

        self.login_frame_2 = LabelFrame(self.Frame, width=1000, height=600, relief='ridge', bg='green', bd=15, font=('arial', 15, 'bold'))
        self.login_frame_2.grid(row=2, column=0, pady=20)

        # ================= Label and Entries =======================

        # Username

        self.label_username = Label(self.login_frame_1, text='Username', font=('arial', 20, 'bold'), bg='green', bd = 20)
        self.label_username.grid(row=0, column=0)

        self.text_username = Entry(self.login_frame_1, font=('arial', 20, 'bold'), textvariable=self.Username)
        self.text_username.grid(row=0, column=1, padx=50)

        # Password

        self.label_password = Label(self.login_frame_1, text='Password', font=('arial', 20, 'bold'), bg='green', bd = 20)
        self.label_password.grid(row=1, column=0)

        self.text_password = Entry(self.login_frame_1, show='*', font=('arial', 20, 'bold'), textvariable=self.Password)
        self.text_password.grid(row=1, column=1, padx=50)

        # ======================== Buttons ================================

        self.btn_login = Button(self.login_frame_2, text='Login', width = 10, font=('arial', 15, 'bold'), command = self.login)
        self.btn_login.grid(row=0, column=0, padx=8, pady=20)

        self.btn_reset = Button(self.login_frame_2, text='Reset', width=10, font=('arial', 15, 'bold'), command=self.reset)
        self.btn_reset.grid(row=0, column=1, padx=8, pady=20)

        self.btn_exit = Button(self.login_frame_2, text='Exit', width=10, font=('arial', 15, 'bold'), command=self.exit)
        self.btn_exit.grid(row=0, column=2, padx=8, pady=20)


        self.master.mainloop()

    # Funtions

    def login(self):
        u = (self.Username.get())  
        p = (self.Password.get())  

        if(u == str('admin') and p == str('admin')):
            # self.__menu__()
            self.menu()
        else:
            tkinter.messagebox.askyesno('Login', 'Error : Wrong Password' )
            self.Username.set('')
            self.Password.set('')

    def reset(self):
        self.Username.set('')
        self.Password.set('')
        self.text_username.focus()


    def exit(self):
        self.exit = tkinter.messagebox.askokcancel('Login System',  'Cancel if you want to exit')
        if self.exit > 0:
            self.master.destroy()
            return

    # def __menu__(self):
    def menu(self):
        # filename = 'menu.py'
        # os.system(filename)
        # os.system('notepad'+filename)
        call(['python','menu.py'])

if __name__ == '__main__':
    main()