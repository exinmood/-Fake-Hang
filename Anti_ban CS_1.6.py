#Exin_mood 

from tkinter import *

window = Tk()

window.title("Anti ban CS_1.6")
window.geometry("400x120")
window.maxsize(400,120)
window.minsize(400,120)

en = Entry(window)
en.pack(side=RIGHT)

def top():
    while 1>0 :
        top = Toplevel(window)
        top.geometry("260x80")
        top.title('')
        Label(top,text=' ↯  Successfully registered ↯ ',font = 'tahoma 15',foreground='green',
    ).pack(fill=BOTH,expand=True)
        top.minsize(260,80)
        top.maxsize(260,80)
    
btn = Button(window,text='Submit',command=top)
btn.pack(side=RIGHT,padx=20)

lab3 = Label(window,text='write ID for Counter_strike1.6 : \n (be more than ten numbers)',
             background = 'black',foreground='white')
lab3.pack(side=LEFT,fill=BOTH,expand=True)

window.mainloop()
