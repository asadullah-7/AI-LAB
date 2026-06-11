import random
import math
import os

def clear_screen():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

board = [' ' for i in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

def check_winner(b, player):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for state in win_states:
        if all(b[i] == player for i in state):
            return True
    return False

def check_draw(b):
    return ' ' not in b

def get_moves(b):
    return [i for i in range(9) if b[i] == ' ']

def heuristics(b):
    score = 0
    lines = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for line in lines:
        x_count = sum(1 for i in line if b[i] == 'X')
        o_count = sum(1 for i in line if b[i] == 'O')

        if x_count > 0 and o_count == 0:
            score += x_count
        elif o_count > 0 and x_count == 0:
            score -= o_count
    return score

def alphaBeta(b, depth, is_max, alpha, beta, max_depth = 3):
    if check_winner(b, 'X'):
        return 10 - depth
    if check_winner(b, 'O'):
        return depth - 10
    if check_draw(b):
        return 0
    
    if depth == max_depth:
        return heuristics(b)
    
    moves = get_moves(b)

    if is_max:
        best = -math.inf

        for move in moves:
            b[move] = 'X'
            val = alphaBeta(b, depth + 1, False, alpha, beta, max_depth)
            b[move] = ' '

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best
    else:
        best = math.inf

        for move in moves:
            b[move] = 'O'
            val = alphaBeta(b, depth + 1, True, alpha, beta, max_depth)
            b[move] = ' '

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best
    

def best_move():
    moves = get_moves(board)
    best_score = -math.inf
    best_moves = []

    for move in moves:
        board[move] = 'X'
        score = alphaBeta(board, 0 , False, -math.inf, math.inf)
        board[move] = ' '

        if score > best_score:
            best_score = score
            best_move = [move]
        elif score == best_score:
            best_moves.append(move)

    return random.choices(best_moves)

def human_move():
    moves = get_moves(board)
    move = int(input("Enter the move, 1,2,3--8 etc. "))
    board[move] = 'O'
    print("Placed at ",move, " successfully\n")

def computer_move():
    move = best_move()
    board[move] = 'X'
    print("Computer chose position ", move)

human_score = 0
computer_score = 0
user_choice = 'y'
while user_choice == 'y':
    
    print("========================= WELCOME TO TIC TAC TOE GAME PLAY !!!! ====================================\n")
    print("Enter to play.") 
    clear_screen()
    if human_score == 0 or human_score > computer_score:
        human_move()
        print_board()
        if check_winner(board, 'O'):
            print("You Wins!!")
            human_score += 10
            print("Score +10!!!")
            break
        if check_draw(board):
            print("Draw!!")
    
    elif human_score < computer_score:
        computer_move()
        print_board()
        if check_winner(board, 'X'):
            print("Computer Wins!!")
            computer_score += 10
            print("Score of computer  +10!!!")
            break
        if check_draw(board):
            print("Draw!!")
    
    user_choice = input("Wana play again, press y/n ? ")

