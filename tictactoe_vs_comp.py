from tkinter import *
import tkinter.messagebox

root = Tk()

root.iconbitmap('tictactoe.ico')

root.title('tic tac toe')

root.resizable(False,False)

click = True

count = 0

Xmove = []
Omove = []
move_all = []

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()
btn10 = StringVar()

xPhoto = PhotoImage(file='X.png')
oPhoto = PhotoImage(file='O.png')

def play():
    button1 = Button(root,height=9,width=19,bd=0.95,relief='ridge',bg='#ffcc99',textvariable=btn1,command=lambda:press(1,0,0))
    button2 = Button(root,height=9,width=19,bd=0.95,relief='ridge',bg='#ffcc99',textvariable=btn2,command=lambda:press(2,0,1))
    button3 = Button(root,height=9,width=19,bd=0.95,relief='ridge',bg='#ffcc99',textvariable=btn3,command=lambda:press(3,0,2))
    button4 = Button(root,height=9,width=19,bd=0.95,relief='ridge',bg='#ffcc66',textvariable=btn4,command=lambda:press(4,1,0))
    button5 = Button(root,height=9,width=19,bd=0.95,relief='ridge',bg='#ffcc66',textvariable=btn5,command=lambda:press(5,1,1))
    button6 = Button(root,height=9,width=19,bd=0.95,relief='ridge',bg='#ffcc66',textvariable=btn6,command=lambda:press(6,1,2))
    button7 = Button(root,height=9,width=19,bd=0.95,relief='ridge',bg='#ffcc33',textvariable=btn7,command=lambda:press(7,2,0))
    button8 = Button(root,height=9,width=19,bd=0.95,relief='ridge',bg='#ffcc33',textvariable=btn8,command=lambda:press(8,2,1))
    button9 = Button(root,height=9,width=19,bd=0.95,relief='ridge',bg='#ffcc33',textvariable=btn9,command=lambda:press(9,2,2))
    
    button1.grid(row=0,column=0)
    button2.grid(row=0,column=1)
    button3.grid(row=0,column=2)
    button4.grid(row=1,column=0)
    button5.grid(row=1,column=1)
    button6.grid(row=1,column=2)
    button7.grid(row=2,column=0)
    button8.grid(row=2,column=1)
    button9.grid(row=2,column=2)

def press(num,r,c):
    global click,count
    global Xmove, Omove, move_all
    if (click == True):
        labelPhoto = Label(root,image=xPhoto)
        labelPhoto.grid(row=r,column=c)
        if num == 1:
            btn1.set('X')
            if (Xmove==[]):
                btn5.set('O')
            elif (Xmove==[2]):
                btn3.set('O')
            elif (Xmove==[3]):
                btn2.set('O')
            elif (Xmove==[4]):
                btn7.set('O')
            elif (Xmove==[6]):
                btn3.set('O')
            elif (Xmove==[7]):
                btn4.set('O')
            elif (Xmove==[8]):
                btn7.set('O')
            elif (Xmove==[9]):
                btn4.set('O')
            elif (Xmove==[3,9])or(Xmove==[9,3]):
                btn4.set('O')
            elif (Xmove==[7,9])or(Xmove==[9,7]):
                btn2.set('O')
            elif (Xmove==[6,9])or(Xmove==[9,6]):
                btn7.set('O')
            elif (Xmove==[9,8])or(Xmove==[8,9]):
                btn3.set('O')
            elif (Xmove==[9,2])or(Xmove==[2,9]):
                btn7.set('O')
            elif (Xmove==[9,4])or(Xmove==[4,9]):
                btn3.set('O')
            elif (Xmove==[2,6])or(Xmove==[6,2]):
                btn7.set('O')
            elif (Xmove==[4,8])or(Xmove==[8,4]):
                btn3.set('O')
            elif (Xmove==[3,7])or(Xmove==[7,3]):
                btn4.set('O')
            #two moves wins above this
            Xmove=[*Xmove,1]
            print(Xmove)
        if num == 2:
            btn2.set('X')
            if (Xmove==[]):
                btn5.set('O')
            elif (Xmove==[1]):
                btn3.set('O')
            elif (Xmove==[3]):
                btn1.set('O')
            elif (Xmove==[6]):
                btn3.set('O')
            elif (Xmove==[4]):
                btn1.set('O')
            elif (Xmove==[7]):
                btn1.set('O')
            elif (Xmove==[8]):
                btn1.set('O')
            elif (Xmove==[9]):
                btn3.set('O')
            elif (Xmove==[1,4])or(Xmove==[4,1]):
                btn3.set('O')
            elif (Xmove==[1,7])or(Xmove==[7,1]):
                btn6.set('O')
            elif (Xmove==[3,9])or(Xmove==[9,3]):
                btn4.set('O')
            elif (Xmove==[3,6])or(Xmove==[6,3]):
                btn1.set('O')
            elif (Xmove==[6,9])or(Xmove==[9,6]):
                btn7.set('O')
            elif (Xmove==[9,8])or(Xmove==[8,9]):
                btn3.set('O')
            elif (Xmove==[7,8])or(Xmove==[8,7]):
                btn1.set('O')
            elif (Xmove==[7,4])or(Xmove==[4,7]):
                btn9.set('O')
            elif (Xmove==[1,8])or(Xmove==[8,1]):
                btn3.set('O')
            elif (Xmove==[1,6])or(Xmove==[6,1]):
                btn7.set('O')
            elif (Xmove==[3,4])or(Xmove==[4,3]):
                btn9.set('O')
            elif (Xmove==[3,8])or(Xmove==[8,3]):
                btn1.set('O')
            elif (Xmove==[9,4])or(Xmove==[4,9]):
                btn3.set('O')
            elif (Xmove==[9,4])or(Xmove==[4,9]):
                btn3.set('O')
            elif (Xmove==[7,6])or(Xmove==[6,7]):
                btn1.set('O')
            elif (Xmove==[8,6])or(Xmove==[6,8]):
                btn1.set('O')
            elif (Xmove==[4,8])or(Xmove==[8,4]):
                btn3.set('O')
            elif (Xmove==[1,9])or(Xmove==[9,1]):
                btn6.set('O')
            elif (Xmove==[3,7])or(Xmove==[7,3]):
                btn4.set('O')
            elif (Xmove==[4,6])or(Xmove==[6,4]):
                btn9.set('O')
            #two moves wins above this
            Xmove=[*Xmove,2]
            print(Xmove)
            print(type(Xmove))
        if num == 3:
            btn3.set('X')
            if (Xmove==[]):
                btn5.set('O')
            elif (Xmove==[1]):
                btn2.set('O')
            elif (Xmove==[2]):
                btn1.set('O')
            elif (Xmove==[4]):
                btn1.set('O')
            elif (Xmove==[6]):
                btn9.set('O')
            elif (Xmove==[7]):
                btn6.set('O')
            elif Xmove==[8]:
                btn9.set('O')
            elif (Xmove==[9]):
                btn6.set('O')
            elif (Xmove==[1,7])or(Xmove==[7,1]):
                btn6.set('O')
            elif (Xmove==[7,9])or(Xmove==[9,7]):
                btn2.set('O')
            elif (Xmove==[9,8])or(Xmove==[8,9]):
                btn3.set('O')
            elif (Xmove==[7,8])or(Xmove==[8,7]):
                btn1.set('O')
            elif (Xmove==[7,4])or(Xmove==[4,7]):
                btn9.set('O')
            elif (Xmove==[7,6])or(Xmove==[6,7]):
                btn1.set('O')
            elif (Xmove==[7,2])or(Xmove==[2,7]):
                btn9.set('O')
            elif (Xmove==[2,4])or(Xmove==[4,2]):
                btn9.set('O')
            elif (Xmove==[8,6])or(Xmove==[6,8]):
                btn1.set('O')
            elif (Xmove==[1,9])or(Xmove==[9,1]):
                btn6.set('O')
            elif (Xmove==[2,8])or(Xmove==[8,2]):
                btn9.set('O')
            elif (Xmove==[4,6])or(Xmove==[6,4]):
                btn9.set('O')
            #two moves wins above this
            Xmove=[*Xmove,3]
        if num == 4:
            btn4.set('X')
            if (Xmove==[]):
                btn5.set('O')
            elif (Xmove==[1]):
                btn7.set('O')
            elif (Xmove==[2]):
                btn1.set('O')
            elif (Xmove==[3]):
                btn1.set('O')
            elif (Xmove==[6]):
                btn1.set('O')
            elif (Xmove==[7]):
                btn1.set('O')
            elif (Xmove==[8]):
                btn7.set('O')
            elif (Xmove==[9]):
                btn7.set('O')
            elif (Xmove==[1,2])or(Xmove==[2,1]):
                btn7.set('O')
            elif (Xmove==[1,3])or(Xmove==[3,1]):
                btn8.set('O')
            elif (Xmove==[7,9])or(Xmove==[9,7]):
                btn2.set('O')
            elif (Xmove==[2,3])or(Xmove==[3,2]):
                btn9.set('O')
            elif (Xmove==[3,6])or(Xmove==[6,3]):
                btn1.set('O')
            elif (Xmove==[6,9])or(Xmove==[9,6]):
                btn7.set('O')
            elif (Xmove==[9,8])or(Xmove==[8,9]):
                btn3.set('O')
            elif (Xmove==[7,8])or(Xmove==[8,7]):
                btn1.set('O')
            elif (Xmove==[1,8])or(Xmove==[8,1]):
                btn3.set('O')
            elif (Xmove==[1,6])or(Xmove==[6,1]):
                btn7.set('O')
            elif (Xmove==[3,8])or(Xmove==[8,3]):
                btn1.set('O')
            elif (Xmove==[9,2])or(Xmove==[2,9]):
                btn7.set('O')
            elif (Xmove==[7,6])or(Xmove==[6,7]):
                btn1.set('O')
            elif (Xmove==[7,2])or(Xmove==[2,7]):
                btn9.set('O')
            elif (Xmove==[2,6])or(Xmove==[6,2]):
                btn7.set('O')
            elif (Xmove==[8,6])or(Xmove==[6,8]):
                btn1.set('O')
            elif (Xmove==[2,8])or(Xmove==[8,2]):
                btn9.set('O')
            #two moves wins above this
            Xmove=[*Xmove,4]
        if num == 5:
            btn5.set('X')
            Xmove=num
            btn1.set('O')
        if num == 6:
            btn6.set('X')
            if Xmove==[]:
                btn5.set('O')
            elif (Xmove==[1]):
                btn3.set('O')
            elif (Xmove==[2]):
                btn3.set('O')
            elif Xmove==[3]:
                btn9.set('O')
            elif (Xmove==[4]):
                btn1.set('O')
            elif Xmove==[7]:
                btn9.set('O')
            elif Xmove==[8]:
                btn9.set('O')
            elif Xmove==[9]:
                btn3.set('O')
            elif (Xmove==[1,2])or(Xmove==[2,1]):
                btn7.set('O')
            elif (Xmove==[1,3])or(Xmove==[3,1]):
                btn8.set('O')
            elif (Xmove==[1,4])or(Xmove==[4,1]):
                btn3.set('O')
            elif (Xmove==[1,7])or(Xmove==[7,1]):
                btn6.set('O')
            elif (Xmove==[7,9])or(Xmove==[9,7]):
                btn2.set('O')
            elif (Xmove==[2,3])or(Xmove==[3,2]):
                btn9.set('O')
            elif (Xmove==[9,8])or(Xmove==[8,9]):
                btn3.set('O')
            elif (Xmove==[7,8])or(Xmove==[8,7]):
                btn1.set('O')
            elif (Xmove==[7,4])or(Xmove==[4,7]):
                btn9.set('O')
            elif (Xmove==[1,8])or(Xmove==[8,1]):
                btn3.set('O')
            elif (Xmove==[3,4])or(Xmove==[4,3]):
                btn9.set('O')
            elif (Xmove==[3,8])or(Xmove==[8,3]):
                btn1.set('O')
            elif (Xmove==[9,2])or(Xmove==[2,9]):
                btn7.set('O')
            elif (Xmove==[9,4])or(Xmove==[4,9]):
                btn3.set('O')
            elif (Xmove==[7,2])or(Xmove==[2,7]):
                btn9.set('O')
            elif (Xmove==[2,4])or(Xmove==[4,2]):
                btn9.set('O')
            elif (Xmove==[4,8])or(Xmove==[8,4]):
                btn3.set('O')
            elif (Xmove==[2,8])or(Xmove==[8,2]):
                btn9.set('O')
            #two moves wins above this
            Xmove=[*Xmove,6]
        if num == 7:
            btn7.set('X')
            if Xmove==[]:
                btn5.set('O')
            elif (Xmove==[1]):
                btn4.set('O')
            elif (Xmove==[2]):
                btn1.set('O')
            elif (Xmove==[3]):
                btn6.set('O')
            elif (Xmove==[4]):
                btn1.set('O')
            elif Xmove==[6]:
                btn9.set('O')
            elif Xmove==[8]:
                btn9.set('O')
            elif Xmove==[9]:
                btn8.set('O')
            elif (Xmove==[1,3])or(Xmove==[3,1]):
                btn8.set('O')
            elif (Xmove==[3,9])or(Xmove==[9,3]):
                btn4.set('O')
            elif (Xmove==[2,3])or(Xmove==[3,2]):
                btn9.set('O')
            elif (Xmove==[3,6])or(Xmove==[6,3]):
                btn1.set('O')
            elif (Xmove==[3,4])or(Xmove==[4,3]):
                btn9.set('O')
            elif (Xmove==[3,8])or(Xmove==[8,3]):
                btn1.set('O')
            elif (Xmove==[2,4])or(Xmove==[4,2]):
                btn9.set('O')
            elif (Xmove==[8,6])or(Xmove==[6,8]):
                btn1.set('O')
            elif (Xmove==[1,9])or(Xmove==[9,1]):
                btn6.set('O')
            elif (Xmove==[2,8])or(Xmove==[8,2]):
                btn9.set('O')
            elif (Xmove==[4,6])or(Xmove==[6,4]):
                btn9.set('O')
            #two moves wins above this
            Xmove=[*Xmove,7]
        if num == 8:
            btn8.set('X')
            if Xmove==[]:
                btn5.set('O')
            elif Xmove==[1]:
                btn7.set('O')
            elif (Xmove==[2]):
                btn1.set('O')
            elif Xmove==[3]:
                btn9.set('O')
            elif Xmove==[6]:
                btn9.set('O')
            elif Xmove==[7]:
                btn9.set('O')
            elif (Xmove==[4]):
                btn7.set('O')
            elif Xmove==[9]:
                btn7.set('O')
            elif (Xmove==[1,2])or(Xmove==[2,1]):
                btn7.set('O')
            elif (Xmove==[1,4])or(Xmove==[4,1]):
                btn3.set('O')
            elif (Xmove==[1,7])or(Xmove==[7,1]):
                btn6.set('O')
            elif (Xmove==[3,9])or(Xmove==[9,3]):
                btn4.set('O')
            elif (Xmove==[2,3])or(Xmove==[3,2]):
                btn9.set('O')
            elif (Xmove==[3,6])or(Xmove==[6,3]):
                btn1.set('O')
            elif (Xmove==[6,9])or(Xmove==[9,6]):
                btn7.set('O')
            elif (Xmove==[7,4])or(Xmove==[4,7]):
                btn9.set('O')
            elif (Xmove==[1,6])or(Xmove==[6,1]):
                btn7.set('O')
            elif (Xmove==[3,4])or(Xmove==[4,3]):
                btn9.set('O')
            elif (Xmove==[9,2])or(Xmove==[2,9]):
                btn7.set('O')
            elif (Xmove==[9,4])or(Xmove==[4,9]):
                btn3.set('O')
            elif (Xmove==[7,6])or(Xmove==[6,7]):
                btn1.set('O')
            elif (Xmove==[7,2])or(Xmove==[2,7]):
                btn9.set('O')
            elif (Xmove==[2,4])or(Xmove==[4,2]):
                btn9.set('O')
            elif (Xmove==[2,6])or(Xmove==[6,2]):
                btn7.set('O')
            elif (Xmove==[1,9])or(Xmove==[9,1]):
                btn6.set('O')
            elif (Xmove==[3,7])or(Xmove==[7,3]):
                btn4.set('O')
            elif (Xmove==[4,6])or(Xmove==[6,4]):
                btn9.set('O')
            #two moves wins above this
            Xmove=[*Xmove,8]
        if num == 9:
            btn9.set('X')
            if Xmove==[]:
                btn5.set('O')
            elif (Xmove==[1]):
                btn4.set('O')
            elif (Xmove==[2]):
                btn3.set('O')
            elif Xmove==[3]:
                btn6.set('O')
            elif (Xmove==[4]):
                btn7.set('O')
            elif Xmove==[6]:
                btn3.set('O')
            elif Xmove==[7]:
                btn8.set('O')
            elif Xmove==[8]:
                btn7.set('O')
            elif (Xmove==[1,2])or(Xmove==[2,1]):
                btn7.set('O')
            elif (Xmove==[1,4])or(Xmove==[4,1]):
                btn3.set('O')
            elif (Xmove==[1,3])or(Xmove==[3,1]):
                btn8.set('O')
            elif (Xmove==[1,7])or(Xmove==[7,1]):
                btn6.set('O')
            elif (Xmove==[1,8])or(Xmove==[8,1]):
                btn3.set('O')
            elif (Xmove==[1,6])or(Xmove==[6,1]):
                btn7.set('O')
            elif (Xmove==[2,6])or(Xmove==[6,2]):
                btn7.set('O')
            elif (Xmove==[4,8])or(Xmove==[8,4]):
                btn3.set('O')
            elif (Xmove==[3,7])or(Xmove==[7,3]):
                btn4.set('O')
            #two moves wins above this
            Xmove=[*Xmove,9]
        count+=1
        #click = False
        checkWin()
    elif(click == False):
        labelPhoto = Label(root,image=oPhoto)
        labelPhoto.grid(row=r,column=c)
        if num == 1:
            (btn5.set('O'))
        if num == 2:
            (btn2.set('O'))
        if num == 3:
            (btn3.set('O'))
        if num == 4:
            (btn4.set('O'))
        if num == 5:
            (btn5.set('O'))
        if num == 6:
            (btn6.set('O'))
        if num == 7:
            (btn7.set('O'))
        if num == 8:
            (btn8.set('O'))
        if num == 9:
            (btn9.set('O'))
        count+=1
        click = True
        checkWin()
        
def checkWin():
    global click, count
    if (btn1.get() == 'X' and btn2.get() == 'X' and btn3.get() == 'X' or
        btn4.get() == 'X' and btn5.get() == 'X' and btn6.get() == 'X' or
        btn7.get() == 'X' and btn8.get() == 'X' and btn9.get() == 'X' or
        btn1.get() == 'X' and btn4.get() == 'X' and btn7.get() == 'X' or
        btn2.get() == 'X' and btn5.get() == 'X' and btn8.get() == 'X' or
        btn3.get() == 'X' and btn6.get() == 'X' and btn9.get() == 'X' or
        btn1.get() == 'X' and btn5.get() == 'X' and btn9.get() == 'X' or
        btn3.get() == 'X' and btn5.get() == 'X' and btn7.get() == 'X'):
        tkinter.messagebox.showinfo('tic tac toe','X WINS!')
        click = True
        count =  0
        clear()
        play()
    
    elif (btn1.get() == 'O' and btn2.get() == 'O' and btn3.get() == 'O' or
          btn4.get() == 'O' and btn5.get() == 'O' and btn6.get() == 'O' or
          btn7.get() == 'O' and btn8.get() == 'O' and btn9.get() == 'O' or
          btn1.get() == 'O' and btn4.get() == 'O' and btn7.get() == 'O' or
          btn2.get() == 'O' and btn5.get() == 'O' and btn8.get() == 'O' or
          btn3.get() == 'O' and btn6.get() == 'O' and btn9.get() == 'O' or
          btn1.get() == 'O' and btn5.get() == 'O' and btn9.get() == 'O' or
          btn3.get() == 'O' and btn5.get() == 'O' and btn7.get() == 'O'):
        tkinter.messagebox.showinfo('tic tac toe','O WINS!')
        click = True
        count =  0
        clear()
        play()
    
    elif(count==9):
        tkinter.messagebox.showinfo('tic tac toe','ITS A DRAW!')
        count =  0
        clear()
        play()

def clear():
    global Xmove
    Xmove=[]
    btn1.set("")
    btn2.set("")
    btn3.set("")
    btn4.set("")
    btn5.set("")
    btn6.set("")
    btn7.set("")
    btn8.set("")
    btn9.set("")
    
play()
    
root.mainloop()
