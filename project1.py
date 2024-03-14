
# Tic Tac Toe

def sum (a,b,c):
    return a+b+c
def printboard(Xstate,Ystate):

    zero = 'x' if Xstate[0] else ('o' if Ystate[0] else "0")
    one = 'x' if Xstate[1] else ('o' if Ystate[1] else "1")
    two = 'x' if Xstate[2] else ('o' if Ystate[2] else "2")
    three = 'x' if Xstate[3] else ('o' if Ystate[3] else "3")
    four = 'x' if Xstate[4] else ('o' if Ystate[4] else "4")
    five = 'x' if Xstate[5] else ('o' if Ystate[5] else "5")
    six = 'x' if Xstate[6] else ('o' if Ystate[6] else "6")
    seven = 'x' if Xstate[7] else ('o' if Ystate[7] else "7")
    eight= 'x' if Xstate[8] else ('o' if Ystate[8] else "8")
  
    print(f"{zero}|{one}|{two}")
    print(f"-----")
    print(f"{three}|{four}|{five}")
    print(f"-----")
    print(f"{six}|{seven}|{eight}")
def checkwin(Xstate,Ystate):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(Xstate[win[0]], Xstate[win[1]],Xstate[win[2]])== 3):
            print("x is the winner")
            return 1
        if (sum(Ystate[win[0]],Ystate[win[1]],Ystate[win[2]])== 3):
            print("o is the winner")
            return 0
    return -1

Xstate =[0,0,0,0,0,0,0,0,0]
Ystate =[0,0,0,0,0,0,0,0,0]
turn = 1 
while(True):
        printboard(Xstate,Ystate)
        if turn ==1:
            x = int(input("enter the x value = "))
            Xstate[x]=1
        else:
            
            y = int(input("enter the o value = "))
            Ystate[y]=1
        win = checkwin(Xstate,Ystate)
        if win != -1:
            break
        turn = 1-turn


