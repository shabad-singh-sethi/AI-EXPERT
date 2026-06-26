import random 
import colorama 
from colorama import Fore , Style , init
init(autoreset=True )

def display_board(board):
    print()
    def colored(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.CYAN + cell +   Style.RESET_ALL
        
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X','O']:
        symbol = input(Fore.GREEN + "DO YOU WANT TO BE X OR O ?" + Style.RESET_ALL).upper()

        if symbol == "X":
            return ('X','O')
        
        else:
            return ('O','X')
        
def player_move(board , symbol):
    move = -1
    while move not in range(1,10) or not board[move -1 ].isdigit():
        try:
            move = int(input("PLEASE ENTER A MOVE BETWEEN 1-9: "))
            if move not in range(1,10) or not board[move -1 ].isdigit():
                print("INVALID MOVE PLEASE ENTER NUMBERS BETWEEN 1-9")

        
        except ValueError:
            print("PLEASE ENETR 1-9")
    board[move -1] = symbol


def ai_move(board , ai_symbol , player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
        

