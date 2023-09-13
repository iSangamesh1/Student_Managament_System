from tkinter import *
from tkinter import ttk
import random
import Std_Info_Backend
import tkinter.messagebox

class Std_Info:
    def __init__(self, master):
            self.master = master
            self.master.title('School Management System/Student Information')
            self.master.geometry('1350x750')
            self.master.config(bg='lightblue')

            # ============= Variables=================
            self.name = StringVar()
            self.fname = StringVar()
            self.mname = StringVar()
            self.address = StringVar()
            self.mobno= StringVar()
            self.email = StringVar()
            self.dob = StringVar()
            self.gender = StringVar()

            # ============== Functions ==================

            def StudentRec(event):
                # pass
                try:
                    global selected_tuple
                    index = self.listbox.curselection()[0]
                    selected_tuple = self.listbox.get(index)

                    self.entry_name.delete(0, END)
                    self.entry_name.insert(END, selected_tuple[1])
                    self.entry_fname.delete(0, END)
                    self.entry_fname.insert(END, selected_tuple[2])
                    self.entry_mname.delete(0, END)
                    self.entry_mname.insert(END, selected_tuple[3])
                    self.entry_address.delete(0, END)
                    self.entry_address.insert(END, selected_tuple[4])
                    self.entry_mobno.delete(0, END)
                    self.entry_mobno.insert(END, selected_tuple[5])
                    self.entry_emailID.delete(0, END)
                    self.entry_emailID.insert(END, selected_tuple[6])
                    self.entry_dob.delete(0, END)
                    self.entry_dob.insert(END, selected_tuple[7])
                    self.entry_gender.delete(0, END)
                    self.entry_gender.insert(END, selected_tuple[8])

                except:
                    pass

            def Add():
                # pass
                if(len(self.name.get()) != 0):
                               Std_Info_Backend.insert(self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(),self.gender.get())
                               self.listbox.delete(0, END)
                               self.listbox.insert(END, (self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(),self.gender.get()))
            def Display():
                self.listbox.delete(0, END)
                for row in Std_Info_Backend.view():
                    self.listbox.insert(END, row, str(' '))
                

            def Exit():
                Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
                if Exit > 0:
                    self.master.destroy()
                    return
                
            def Reset():
                self.name.set('')
                self.fname.set('')
                self.mname.set('')
                self.address.set('')
                self.mobno.set('')
                self.email.set('')
                self.dob.set('')
                self.gender.set('')
                self.listbox.delete(0, END)
            def Delete():
                if(len(self.name.get()) != 0):
                    Std_Info_Backend.delete(selected_tuple[0])
                    Reset()
                    Display()
            def Search():
                self.listbox.delete(0, END)
                for row in Std_Info_Backend.search(self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(),self.gender.get()):
                    self.listbox.insert(END, row, str(' '))

            def Update():
                if(len(self.name.get()) != 0):
                    Std_Info_Backend.delete(selected_tuple[0])
                    if(len(self.name.get()) != 0):
                        Std_Info_Backend.insert(self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), self.gender.get())
                        self.listbox.delete(0, END)
                        self.listbox.insert(END, (self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), self.gender.get()))

            # ================================== Frames ==========================

            self.main_frame = LabelFrame(self.master, width=1300, height=500, font=('arial', 20, 'bold'), bg='lightblue', bd=15, relief='ridge')
            self.main_frame.grid(row=0, column=0, padx=10, pady=20)

            self.frame_1 = LabelFrame(self.main_frame, width=600, height=400, font=('arial', 15, 'bold'), relief='ridge', bd=10, bg='lightblue', text='STUDENT INFORMATION')
            self.frame_1.grid(row=1, column=0, padx=10) 

            self.frame_2 = LabelFrame(self.main_frame, width=750, height=400, font=('arial', 15, 'bold'), relief='ridge', bd=10, bg='lightblue', text='STUDENT DATABASE')
            self.frame_2.grid(row=1, column=1, padx=5)

            self.frame_3 = LabelFrame(self.master, width=1200, height=100, font=('arial', 10, 'bold'), bg='lightblue', relief='ridge', bd=13)
            self.frame_3.grid(row=2, column=0, pady=10)

            # =========== Labels of Frame_1 ===============================================

            self.label_name = Label(self.frame_1, text='Name : ', font=('arial', 20, 'bold'), bg='lightblue', )
            # self.label_name.grid(row=0, column=0, sticky=W, padx=20, pady=20)
            self.label_name.grid(row=0, column=0, sticky=W, padx=20)

            self.label_fname = Label(self.frame_1, text='Father Name : ', font=('arial', 20, 'bold'), bg='lightblue')
            self.label_fname.grid(row=1, column=0, sticky=W, padx=20)

            self.label_mname = Label(self.frame_1, text='Mother Name : ', font=('arial', 20, 'bold'), bg='lightblue')
            self.label_mname.grid(row=2, column=0, sticky=W, padx=20)

            self.label_address = Label(self.frame_1, text='Address : ', font=('arial', 20, 'bold'), bg='lightblue')
            self.label_address.grid(row=3, column=0, sticky=W, padx=20)

            self.label_mobno = Label(self.frame_1, text='Mobile Number : ', font=('arial', 20, 'bold'), bg='lightblue')
            self.label_mobno.grid(row=4, column=0, sticky=W, padx=20)

            self.label_email = Label(self.frame_1, text='Email Id : ', font=('arial', 20, 'bold'), bg='lightblue')
            self.label_email.grid(row=5, column=0, sticky=W, padx=20)

            self.label_dob = Label(self.frame_1, text='Date of Birth : ', font=('arial', 20, 'bold'), bg='lightblue')
            self.label_dob.grid(row=6, column=0, sticky=W, padx=20)

            self.label_gender = Label(self.frame_1, text='Gender : ', font=('arial', 20, 'bold'), bg='lightblue')
            self.label_gender.grid(row=7, column=0, sticky=W, padx=20)

            # ===================== EntryBox =================================

            self.entry_name = Entry(self.frame_1, font=('arial', 17, 'bold'), textvariable=self.name)
            self.entry_name.grid(row=0, column=1, padx=10, pady=5)
            self.entry_fname = Entry(self.frame_1, font=('arial', 17, 'bold'), textvariable=self.fname)
            self.entry_fname.grid(row=1, column=1, padx=10, pady=5)
            self.entry_mname = Entry(self.frame_1, font=('arial', 17, 'bold'), textvariable=self.mname)
            self.entry_mname.grid(row=2, column=1, padx=10, pady=5)
            self.entry_address = Entry(self.frame_1, font=('arial', 17, 'bold'), textvariable=self.address)
            self.entry_address.grid(row=3, column=1, padx=10, pady=5)
            self.entry_mobno = Entry(self.frame_1, font=('arial', 17, 'bold'), textvariable=self.mobno)
            self.entry_mobno.grid(row=4, column=1, padx=10, pady=5)
            self.entry_email = Entry(self.frame_1, font=('arial', 17, 'bold'), textvariable=self.email)
            self.entry_email.grid(row=5, column=1, padx=10, pady=5)
            self.entry_dob = Entry(self.frame_1, font=('arial', 17, 'bold'), textvariable=self.dob)
            self.entry_dob.grid(row=6, column=1, padx=10, pady=5)
            self.entry_gender = ttk.Combobox(self.frame_1, values=('', 'Male', 'Female', 'Others'), font=('arial', 17, 'bold'), width=19, textvariable=self.gender)
            self.entry_gender.grid(row=7, column=1, padx=10, pady=5)

            # ================= Buttons ==============

            self.btnSave = Button(self.frame_3, text='Save', font=('arial', 17, 'bold'), width=8, command=Add)
            self.btnSave.grid(row=0, column=0, padx=10, pady=10)
            self.btnDisplay = Button(self.frame_3, text='Display', font=('arial', 17, 'bold'), width=8, command=Display)
            self.btnDisplay.grid(row=0, column=1, padx=10, pady=10)
            self.btnReset = Button(self.frame_3, text='Reset', font=('arial', 17, 'bold'), width=8, command=Reset)
            self.btnReset.grid(row=0, column=2, padx=10, pady=10)
            self.btnUpdate = Button(self.frame_3, text='Update', font=('arial', 17, 'bold'), width=8, command=Update)
            self.btnUpdate.grid(row=0, column=3, padx=10, pady=10)
            self.btnDelete = Button(self.frame_3, text='Delete', font=('arial', 17, 'bold'), width=8, command=Delete)
            self.btnDelete.grid(row=0, column=4, padx=10, pady=10)
            self.btnSearch = Button(self.frame_3, text='Search', font=('arial', 17, 'bold'), width=8, command=Search)
            self.btnSearch.grid(row=0, column=5, padx=10, pady=10)
            self.btnExit = Button(self.frame_3, text='Exit', font=('arial', 17, 'bold'), width=8, command=Exit)
            self.btnExit.grid(row=0, column=6, padx=10, pady=10)

            # ==== List Box and self.scrollbar ================
            self.scrollbar = Scrollbar(self.frame_2)
            self.scrollbar.grid(row=0, column=1, sticky='ns')

            self.listbox = Listbox(self.frame_2, width=75, height=20, font=('arial', 12, 'bold'))
            self.listbox.bind('<<ListboxSelect>>', StudentRec)
            self.listbox.grid(row=0, column=0)
            self.scrollbar.config(command=self.listbox.yview)




root = Tk()
obj = Std_Info(root)
root.mainloop()
