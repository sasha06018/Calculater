from tkinter import *

def calculate(operation):
    if operation == 'C':
        lbl['text'] = ''
    elif operation == 'DEL':
        lbl['text'] = lbl['text'][0:-1]
    elif operation == 'X^2':
        lbl['text'] = str(eval(lbl['text']) ** 2) # 2 + 2
    elif operation == '=':
        lbl['text'] = str(eval(lbl['text']))
    else:
        if lbl['text'] == '0':
            lbl['text'] = ''
        lbl['text'] = lbl['text'] + operation # '5' = '5' + '+'



root = Tk()
root.geometry('485x550')
root['bg'] = 'black'
root.title('Калькулятор')
root.resizable(False, False)
lbl = Label(text='0', font=('Consolas', 21, 'bold'), bg='black', fg='white')
lbl.place(x=11, y=50)
btns = ['C', 'DEL', '*', '=',
        '1', '2', '3', '/',
        '4', '5', '6', '+',
        '7', '8', '9', '-',
        '(', '0', ')', 'X^2'
        ]
x = 10
y = 140
for bt in btns:
    def com(x=bt):
        calculate(x)
    Button(text=bt, font=('Consolas', 15), bg='white', command=com).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 10
        y += 81
root.mainloop()