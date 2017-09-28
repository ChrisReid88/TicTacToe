#Storing the board selections in a list
board = [0,1,2,3,4,5,6,7,8]

#Displaying the board
def display():
    print " ",board[0],"|",board[1],'|',board[2]
    print " -----------"
    print " ",board[3],"|",board[4],'|',board[5]
    print " -----------"
    print " ",board[6],"|",board[7],'|',board[8]

#Empty lists to store players selections
xs = []
os = []

#All possible winning combinations
win = [[0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8]]

#First player/X's turn
def xTurn():
    x = raw_input("Player X choose a number: ")
    while len(x) != 1 or (not x.isdigit()):
        print "Not a valid choice."
        x = raw_input("Player X choose a number: ")
    x = int(x)

    if board[x] != 'x' and board[x] != 'o':
        board[x] = 'x'
        xs.append(x)
        xs.sort()
    else:
        print "This is not a valid choice. Please choose another"
        xTurn()
 

def oTurn():
    o = raw_input("Player O choose a number: ")
    while len(o) != 1 or (not o.isdigit()):
        print "Not a valid choice."
        o = raw_input("Player O choose a number: ")
    o = int(o)

    if board[o] != 'x' and board[o] != 'o':
        board[o] = 'o'
        os.append(o)
        os.sort()
    else:
        print "This is not a valid choice. Please choose another"
        oTurn()

def winner():
    if xs in win:
        print "X's Wins!!!"
        quit()
    if os in win:
        print "O's Win!!!"
        quit()

display()

while True:
    xTurn()
    winner()
    display()
    oTurn()
    winner()
    display()
