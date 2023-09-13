from tkinter import *
from tkinter import ttk
import datetime
import Fee_Backend
import tkinter.messagebox

class Fee():
    def __init__(self, master):
        self.master = master
        self.master.title('School Management System / Fee Report ')
        self.master.geometry('1400x750+60+40')
        self.master.config(bg='lightblue')

        # =================== Variables ==========================

        self.receipt = StringVar()
        self.stu_name = StringVar()
        self.addmission = StringVar()
        self.branch = StringVar()
        self.date = StringVar()
        self.semester = StringVar()
        self.total = StringVar()
        self.paid_amount = StringVar()
        self.due = StringVar()

        # ========== Functions ================

        def Tuple(event):
            try:
                global st
                index = self.list.curselection()[0]
                st = self.list.get(index)

                receipt_no_en.delete(0, END)
                receipt_no_en.insert(END, st[1])
                stu_name_en.delete(0, END)
                stu_name_en.insert(END, st[2])
                addmission_no_entry.delete(0, END)
                addmission_no_entry.insert(END, st[3])
                date_entry.delete(0, END)
                date_entry.insert(END, st[4])
                branch_entry.delete(0, END)
                branch_entry.insert(END, st[5])
                semester_entry.delete(0, END)
                semester_entry.insert(END, st[6])
                total_en.delete(0, END)
                total_en.insert(END, st[7])
                paid_amount_en.delete(0, END)
                paid_amount_en.insert(END, st[8])
                due_en.delete(0, END)
                due_en.insert(END, st[9])

            except IndexError:
                pass

        def Save():
            # pass
            if (len(self.addmission.get()) != 0):
                Fee_Backend.insert(self.receipt.get(), self.stu_name.get(), self.addmission.get(), self.date.get(), self.branch.get(), self.semester.get(), self.total.get(), self.paid_amount.get(), self.due.get())
                self.list.delete(0, END)
                self.list.insert(END, (self.receipt.get(), self.stu_name.get(), self.addmission.get(), self.date.get(), self.branch.get(), self.semester.get(), self.total.get(), self.paid_amount.get(), self.due.get()))

        def Display():
            self.list.delete(0, END)
            for row in Fee_Backend.Display():
                self.list.insert(END, row, str(' '))

        def Reset():
            # pass
            self.receipt.set(' ')
            self.stu_name.set(' ')
            self.addmission.set(' ')
            self.branch.set(' ')
            self.semester.set(' ')
            self.paid_amount.set(' ')
            self.due.set(' ')
            display.delete('1.0', END)
            self.list.delete(0, END)
            # pass


        def Search():
            # pass
            self.list.delete(0, END)
            for row in Fee_Backend.search(self.receipt.get(), self.stu_name.get(), self.addmission.get(), self.date.get(), self.branch.get(), self.semester.get(), self.total.get(), self.paid_amount.get()):
                self.list.insert(END, row, str(' '))

        def Delete():
            # pass
            Fee_Backend.delete(st[0])
            Reset()
            Display()
            
        def Receipt():
            # pass
            display.delete('1.0', END)
            display.insert(END, '\t\tReceipt' + '\n\n')
            display.insert(
                END, '\tReceipt No. \t  :' + self.receipt.get() + '\n') 
            display.insert(END, '\tStudent Name :' + self.stu_name.get() + '\n')
            display.insert(END, '\tAddmission No. \t:' + self.addmission.get() + '\n')
            display.insert(END, '\tDate\t       :' + self.date.get()+ '\n')
            display.insert(END, '\tBranch\t       :' + self.branch.get()+ '\n')
            display.insert(END, '\tSemester\t       :' + self.semester.get()+ '\n')

            x1 = (var_1.get())
            x2 = (self.paid_amount.get())
            x3 = x1-x2


            (display.insert(END, '\tTotal Amount :' + str(x1) + '\n'))
            (display.insert(END, '\tPaid Amount :' + str(x2) + '\n'))
            (display.insert(END, '\tTotal Amount :' + str(x3) + '\n'))

            self.due.set(x3)

        def Update():
            Fee_Backend.delete(st[0])
            Save()

        def Exit():
            # pass
            Exit = tkinter.messagebox.askyesno('Important', 'Confirm, if you want to Exit')
            if Exit > 0:
                root.destroy()
                return
        

        # ==================== Frames =========================

        main_frame = Frame(self.master, bg='lightblue')
        main_frame.grid()

        title_frame = LabelFrame(main_frame, width=1350, height=100, bg='lightblue', relief='ridge', bd=15)
        title_frame.pack(side=TOP)
        # how to take label at center???

        self.lblTitle = Label(title_frame, font=('arial', 40, 'bold'), text='Fee Report', bg='lightblue', padx=13)
        self.lblTitle.grid(row=0, column=0, padx=470)

        # ======== Making the Center Frame ==========

        data_frame = Frame(main_frame, width=950, height=400, bg='lightblue', relief='ridge', bd=15)
        data_frame.pack(side=TOP, padx=5)

        # ========== Making Iformation Frame and Fee recipt  ==============

        info_frame = LabelFrame(data_frame, text='Informations', width=650, height=250, relief='ridge', bd=10, font=('arial', 15, 'bold'), bg='Navajo white')
        info_frame.pack(side=LEFT, padx=10, pady=20)

        fee_recipt_frame = LabelFrame(data_frame, text='Fee Receipt', height=300, width=400, font=('arial', 15, 'bold'), bg='Navajo white', bd=10)
        fee_recipt_frame.pack(side='right', padx=10)

        # ========= Making list frame =============

        list_frame = Frame(main_frame, height=150, width=1350, bd=15, bg='navajo white', relief=RIDGE)
        list_frame.pack(side=TOP, padx=20)

        # ============ Button Frame ============== 

        button_frame = Frame(main_frame, width=1350, height=100, bd=15, bg='navajo white', relief=RIDGE)
        button_frame.pack(side=TOP, padx=20)

        # ======= Making the contents of information frame ============

        receipt_no = Label(info_frame, text='Receipt No. :', font=('arial', 14, 'bold'), bg='Navajo white')
        receipt_no.grid(row=0, column=0, padx=10, sticky=W)

        student_name = Label(info_frame, text='Student Name :', font=('arial', 14, 'bold'), bg='Navajo white')
        student_name.grid(row=1, column=0, padx=10, sticky=W)

        addmission = Label(info_frame, text='Admission :', font=('arial', 14, 'bold'), bg='Navajo white')
        addmission.grid(row=2, column=0, padx=10, sticky=W)

        date = Label(info_frame, text='Date :', font=('arial', 14, 'bold'), bg='Navajo white')
        date.grid(row=3, column=0, padx=10, sticky=W)

        branch = Label(info_frame, text='Branch :', font=('arial', 14, 'bold'), bg='Navajo white')
        branch.grid(row=4, column=0, padx=10, sticky=W)

        semester = Label(info_frame, text='Semester :', font=('arial', 14, 'bold'), bg='Navajo white')
        semester.grid(row=5, column=0, padx=10, sticky=W)

        total_amount = Label(info_frame, text='TOTAL AMOUNT :', font=('arial', 14, 'bold'), bg='Navajo white')
        total_amount.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        paid_amount = Label(info_frame, text='PAID AMOUNT :', font=('arial', 14, 'bold'),bg='Navajo white' )
        paid_amount.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        due = Label(info_frame, text='Due :', font=('arial', 14, 'bold'),bg='Navajo white' )
        due.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        # ========================= Entry Fields =================================

        var_1 = DoubleVar(info_frame, value='15000')
        d1 = datetime.date.today()
        self.date.set(d1)

        receipt_no_en = Entry(info_frame, font=('arial', 14), textvariable=self.receipt)
        receipt_no_en.grid(row=0, column=1, padx=10, pady=5)

        stu_name_en = Entry(info_frame, font=('arial', 14), textvariable=self.stu_name)
        stu_name_en.grid(row=1, column=1, padx=10, pady=5)

        addmission_no_entry = Entry(info_frame, font=('arial', 14), textvariable=self.addmission)
        addmission_no_entry.grid(row=2, column=1, padx=10, pady=5)

        date_entry = Entry(info_frame, font=('arial', 14), textvariable=self.date)
        date_entry.grid(row=3, column=1, padx=10, pady=5)

        branch_entry = ttk.Combobox(info_frame, values=(' ', 'CSE', 'IT', 'IS', 'CE'), width=18, font=('arial', 14), textvariable=self.branch)
        branch_entry.grid(row=4, column=1, padx=10, pady=5)

        semester_entry = ttk.Combobox(info_frame, values=(' ', 'FIRST', 'SECOND', 'THIRD'), font=('arial', 14), width=18, textvariable=self.semester)
        semester_entry.grid(row=5, column=1, padx=10, pady=5)

        total_en = Entry(info_frame, font=('arial', 14), width=10, textvariable=var_1, state='readonly')
        total_en.grid(row=2, column=3, padx=10, pady=5)

        paid_amount_en = Entry(info_frame, font=('arial', 14),  width=10, textvariable=self.paid_amount)
        paid_amount_en.grid(row=3, column=3, padx=10, pady=5)

        due_en = Entry(info_frame, font=('arial', 14),  width=10, textvariable=self.due)
        due_en.grid(row=4, column=3, padx=10, pady=5)

        #  ================ textbox in fee receipt frame ===================

        display = Text(fee_recipt_frame, width=42, height=12, font=('arial', 14, 'bold'))
        display.grid(row=0, column=0, padx=3)

        # ========= Listbox and scrollbar ===========

        sb = Scrollbar(list_frame)
        sb.grid(row=0, column=1, sticky='ns')

        self.list = Listbox(list_frame, font=('arial', 13, 'bold'), width=140, height=8)
        self.list.bind('<<ListboxSelect>>', Tuple)
        self.list.grid(row=0, column=0)
        sb.config(command=self.list.yview)

        # ============= Buttons ==================

        btnSave = Button(button_frame, text='Save', font=('arial', 14, 'bold'), width=10, command=Save)
        btnSave.grid(row=0, column=0, padx=5, pady=5)

        btnDisplay = Button(button_frame, text='Display', font=('arial', 14, 'bold'), width=10, command=Display)
        btnDisplay.grid(row=0, column=1, padx=5, pady=5)

        btnReset = Button(button_frame, text='Reset', font=('arial', 14, 'bold'), width=10, command=Reset)
        btnReset.grid(row=0, column=2, padx=5, pady=5)

        btnUpdate = Button(button_frame, text='Update', font=('arial', 14, 'bold'), width=10, command=Update)
        btnUpdate.grid(row=0, column=3, padx=5, pady=5)

        btnSearch = Button(button_frame, text='Search', font=('arial', 14, 'bold'), width=10, command=Search)
        btnSearch.grid(row=0, column=4, padx=5, pady=5)

        btnDelete = Button(button_frame, text='Delete', font=('arial', 14, 'bold'), width=10, command=Delete)
        btnDelete.grid(row=0, column=5, padx=5, pady=5)

        btnReceipt = Button(button_frame, text='Reciept', font=('arial', 14, 'bold'), width=10, command=Receipt)
        btnReceipt.grid(row=0, column=6, padx=5, pady=5)

        btnExit = Button(button_frame, text='Exit', font=('arial', 14, 'bold'), width=10, command=Exit)
        btnExit.grid(row=0, column=7, padx=5, pady=5)
        

root = Tk()
obj = Fee(root)
root.mainloop()