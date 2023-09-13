from tkinter import *
# import random 
import os
from subprocess import call

def __information__():
    # pass
    # filename = 'index.py'
    # os.system(filename)
    # os.system('notepad' + filename + '.py')
    # os.system('index.py')
    call(['python','Std_Info_Frontend.py'])
    

def __feeReport__():
    # pass
    # filename = 'Fee_Frontend.py'
    # os.system(filename)
    # os.system('Visual Studio Code' + filename)
    call(['python','fee_frontend.py'])

def menu():
    root = Tk()
    root.title('Menu')
    root.geometry('1350x750')

    # Frame for School Management System

    title_frame = LabelFrame(root, font=('arial', 50, 'bold'), width=1000, height=100, bg= 'lightblue', relief = 'raise', bd= 13)
    title_frame.grid(row=0, column=0, pady=50, padx=250)

    title_label = Label(title_frame, text='School Management System', font=('arial', 30, 'bold' ), bg='lightblue')
    title_label.grid(row=0, column=0, padx=150)

    # Frame for Student Profile and Fee Reciept

    frame_1 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='lightblue', relief='ridge', bd=10)
    frame_1.grid(row = 1, column=0, padx=280)
    frame_2 = LabelFrame(root, font=('arial', 17, 'bold'),width=1000, height=100, bg='lightblue', relief='ridge', bd=10)
    frame_2.grid(row = 2, column=0, padx=280, pady=7)


    # Labels

    label_1 = Label(frame_1, text='STUDENT PROFILE', font=('arial', 25, 'bold'), bg='lightblue')
    label_1.grid(row=0, column=0, padx=50, pady=5)
    label_2 = Label(frame_2, text='FEE REPORT', font=('arial', 25, 'bold'), bg='lightblue')
    label_2.grid(row=0, column=0, padx=100, pady=5)

    # Buttons
    
    button_1 = Button(frame_1, text='VIEW', font=('arial', 16, 'bold'), width=8, command= __information__)
    button_1.grid(row=0, column=3, padx=50)
    button_2 = Button(frame_2, text='VIEW', font=('arial', 16, 'bold'), width=8, command= __feeReport__)
    button_2.grid(row=0, column=3, padx=50)

    root.mainloop()

# if __name__ == '__main__':
menu()