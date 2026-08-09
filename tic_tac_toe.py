board = ['1','2','3',
         '4','5','6',
         '7','8','9']

def display_board(board):
    print()
    print(board[0] , '|' ,board[1], '|' ,board[2])
    print('--+--+--')
    print(board[3] , '|' , board[4] , '|' , board[5])
    print('--+--+--')
    print(board[6] , '|' , board[7] , '|' , board[8])
    print()

def get_move(board,player):
    while True:
        move = input(f'player {player},choose a position from 1-9: ')
        if not move.isdigit():
            print('Invalid input. Please choose a number between 1-9.')
            continue
        move = int(move)
        if move<1 or move>9:
            print('Invalid input, please choose a number between 1-9.')
            continue

        position = move - 1

        if board[position] in['X', 'O']:
            print('Position already taken, please choose another position.')
            continue
        return position
def check_winner(board, player):
    winning_combination = [
        [0,1,2],
        [3,4,5],
        [6,7,8],

        [0,3,6],
        [1,4,7],
        [2,5,8],

        [0,4,8],
        [2,4,6]]
    for combination in winning_combination:
        if (board[combination[0]] == player and board[combination[1]] == player and board[combination[2]] == player):
            return True
    return False

def check_draw(board):
    for cell in board:
        if cell not in ["X", "O"]:
            return False

    return True

def play_game():

    board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]
    player = "X"

    print()
    print("======================")
    print("     TIC-TAC-TOE")
    print("======================")
    print()
    print("Player 1 = X")
    print("Player 2 = O")


    while True:
        display_board(board)
        position = get_move(board, player)
        board[position] = player

        if check_winner(board,player):
            display_board(board)
            if player == "X":
                print("Player 1 (X) wins!")
            else:
                print("Player 2 (O) wins!")
            board = [
                "1", "2", "3",
                "4", "5", "6",
                "7", "8", "9"
            ]

            player = "X"
            print("\nBoard reset! Starting a new round...\n")

            continue
            

        if check_draw(board):
            display_board(board)
            print("The game is a draw!")
            board = [
                "1", "2", "3",
                "4", "5", "6",
                "7", "8", "9"
            ]

            player = "X"
            print("\nBoard reset! Starting a new round...\n")

            continue

        if player == "X":
            player = "O"
        else:   
            player = "X"

while True:

    play_game()

    while True:

        again = input("Would you like to play again? (yes/no): ").lower()

        if again == "yes":
            print("\nStarting a new game...")
            break

        elif again == "no":
            print("\nThanks for playing!")
            break

        else:
            print("Please enter 'yes' or 'no'.")
    if again == "no":
        break
