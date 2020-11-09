from tkinter import *
from tkinter import filedialog


root = Tk()
root.geometry('400x400')
root.title('Notepad')

notepad = Text(root, width=48, height=20).grid(row=1, column=0)

def save():
    root.filename = filedialog.asksaveasfilename(
                        initialdir=r'Text Editor\Saved Files',
                        title='Save',
                        filetypes=(('*.txt', 'Text Files'),
                                   ('*.*', 'All Files'))
                        )
    lbl = Label(root, font=8, text=root.filename,
                justify=LEFT).grid(row=0, column=0)
    filedialog.SaveAs(root)


btn = Button(root, text='Save', font=12, command=save).grid(row=2, column=0)


mainloop()
