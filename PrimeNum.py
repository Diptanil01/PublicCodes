import math
import _tkinter
from tkinter import Tk,ttk,IntVar,messagebox
def isprime(num:int):
    '''a func to find whether num is prime or not'''
    if num==1 or num==0 or num==-1:
        return None
    else:
        if num<0:
            num=-num
        prime=True
        t=math.sqrt(num)
        t=int((str(t).split('.'))[0])
        Available_Nums=[i for i in range(t+1)]
        for number in Available_Nums:
            if number==0:
                pass
            elif  math.remainder(num,number)==0 and number!=1 :
                prime=False
                break
        return  prime

def checkout():
    try:
        result.configure(text="Is it Prime? : "+str(isprime(var.get())))
    except _tkinter.TclError:
        result.configure(text="Is it Prime? : "+'StringValErr!')
        messagebox.showerror('Error in Input','Expected Float...Got String')
        var.set(value=0)
        result.configure(text="Is it Prime? : "+'None')

root=Tk()
root.title('IsPrime')
root.minsize(400,80)
root.maxsize(400,80)
root.title('IsPrime')
f1=ttk.Frame()
var=IntVar(value=0)
ttk.Label(f1,text='Enter the Number: ',font='Arial 11 bold').pack(side='left',anchor='n')
ttk.Entry(f1,textvariable=var,font='Arial 11 bold').pack(side='left',anchor='n')
ttk.Button(f1,text='CHECK!',command=checkout).pack()
ttk.Label(f1,text='©Diptanil',font='Arial 7 ').pack(side='left',anchor='n')
ttk.Label(root,text="returns None for 0,1 or -1/'True' for Prime/else 'False'",font='Arial 8').pack()
f1.pack()
result=ttk.Label(text="Is it Prime? : None",font='Arial 12')
result.pack()
root.mainloop()