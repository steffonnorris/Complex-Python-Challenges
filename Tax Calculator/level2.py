from tkinter import *


root = Tk()
root.title('Tax Calculator')

# Error handling
def callback(input):
    pass

def age_set():
    if r.get() == 'Individual':
        e.configure(state=NORMAL)
        e.delete(0, END)
    else:
        e.insert(0, 'N/A')
        e.configure(state=DISABLED)
        e.delete(0, END)
        
# Calculate Taxes Due
def tax_calc():
    age = e.get()
    if age.isdigit():
        age = int(age)
    else:
        age = None
    income = e1.get()
    income = round(float(income))

    if r.get() == 'Individual':
        if age < 60:
            if income <= 20_000:
                tax = 0
            elif income > 20_000 and income <= 50_000:
                tax = income * 0.2
            elif income > 50_000 and income <= 100_000:
                tax = income * 0.3
            elif income > 100_000:
                tax = income * 0.4

        elif age >= 60:
            if income <= 20_000:
                tax = 0
            elif income > 20_000 and income <= 50_000:
                tax = income * 0.1
            elif income > 50_000 and income <= 100_000:
                tax = income * 0.2
            elif income > 100_000:
                tax = income * 0.3

    if r.get() == 'Business':
        # Additional business tax of 7.5%
        biz_tax = 0.075
        if income <= 20_000:
            tax = income * biz_tax
        elif income > 20_000 and income <= 50_000:
            tax = income * (0.2 + biz_tax)
        elif income > 50_000 and income <= 100_000:
            tax = income * (0.3 + biz_tax)
        elif income > 100_000:
            tax = income * (0.4 + biz_tax)

    e2.configure(state=NORMAL)
    e2.focus()
    result.set(f'${tax: ,.0f}')

def reset():
    e.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)


frame = LabelFrame(root, bg='lightgreen',
                   borderwidth=3, padx=15,
                   pady=5)
frame.grid(row=0, column=0)

r = StringVar()
r.set('Individual')

R1 = Radiobutton(frame, text='Individual', font=('Arial', 12, 'bold'), variable=r,
                 value='Individual', bg='gray', padx=8,
                 borderwidth=5, relief=SUNKEN, command=age_set)
R2 = Radiobutton(frame, text='Business', font=('Arial', 12, 'bold'), variable=r,
                 value='Business', bg='gray', padx=8,
                 borderwidth=5, relief=SUNKEN, command=age_set)
R1.grid(row=0, column=0, padx=5)
R2.grid(row=0, column=1, padx=5)


frame1 = LabelFrame(root, bg='lightgreen',
                    borderwidth=3,
                    padx=28, pady=5)
frame1.grid(row=1, column=0, pady=2)
l = Label(frame1, text='Age', bg='lightgreen', 
          font=('Arial', 12, 'bold'))
e = Entry(frame1, borderwidth=5, bg='gray',
          font=14, width=10)
l.grid(row=1, column=0)
e.grid(row=1, column=1)


frame2 = LabelFrame(root, bg='lightgreen',
                    borderwidth=3, padx=18,
                    pady=5)
frame2.grid(row=2, column=0, pady=2)
l1=Label(frame2, text='Income', bg='lightgreen',
         font=('Arial', 12, 'bold'))
e1 = Entry(frame2, borderwidth=5, bg='gray', font=14)
l1.grid(row=2, column=0)
e1.grid(row=2, column=1)


btnCalc = Button(root, text='Calculate', bg='green',
             fg='white', padx=15, 
             font=('Arial', 16, 'bold'),
             width=20, command=tax_calc)
btnCalc.grid(row=3, column=0, pady=2)


result = StringVar()
result.set('')

frame3 = LabelFrame(root, bg='blue',
                    borderwidth=3, padx=6,
                    pady=5)
frame3.grid(row=4, column=0, pady=20)
l2 = Label(frame3, text='Taxes Due', bg='blue',
           fg='white', font=('Arial', 14, 'bold'))
e2 = Entry(frame3, borderwidth=5, bg='gray',
           font=('Arial', 14, 'bold'),
           textvariable=result, state=DISABLED)
l2.grid(row=4, column=0)
e2.grid(row=4, column=1)


btnReset = Button(root, text='Reset', bg='darkred',
                 fg='white', padx=15,
                 font=('Arial', 16, 'bold'),
                 width=20, command=reset)
btnReset.grid(row=5, column=0, pady=2)


mainloop()
