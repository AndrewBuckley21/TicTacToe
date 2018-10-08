
def displayBoard(board):
    count = 1
    for i in range(3):
        for n in range(3):
            print(end="| ")
            if board[(i * 3) + n] == "_":
                print(count, end=" | ")
            else:
                print(board[(i * 3) + n], end=" | ")
            count += 1
        print()


def filled(board):
    if "_" in board:
        return False
    else:
        return True


def makeMove(board, x, token):
    if board[x - 1] == 'X' or board[x - 1] == 'O':
        print("That position is filled! Try again!")
        return False
    else:
        board[x - 1] = token
        return True


def winner(board, char):
    p1 = board[0] + board[1] + board[2]
    p2 = board[3] + board[4] + board[5]
    p3 = board[6] + board[7] + board[8]
    p4 = board[0] + board[3] + board[6]
    p5 = board[1] + board[4] + board[7]
    p6 = board[2] + board[5] + board[8]
    p7 = board[0] + board[4] + board[8]
    p8 = board[2] + board[4] + board[6]
    win = char + char + char
    if win == p1 or win == p2 or win == p3 or win == p4 or win == p5 or win == p6 or win == p7 or win == p8:
        return True
    else:
        return False

def main():
    print("Play Tic-Tac-Toe!")
    board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    token = 'X'
    gameOver = False
    while not gameOver:
        displayBoard(board)
        move = int(input("Enter a move for " + token + " (1-9): "))
        print()
        if (move < 1) or (move > 9):
            print("Move is out of range; try again.")
        else:
            if makeMove(board, move, token):
                if winner(board, token):
                    print(token + " wins!")
                    gameOver = True
                else:
                    if filled(board):
                        print("Board is full! No winner!")
                        gameOver = True
                    else:
                        if token == 'X':
                            token = 'O'
                        else:
                            token = 'X'
    displayBoard(board)

if __name__ == "__main__":
    main()


