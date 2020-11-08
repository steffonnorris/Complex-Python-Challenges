from tkinter import *
from tkinter import messagebox


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
    income = e1.get()
    if age.isdigit():
        age = int(age)
    else:
        age = None
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

    # result = f'Taxes Due: ${tax: ,.0f}'
    # e2.configure(textvariable=result)

    messagebox.showinfo('Tax Calculator',
                        f'Taxes Due: ${tax: ,.0f}',
                        )


frame = LabelFrame(root, bg='lightgreen',
                   borderwidth=3, padx=28,
                   pady=5)
frame.grid(row=0, column=0, pady=5)

r = StringVar()
r.set('Individual')

R1 = Radiobutton(frame, text='Individual', font=14, variable=r,
                 value='Individual', bg='gray', padx=8,
                 borderwidth=5, relief=SUNKEN, command=age_set)
R2 = Radiobutton(frame, text='Business', font=14, variable=r,
                 value='Business', bg='gray', padx=8,
                 borderwidth=5, relief=SUNKEN, command=age_set)
R1.grid(row=0, column=0)
R2.grid(row=0, column=1)


frame1 = LabelFrame(root, bg='lightgreen',
                    borderwidth=3,
                    padx=28, pady=5)
frame1.grid(row=1, column=0, pady=2)
l = Label(frame1, text='Age', bg='lightgreen', 
          font=14)
e = Entry(frame1, borderwidth=5, bg='gray',
          font=14, width=10)
l.grid(row=1, column=0)
e.grid(row=1, column=1)


frame2 = LabelFrame(root, bg='lightgreen',
                    borderwidth=3, padx=18,
                    pady=5)
frame2.grid(row=2, column=0, pady=2)
l1 = Label(frame2, text='Income', bg='lightgreen', font=14)
e1 = Entry(frame2, borderwidth=5, bg='gray', font=14)
l1.grid(row=2, column=0)
e1.grid(row=2, column=1)


btn = Button(root, text='Calculate', bg='green',
            fg='white', padx=15, pady=5, font=28,
            width=20, command=tax_calc)
btn.grid(row=3, column=0, pady=2)

frame3 = LabelFrame(root, bg='darkblue',
                    borderwidth=3, padx=18,
                    pady=5)
frame3.grid(row=4, column=0, pady=2)
l2 = Label(frame3, text='Taxes Due', bg='darkblue',
           fg='white', font=('Arial', 12, 'bold'))
e2 = Entry(frame3, borderwidth=5, bg='gray', font=14)
l2.grid(row=4, column=0)
e2.grid(row=4, column=1)



mainloop()
