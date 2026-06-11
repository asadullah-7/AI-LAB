import random
import math

board = [' ' for i in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

def check_winner(b, player):
    win_states = [[0,1,2], [3,4,5], [6,7,8],
                  [0,3,6], [1,4,7], [2,5,8],
                  [0,4,8], [2,4,6]]
    
    for state in win_states:
        if all(b[i] == player for i in state):
            return True
    return False

def check_draw(b):
    return ' ' not in b

def get_moves(b):
    return [i for i in range(9) if b[i] == ' ']

def heuristic(b):
    score = 0
    lines = [[0,1,2], [3,4,5], [6,7,8],
             [0,3,6], [1,4,7], [2,5,8],
             [0,4,8], [2,4,6]]
    
    for line in lines:
        x_count = sum(1 for i in line if b[i] == 'X')
        o_count = sum(1 for i in line if b[i] == 'O')

        if x_count > 0 and o_count == 0:
            score += x_count
        if o_count > 0 and x_count == 0:
            score -= o_count

    return score

def minimax(b, depth, is_max, alpha, beta, max_depth = 3):

    if check_winner(b, 'X'):
        return 10 - depth
    if check_winner(b, 'O'):
        return depth - 10
    if check_draw(b):
        return 0
    
    if depth == max_depth:
        return heuristic(b)
    
    moves = get_moves(b)

    if is_max:
        best = -math.inf
        for move in moves:
            b[move] = 'X'
            val = minimax(b, depth+1, False, alpha, beta, max_depth)
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
            val = minimax(b, depth+1, True, alpha, beta, max_depth)
            b[move] = ' '
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best
    

def best_moves():
    moves = get_moves(board)
    best_score = -math.inf
    best_moves = []

    for move in moves:
        board[move] = 'X'
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = ' '

        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)
        
    return random.choice(best_moves)

def human_move():
    moves = get_moves(board)
    move = random.choice(moves)
    board[move] = 'O'
    print(f"Human chose postion {move}")

def computer_move():
    move = best_moves()
    board[move] = 'X'
    print(f"Computer chose position {move}")


def play_game():
    print("tic tac toe ")
    print_board()

    while True:
        computer_move()
        print_board()

        if check_winner(board, 'X'):
            print("Computer Wins!")
            break
        if check_draw(board):
            print("Draw!")
            break

        human_move()
        print_board

        if check_winner(board, 'O'):
            print("Human Wins!")
            break
        if check_draw(board):
            print("Draw!")
            break


play_game()