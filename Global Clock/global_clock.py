from tkinter import *
from datetime import datetime as dt
import pytz


root = Tk()
root.title('Global Clock')

# Get list of all timezones
# for tz in pytz.all_timezones:
#     print(tz)


def time():
    '''Displays time on the label'''

    # Set timezone
    home = pytz.timezone('America/New_York')
    # Get local time in timezone
    local_time = dt.now(home)
    # Format time
    current_time = local_time.strftime('%H:%M:%S %p')
    # Set label text as local time
    lbl.config(text=current_time)

    home = pytz.timezone('Europe/London')
    local_time = dt.now(home)
    current_time = local_time.strftime('%H:%M:%S %p')
    lbl1.config(text=current_time)

    home = pytz.timezone('Africa/Nairobi')
    local_time = dt.now(home)
    current_time = local_time.strftime('%H:%M:%S %p')
    lbl2.config(text=current_time)

    home = pytz.timezone('Asia/Hong_Kong')
    local_time = dt.now(home)
    current_time = local_time.strftime('%H:%M:%S %p')
    lbl3.config(text=current_time)

    home = pytz.timezone('Japan')
    local_time = dt.now(home)
    current_time = local_time.strftime('%H:%M:%S %p')
    lbl4.config(text=current_time)

    home = pytz.timezone('America/Vancouver')
    local_time = dt.now(home)
    current_time = local_time.strftime('%H:%M:%S %p')
    lbl5.config(text=current_time)

    home = pytz.timezone('Brazil/East')
    local_time = dt.now(home)
    current_time = local_time.strftime('%H:%M:%S %p')
    lbl6.config(text=current_time)

    home = pytz.timezone('Africa/Lagos')
    local_time = dt.now(home)
    current_time = local_time.strftime('%H:%M:%S %p')
    lbl7.config(text=current_time)

    home = pytz.timezone('Asia/Jakarta')
    local_time = dt.now(home)
    current_time = local_time.strftime('%H:%M:%S %p')
    lbl8.config(text=current_time)

    home = pytz.timezone('Pacific/Auckland')
    local_time = dt.now(home)
    current_time = local_time.strftime('%H:%M:%S %p')
    lbl9.config(text=current_time)

    # Updates labels after 1000ms
    lbl.after(1000, time)


# Make clock widgets

frame = LabelFrame(root, text='New York (GMT -5)',
                   font=('calibri', 14, 'bold'),
                   borderwidth=5, bg='black',
                   fg='red', labelanchor=N,
                   pady=10)
frame.grid(row=0, column=0, padx=5, pady=5)
lbl = Label(frame, font=('calibri', 28, 'bold'),
            bg='darkblue', fg='white')
lbl.grid(row=0, column=0)


frame1 = LabelFrame(root, text='London (GMT +0)',
                    font=('calibri', 14, 'bold'),
                    borderwidth=5, bg='black',
                    fg='red', labelanchor=N,
                    pady=10)
frame1.grid(row=0, column=1, padx=5, pady=5)
lbl1 = Label(frame1, font=('calibri', 28, 'bold'),
             bg='darkblue', fg='white')
lbl1.grid(row=0, column=1)


frame2 = LabelFrame(root, text='Nairobi (GMT +3)',
                    font=('calibri', 14, 'bold'),
                    borderwidth=5, bg='black',
                    fg='red', labelanchor=N,
                    pady=10)
frame2.grid(row=0, column=2, padx=5, pady=5)
lbl2 = Label(frame2, font=('calibri', 28, 'bold'),
             bg='darkblue', fg='white')
lbl2.grid(row=0, column=2)


frame3 = LabelFrame(root, text='Hong Kong (GMT +8)',
                    font=('calibri', 14, 'bold'),
                    borderwidth=5, bg='black',
                    fg='red', labelanchor=N,
                    pady=10)
frame3.grid(row=0, column=3, padx=5, pady=5)
lbl3 = Label(frame3, font=('calibri', 28, 'bold'),
             bg='darkblue', fg='white')
lbl3.grid(row=0, column=3)


frame4 = LabelFrame(root, text='Tokyo (GMT +9)',
                    font=('calibri', 14, 'bold'),
                    borderwidth=5, bg='black',
                    fg='red', labelanchor=N,
                    pady=10)
frame4.grid(row=0, column=4, padx=5, pady=5)
lbl4 = Label(frame4, font=('calibri', 28, 'bold'),
             bg='darkblue', fg='white')
lbl4.grid(row=0, column=4)


frame5 = LabelFrame(root, text='Vancouver (GMT -8)',
                    font=('calibri', 14, 'bold'),
                    borderwidth=5, bg='black',
                    fg='red', labelanchor=N,
                    pady=10)
frame5.grid(row=1, column=0, padx=5, pady=5)
lbl5 = Label(frame5, font=('calibri', 28, 'bold'),
             bg='darkblue', fg='white')
lbl5.grid(row=1, column=0)


frame6 = LabelFrame(root, text='Rio de Janeiro (GMT -3)',
                    font=('calibri', 14, 'bold'),
                    borderwidth=5, bg='black',
                    fg='red', labelanchor=N,
                    pady=10)
frame6.grid(row=1, column=1, padx=5, pady=5)
lbl6 = Label(frame6, font=('calibri', 28, 'bold'),
             bg='darkblue', fg='white')
lbl6.grid(row=1, column=1)


frame7 = LabelFrame(root, text='Lagos (GMT +1)',
                    font=('calibri', 14, 'bold'),
                    borderwidth=5, bg='black',
                    fg='red', labelanchor=N,
                    pady=10)
frame7.grid(row=1, column=2, padx=5)
lbl7 = Label(frame7, font=('calibri', 28, 'bold'),
             bg='darkblue', fg='white')
lbl7.grid(row=1, column=2)


frame8 = LabelFrame(root, text='Jakarta (GMT + 7)',
                    font=('calibri', 14, 'bold'),
                    borderwidth=5, bg='black',
                    fg='red', labelanchor=N,
                    pady=10)
frame8.grid(row=1, column=3, padx=5)
lbl8 = Label(frame8, font=('calibri', 28, 'bold'),
             bg='darkblue', fg='white')
lbl8.grid(row=1, column=3)


frame9 = LabelFrame(root, text='Auckland (GMT +11)',
                    font=('calibri', 14, 'bold'),
                    borderwidth=5, bg='black',
                    fg='red', labelanchor=N,
                    pady=10)
frame9.grid(row=1, column=4, padx=5)
lbl9 = Label(frame9, font=('calibri', 28, 'bold'),
             bg='darkblue', fg='white')
lbl9.grid(row=1, column=4)


time()

mainloop()
