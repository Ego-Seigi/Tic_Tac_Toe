'''
A game of Tic-Tac-Toe
in a 3x3 grid format
'''

from tkinter import *


# class AI to define the play of the system

class AI:

    def __init__(self):
        self.var= "Hi it's Cortana"

    def winmove(self):

        flag = False
        
        for i in range(3):
            for j in range(3):
                if btns[i][j]['text'] == '':
                    btns[i][j]['text'] = s['Cortana']
                    if winner('#F0F0F0') is False:
                        btns[i][j]['text'] = ''
                        flag = False
                    else:
                        flag = True
                        break
            if flag:
                break

        if flag:
            return True

        for i in range(3):
            for j in range(3):
                if btns[i][j]['text'] == '':
                    btns[i][j]['text'] = s[player]
                    if winner('#F0F0F0') is True:
                        btns[i][j]['text'] = s['Cortana']
                        flag = True
                        break
                    else:
                        btns[i][j]['text'] = ''
                        flag = False
            if flag:
                break

        if flag:
            return True
        else:
            return False
                

    def bestmove(self):

        flag = False

        for i in range(3):
            
            if btns[i][i]['text'] == '':
                btns[i][i]['text'] = s['Cortana']
                break
                
            elif btns[i][2-i]['text'] == '':
                btns[i][2-i]['text'] = s['Cortana']
                break

            else:
                for j in range(3):
                    if btns[i][j]['text'] == '':
                        btns[i][j]['text'] = s['Cortana']
                        flag = True
                        break
                if flag == True:
                    break
                    
            
    def move(self):

        if self.winmove() == False:
            self.bestmove()



def play(row, column):

    global active_player
    global btns
    
    if btns[row][column]['text'] == '':

        if winner('#F0F0F0') is False:

            btns[row][column]['text'] = s[active_player]
       
        if winner('#F0F0F0') is False:
                
            active_player = 'Cortana'
            label.config(text=active_player+"'s turn \n"+s[active_player])

            obj = AI()
            win.after(1, obj.move())                      
            
                            
        if winner('#F0F0F0') is True:
            if active_player == player:
                winner('green')
                label.config(text='You win!')
            else:
                winner('red')
                label.config(text='Cortana wins!')
                
        elif winner('#F0F0F0') == 'DRAW':
            winner('yellow')
            label.config(text=('Draw'))

        else:
            active_player = player                
            label.config(text=active_player+" turn \n"+s[active_player])


def winner(color):
    
    for row in range(3):
        if btns[row][0]['text'] == btns[row][1]['text'] == btns[row][2]['text'] != "":
            btns[row][0].config(bg=color)
            btns[row][1].config(bg=color)
            btns[row][2].config(bg=color)
            return True

    for column in range(3):
        if btns[0][column]['text'] == btns[1][column]['text'] == btns[2][column]['text'] != "":
            btns[0][column].config(bg=color)
            btns[1][column].config(bg=color)
            btns[2][column].config(bg=color)
            return True

    if btns[0][0]['text'] == btns[1][1]['text'] == btns[2][2]['text'] != "":
        btns[0][0].config(bg=color)
        btns[1][1].config(bg=color)
        btns[2][2].config(bg=color)
        return True

    elif btns[0][2]['text'] == btns[1][1]['text'] == btns[2][0]['text'] != "":
        btns[0][2].config(bg=color)
        btns[1][1].config(bg=color)
        btns[2][0].config(bg=color)
        return True

    elif blanks() is False:

        for row in range(3):
            for column in range(3):
                btns[row][column].config(bg=color)
        return "DRAW"

    else:
        return False
        
   
def blanks():

    blank = 0
    
    for row in range(0,3):
        for column in range(0,3):
            if btns[row][column]['text'] == '':
                blank += 1 
    if blank == 0:
        return False
    else:
        return True


def reset():

    global active_player

    active_player = player

    for i in range(0,3):
            for j in range(0,3):
                btns[i][j].config(text='', bg='#F0F0F0')

    label.config(text=active_player+" turn")



def select(ch):

    global player
    
    s[player] = ch
    
    if ch == 'X':
        s['Cortana'] = 'O'
    else:
        s['Cortana'] = 'X'
    


#main window

def main():

    mainframe.destroy()
    
    heading.config(text='Tic-Tac-Toe', font=('calibri', 30))
    heading.pack()
                
    for row in range(0,3):
        for column in range(0,3):
            btns[row][column].config(text='', font=('arial', 10), width=5, height=2, command= lambda r=row, c=column: play(r, c))
            btns[row][column].grid(row=row, column=column)


    label.config(text=active_player+" turn",  fg='red', font=('vivaldi', 25))
    label.pack(side=TOP, pady=20)

    reset_btn.config(text='Exit', font=10, command=win.destroy)
    reset_btn.pack(side=BOTTOM, pady = 20)

    reset_btn.config(text='Reset', font=10, command=reset)
    reset_btn.pack(side=BOTTOM)
    


# Initializing variables

s = {}
player = 'Your'
active_player = player

btns = [[0,0,0],
        [0,0,0],
        [0,0,0]]



# Main body

win = Tk()
win.title('Tic-Tac-Toe')
win.geometry('500x500+500+100')


# Intro window

mainframe = Frame(win)
mainframe.pack(pady=20)

msg1 = Label(mainframe, text="Hi! I am Cortana. \nWanna play Tic-Tac-Toe with me?\n\n", font=10)
msg1.grid(row=0, column=0)

msg2 = Label(mainframe, text='Enter your choice: ', font=10)
msg2.grid(row=1, column=0)

box = Frame(mainframe)
box.grid(row=2, column=0)

symbol = [0,0]
symbol[0] = Button(box, text='X', font=('arial', 20), width=5, height=2, command=lambda s='X': select(s))
symbol[0].grid(row=0, column=0)
symbol[1] = Button(box, text='O', font=('arial', 20), width=5, height=2, command=lambda s='O': select(s))
symbol[1].grid(row=0, column=1)

spacey = Label(mainframe, text='', font=10)
spacey.grid(row=3, column=0)

done = Button(mainframe, text = 'Done', font=('calibri body', 20), command=main)
done.grid(row=4, column=0)


# blueprint of main window 

heading = Label(win)
heading.pack()

frame = Frame(win)
frame.pack(pady=20)
                
for row in range(0,3):
    for column in range(0,3):
        btns[row][column] = Button(frame)
        
label = Label(win)

reset_btn = Button(win)

reset_btn = Button(win)

 

win.mainloop()


