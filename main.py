from tkinter import *
from time import strftime

root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title('python-digital clock')

Label(root,text='today-time and day',font='arial 20 bold').pack(side=BOTTOM)

def time():
    string = strftime("%I:%M:%S %p "
                      " \n %A")
    mark.config(text = string)
    mark.after(1000,time)

mark = Label(root,
             font=('calibri', 40, 'bold'),
             pady=150,
             foreground='black')

mark.pack(anchor='center')
time()

mainloop()
