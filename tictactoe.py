
def print_TICTACTOE(xState,oState):
    index0='X' if xState[0] else("O" if oState[0] else 0)
    index1='X' if xState[1] else("O" if oState[1] else 1)
    index2='X' if xState[2] else("O" if oState[2] else 2)
    index3='X' if xState[3] else("O" if oState[3] else 3)
    index4='X' if xState[4] else("O" if oState[4] else 4)
    index5='X' if xState[5] else("O" if oState[5] else 5)
    index6='X' if xState[6] else("O" if oState[6] else 6)
    index7='X' if xState[7] else("O" if oState[7] else 7)
    index8='X' if xState[8] else("O" if oState[8] else 8)
    print(f"-----------")
    print(f"{index0} | {index1} | {index2}")
    print(f"--|---|----")
    print(f"{index3} | {index4} | {index5}")
    print(f"--|---|----")
    print(f"{index6} | {index7} | {index8}")
    print(f"-----------")

def sum(x,y,z):
    return x+y+z


def tie(x,o):
    return all(x[i] == 1 or o[i] == 1 for i in range(9))

def winner(xState,oState):
    xWIN=[[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
    oWIN=[[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]

    for i in xWIN:
        if sum(xState[i[0]],xState[i[1]],xState[i[2]])==3:
            print("X WON!!! ;)")
            return 1
        if sum(oState[i[0]],oState[i[1]],oState[i[2]])==3:
            print("O WON!!! ;)")
            return 0


    return -1




def statesAndTurns():
    x=[0,0,0,0,0,0,0,0,0]
    o=[0,0,0,0,0,0,0,0,0]
    turn=1
    while(True):

        print_TICTACTOE(x,o)
        last=None
        if turn==1:
            print("X Turn")
            value=int(input("Enter the board position: "))
            if value < 0 or value > 8:
                print("Please enter a number between 0 and 8.")
                continue
            if x[value]!=1 and o[value]!=1:
                x[value]=1
                last=value
            else:
                print("Already taken--Choose another one")
                continue
        else:
            print("O Turn")
            value = int(input("Enter the board position: "))
            if x[value] != 1 and o[value] != 1:
             o[value] = 1
             last=value
            else:
                print("Already taken--Choose another one")
                continue
        temp=winner(x,o)
        if temp!=-1:

            print_TICTACTOE(x,o)
            print("--Match Over--")
            break
        elif tie(x,o) and temp!=-1:

            print("TIE!!! :(")
            print_TICTACTOE(x,o)
            print("--Match Over--")
            break
        turn=int(not(turn))






print("----TIC TAC TOE----\n")
#print_TICTACTOE()
statesAndTurns()