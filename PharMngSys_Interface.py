----------------------------------------------------# Interface of Pharmacy Management System created using Tkinter #--------------------------------------------------

# Just an example code to elaborate use of Tkinter library of python.

from tkinter import*

root = Tk()
root.title("Pharmacy Management System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1000
height = 500
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

MedicineName = StringVar()
MedicinePrice = StringVar()
Quantity = StringVar()
Category = StringVar()

Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=200, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=250, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)

txt_title = Label(Top, width=900, font=('arial', 24), fg='black', text="Pharmacy Management System")
txt_title.pack()
label0 = Label(Forms, text="Medicine Name:", fg='black', font=('arial', 16), bd=15)
label0.grid(row=0, stick="e")
label1 = Label(Forms, text="Medicine Price:", fg='black', font=('arial', 16), bd=15)
label1.grid(row=1, stick="e")
label2 = Label(Forms, text="Quantity:", fg='black', font=('arial', 16), bd=15)
label2.grid(row=2, stick="e")
label3 = Label(Forms, text="Category:", fg='black', font=('arial', 16), bd=15)
label3.grid(row=3, stick="e")

txt_result = Label(Buttons)
txt_result.pack(side=TOP)

entry1 = Entry(Forms, textvariable=MedicineName, width=30)
entry1.grid(row=0, column=1)
entry2 = Entry(Forms, textvariable=MedicinePrice, width=30)
entry2.grid(row=1, column=1)
entry3 = Entry(Forms, textvariable=Quantity, width=30)
entry3.grid(row=2, column=1)
entry4 = Entry(Forms, textvariable=Category, width=30)
entry4.grid(row=3, column=1)

btn_clear = Button(Buttons, width=10, text="CLEAR", command=clearitem)
btn_clear.pack(side=LEFT)

root.mainloop()
