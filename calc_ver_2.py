###Seth Ewald
###Python Calculator Ver. 2
###03/06/2018

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

calc = tk.Tk()
calc.title('Python Calculator')
calc.minsize(150,150)
calc.maxsize(150,150)

e=tk.Entry(calc)
e.grid(row=0, column=0, columnspan=10)

#Add Buttons to calc
class calcButton:

    def __init__(self,bvalue,gRow,gCol):
        def clickact():
            e.insert(END, bvalue)
        self=tk.Button(calc, text=bvalue, width=4, command=clickact)
        self.grid(row=gRow, column=gCol, sticky='')

oneButton=calcButton('1',3,3)
twoButton = calcButton('2',3,4)
threeButton = calcButton('3',3,5)
fourButton = calcButton('4',2,3)
fiveButton = calcButton('5',2,4)
sixButton = calcButton('6',2,5)
sevenButton = calcButton('7',1,3)
eightButton = calcButton('8',1,4)
nineButton = calcButton('9',1,5)
zeroButton = calcButton('0',4,4)
decimalButton = calcButton('.',4,3)
plusButton = calcButton('+',5,0)
minusButton = calcButton('-',4,0)
divideButton = calcButton('/',2,0)
multiplyButton = calcButton('*',3,0)

def clear():
    e.delete(0,20)

def equals():
    sum=str(eval(e.get()))
    e.delete(0,10)
    e.insert(0,sum)

equalsButton = tk.Button(calc, text='=', width=4, command=equals)
equalsButton.grid(row=4, column=5)

clearButton = tk.Button(calc, text='C', width=4, command=clear)
clearButton.grid(row=1, column=0)

calc.mainloop()