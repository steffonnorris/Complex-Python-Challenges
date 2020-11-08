from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Tile Calculator')

# Utility functions for the GUI

def callback(input):
    '''Ensures 'Entry' inputs follows correct parameters'''

    if input.isdigit():
        return True

    if input is clear_all():
        return True

    else:
        return False


def calculate():
    length = e.get()
    width = e1.get()
    price = e2.get()
    discount = e3.get()

    if length == '' or width == '' or \
        price == '' or discount == '':
        messagebox.showerror('Missing Values',
                             'Required Fields Are Blank')
    
    else:
        length = float(length)
        width = float(width)
        price = float(price)
        discount = float(discount)

    # Convert units to feet
    if r.get() == 'in':
        length *= 0.083333333
        width *= 0.083333333
    elif r.get() == 'm':
        length *= 3.280839895
        width *= 3.280839895
    elif r.get() == 'cm':
        length *= 0.032808399
        width *= 0.032808399

    area = length * width
    total = area * price
    disc_amt = (discount / 100) * total
    final = total - disc_amt

    messagebox.showinfo('Result',
                        f'Area: {area: ,.2f} ft\N{SUPERSCRIPT TWO}\n'
                        f'Price/sq.ft: ${price: ,.2f}\n'
                        f'Total: ${total: ,.2f}\n'
                        f'Discount: ${disc_amt: ,.2f}\n'
                        f'Discounted Total: ${final: ,.2f}'
                        )


def clear_all():
    e.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


# padx, pady add padding inside the frame
frame = LabelFrame(root, font=14, padx=5,
                   text='Unit of Measurement',
                   pady=10, borderwidth=5,
                   bg='lightgray', labelanchor=N
                   )
# padx, pady add padding outside the frame
frame.grid(row=0, column=0, pady=10)

# Radio button Tkinter variables
r = StringVar()
r.set('ft')

R1 = Radiobutton(frame, text="ft", font=12, variable=r,
                 value='ft', bg='gray', relief=SUNKEN)
R2 = Radiobutton(frame, text="in", font=12, variable=r,
                 value='in', bg='gray', relief=SUNKEN)
R3 = Radiobutton(frame, text="m", font=12, variable=r,
                 value='m', bg='gray', relief=SUNKEN)
R4 = Radiobutton(frame, text="cm", font=12, variable=r,
                 value='cm', bg='gray', relief=SUNKEN)

R1.grid(row=0, column=1, padx=1)
R2.grid(row=0, column=2, padx=1)
R3.grid(row=0, column=3, padx=1)
R4.grid(row=0, column=4, padx=1)


frame1 = LabelFrame(root, borderwidth=5,
                    text='Measurements', font=14,
                    padx=5, pady=5, bg='lightgray',
                    labelanchor=N)
frame1.grid(row=1, column=0, pady=10)

l = Label(frame1, text='Length', font=12, bg='lightgray')
l1 = Label(frame1, text='Width', font=12, bg='lightgray')
e = Entry(frame1, width=13, font=12, borderwidth=5,
          bg='gray')
e1 = Entry(frame1, width=13, font=12, borderwidth=5,
           bg='gray')

l.grid(row=1, column=0)
l1.grid(row=2, column=0)
e.grid(row=1, column=1)
e1.grid(row=2, column=1)

reg = root.register(callback)
e.config(validate="key", validatecommand=(reg, '%P'))
e1.config(validate="key", validatecommand=(reg, '%P'))


# Input price ($/sq.ft)
frame2 = LabelFrame(root, text='Price',
                    font=14, borderwidth=5, padx=5,
                    pady=5, bg='lightgray',
                    labelanchor=N)
frame2.grid(row=3, column=0, pady=10)

l2 = Label(frame2, text='$/sq.ft: ', font=12, bg='lightgray')
e2 = Entry(frame2, width=13, font=12, bg='gray', borderwidth=5)

l2.grid(row=3, column=0)
e2.grid(row=3, column=1)
e2.config(validate="key", validatecommand=(reg, '%P'))


# Input % discount
frame3 = LabelFrame(root, borderwidth=5,
                    text='Discount Offered',
                    font=14, padx=5, pady=5,
                    bg='lightgray', labelanchor=N
                    )
frame3.grid(row=4, column=0, padx=8, pady=10)

l3 = Label(frame3, text='% of Price: ', font=12, bg='lightgray')
e3 = Entry(frame3, width=10, font=12, bg='gray',
           borderwidth=5)
l3.grid(row=4, column=0)
e3.grid(row=4, column=1)

e3.config(validate="key", validatecommand=(reg, '%P'))


frame4 = LabelFrame(root, borderwidth=5,
                    font=14, padx=5, pady=5,
                    bg='lightgray')
frame4.grid(row=5, column=0, pady=10)
# Submit data
submit = Button(frame4, text='Submit', font=24,
                padx=24, pady=2, bg='darkblue',
                fg='white', command=calculate)
submit.grid(row=5, column=0, pady=5)

# Clear display
clear = Button(frame4, text='Clear Display', font=24,
               pady=5, bg='red', fg='white',
               command=clear_all)
clear.grid(row=6, column=0, pady=5)


mainloop()
