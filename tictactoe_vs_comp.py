from tkinter import *
import tkinter.messagebox

root = Tk()

root.iconbitmap('tictactoe.ico')

root.title('tic tac toe')

root.resizable(False,False)

click = True

count = 0

move = []

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
    global move
    if (click == True):
        labelPhoto = Label(root,image=xPhoto)
        labelPhoto.grid(row=r,column=c)
        if num == 1:
            btn1.set('X')
            if (move==[]):
                btn5.set('O')
            elif (move==[2]):
                btn3.set('O')
            elif (move==[3]):
                btn2.set('O')
            elif (move==[4]):
                btn7.set('O')
            elif (move==[6]):
                btn3.set('O')
            elif (move==[7]):
                btn4.set('O')
            elif (move==[8]):
                btn7.set('O')
            elif (move==[3,9])or(move==[9,3]):
                btn4.set('O')
            elif (move==[7,9])or(move==[9,7]):
                btn2.set('O')
            elif (move==[6,9])or(move==[9,6]):
                btn7.set('O')
            elif (move==[9,8])or(move==[8,9]):
                btn3.set('O')
            elif (move==[9,2])or(move==[2,9]):
                btn7.set('O')
            elif (move==[9,4])or(move==[4,9]):
                btn3.set('O')
            move=[*move,1]
            print(move)
        if num == 2:
            btn2.set('X')
            if (move==[]):
                btn5.set('O')
            elif (move==[1]):
                btn3.set('O')
            elif (move==[3]):
                btn1.set('O')
            elif (move==[9]):
                btn3.set('O')
            elif (move==[1,4])or(move==[4,1]):
                btn3.set('O')
            elif (move==[1,7])or(move==[7,1]):
                btn6.set('O')
            elif (move==[3,9])or(move==[9,3]):
                btn4.set('O')
            elif (move==[3,6])or(move==[6,3]):
                btn1.set('O')
            elif (move==[6,9])or(move==[9,6]):
                btn7.set('O')
            elif (move==[9,8])or(move==[8,9]):
                btn3.set('O')
            elif (move==[7,8])or(move==[8,7]):
                btn1.set('O')
            elif (move==[7,4])or(move==[4,7]):
                btn9.set('O')
            elif (move==[1,8])or(move==[8,1]):
                btn3.set('O')
            elif (move==[1,6])or(move==[6,1]):
                btn7.set('O')
            elif (move==[3,4])or(move==[4,3]):
                btn9.set('O')
            elif (move==[3,8])or(move==[8,3]):
                btn1.set('O')
            elif (move==[9,4])or(move==[4,9]):
                btn3.set('O')
            print(move)
            move=[*move,2]
            print(move)
            print(type(move))
        if num == 3:
            btn3.set('X')
            if (move==[]):
                btn5.set('O')
            elif (move==[1]):
                btn2.set('O')
            elif (move==[2]):
                btn1.set('O')
            elif (move==[4]):
                btn1.set('O')
            elif (move==[6]):
                btn9.set('O')
            elif move==[8]:
                btn9.set('O')
            elif (move==[9]):
                btn6.set('O')
            elif (move==[1,7])or(move==[7,1]):
                btn6.set('O')
            elif (move==[7,9])or(move==[9,7]):
                btn2.set('O')
            elif (move==[9,8])or(move==[8,9]):
                btn3.set('O')
            elif (move==[7,8])or(move==[8,7]):
                btn1.set('O')
            elif (move==[7,4])or(move==[4,7]):
                btn9.set('O')
            move=[*move,3]
        if num == 4:
            btn4.set('X')
            if (move==[]):
                btn5.set('O')
            elif (move==[1]):
                btn7.set('O')
            elif (move==[3]):
                btn1.set('O')
            elif (move==[7]):
                btn1.set('O')
            elif (move==[9]):
                btn7.set('O')
            elif (move==[1,2])or(move==[2,1]):
                btn7.set('O')
            elif (move==[1,3])or(move==[3,1]):
                btn8.set('O')
            elif (move==[7,9])or(move==[9,7]):
                btn2.set('O')
            elif (move==[2,3])or(move==[3,2]):
                btn9.set('O')
            elif (move==[3,6])or(move==[6,3]):
                btn1.set('O')
            elif (move==[6,9])or(move==[9,6]):
                btn7.set('O')
            elif (move==[9,8])or(move==[8,9]):
                btn3.set('O')
            elif (move==[7,8])or(move==[8,7]):
                btn1.set('O')
            elif (move==[1,8])or(move==[8,1]):
                btn3.set('O')
            elif (move==[1,6])or(move==[6,1]):
                btn7.set('O')
            elif (move==[3,8])or(move==[8,3]):
                btn1.set('O')
            elif (move==[9,2])or(move==[2,9]):
                btn7.set('O')
            move=[*move,4]
        if num == 5:
            btn5.set('X')
            move=num
            btn1.set('O')
        if num == 6:
            btn6.set('X')
            if move==[]:
                btn5.set('O')
            elif (move==[1]):
                btn3.set('O')
            elif move==[3]:
                btn9.set('O')
            elif move==[9]:
                btn3.set('O')
            elif (move==[1,2])or(move==[2,1]):
                btn7.set('O')
            elif (move==[1,3])or(move==[3,1]):
                btn8.set('O')
            elif (move==[1,4])or(move==[4,1]):
                btn3.set('O')
            elif (move==[1,7])or(move==[7,1]):
                btn6.set('O')
            elif (move==[7,9])or(move==[9,7]):
                btn2.set('O')
            elif (move==[2,3])or(move==[3,2]):
                btn9.set('O')
            elif (move==[9,8])or(move==[8,9]):
                btn3.set('O')
            elif (move==[7,8])or(move==[8,7]):
                btn1.set('O')
            elif (move==[7,4])or(move==[4,7]):
                btn9.set('O')
            elif (move==[1,8])or(move==[8,1]):
                btn3.set('O')
            elif (move==[3,4])or(move==[4,3]):
                btn9.set('O')
            elif (move==[3,8])or(move==[8,3]):
                btn1.set('O')
            elif (move==[9,2])or(move==[2,9]):
                btn7.set('O')
            elif (move==[9,4])or(move==[4,9]):
                btn3.set('O')
            move=[*move,6]
        if num == 7:
            btn7.set('X')
            if move==[]:
                btn5.set('O')
            elif (move==[4]):
                btn1.set('O')
            elif move==[8]:
                btn9.set('O')
            elif move==[9]:
                btn8.set('O')
            elif (move==[1,3])or(move==[3,1]):
                btn8.set('O')
            elif (move==[1]):
                btn4.set('O')
            elif (move==[3,9])or(move==[9,3]):
                btn4.set('O')
            elif (move==[2,3])or(move==[3,2]):
                btn9.set('O')
            elif (move==[3,6])or(move==[6,3]):
                btn1.set('O')
            elif (move==[3,4])or(move==[4,3]):
                btn9.set('O')
            elif (move==[3,8])or(move==[8,3]):
                btn1.set('O')
            move=[*move,7]
        if num == 8:
            btn8.set('X')
            if move==[]:
                btn5.set('O')
            elif move==[1]:
                btn7.set('O')
            elif move==[3]:
                btn9.set('O')
            elif move==[7]:
                btn9.set('O')
            elif move==[9]:
                btn7.set('O')
            elif (move==[1,2])or(move==[2,1]):
                btn7.set('O')
            elif (move==[1,4])or(move==[4,1]):
                btn3.set('O')
            elif (move==[1,7])or(move==[7,1]):
                btn6.set('O')
            elif (move==[3,9])or(move==[9,3]):
                btn4.set('O')
            elif (move==[2,3])or(move==[3,2]):
                btn9.set('O')
            elif (move==[3,6])or(move==[6,3]):
                btn1.set('O')
            elif (move==[6,9])or(move==[9,6]):
                btn7.set('O')
            elif (move==[7,4])or(move==[4,7]):
                btn9.set('O')
            elif (move==[1,6])or(move==[6,1]):
                btn7.set('O')
            elif (move==[3,4])or(move==[4,3]):
                btn9.set('O')
            elif (move==[9,2])or(move==[2,9]):
                btn7.set('O')
            elif (move==[9,4])or(move==[4,9]):
                btn3.set('O')
            move=[*move,8]
        if num == 9:
            btn9.set('X')
            if move==[]:
                btn5.set('O')
            elif (move==[2]):
                btn3.set('O')
            elif move==[3]:
                btn6.set('O')
            elif (move==[4]):
                btn7.set('O')
            elif move==[6]:
                btn3.set('O')
            elif move==[7]:
                btn8.set('O')
            elif move==[8]:
                btn7.set('O')
            elif (move==[1,2])or(move==[2,1]):
                btn7.set('O')
            elif (move==[1,4])or(move==[4,1]):
                btn3.set('O')
            elif (move==[1,3])or(move==[3,1]):
                btn8.set('O')
            elif (move==[1,7])or(move==[7,1]):
                btn6.set('O')
            elif (move==[1,8])or(move==[8,1]):
                btn3.set('O')
            elif (move==[1,6])or(move==[6,1]):
                btn7.set('O')
            move=[*move,9]
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
    global move
    move=[]
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