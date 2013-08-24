import sys
import numpy as np

def split_payoffs(payoff_matrix_rows, matrix_dim):
    playerA = []
    playerB = []
    for row in payoff_matrix_rows:
        payoff_squares = row.split()
        playerA_row_formatted = []
        playerB_row_formatted = []
        for square in payoff_squares:
            individual_payoffs = square.split(',')
            playerA_row_formatted.append(individual_payoffs[0])
            playerB_row_formatted.append(individual_payoffs[1])
        playerA.append(playerA_row_formatted)
        playerB.append(playerB_row_formatted)
    return playerA, playerB

def find_nash_equilibrium2(playerA_narr, playerB_narr, matrix_dim):
    # The algorithm is as such
    # playerA_narr strategies are reflected in rows
    # For each row in matrix B, find the greatest payoff for B and look in columns if A has incentive to deviate 
    lst_of_nash_eq = []
    for row in range(matrix_dim):
        row_in_B = playerB_narr[row]
        max_payoff_B = max(row_in_B)
        indices_of_max = np.where(row_in_B == max_payoff_B)[0]
        for col in indices_of_max:
            max_payoff_A = max(playerA_narr[:,col])
            if playerA_narr[row][col] == max_payoff_A:
                lst_of_nash_eq.append((row,col))
    return lst_of_nash_eq

def find_nash_equilibrium1(playerA_narr, playerB_narr, matrix_dim):
    # matrix A
    max_in_a = []
    max_in_b = []
    for i in range(matrix_dim):
        col = playerA_narr[:,i]
        max_payoff_A = max(col)
        rows_of_max = np.where(col == max_payoff_A)[0]
        max_in_a += zip(rows_of_max,[i] * len(rows_of_max))
    for i in range(matrix_dim):
        row = playerB_narr[i]
        max_payoff_B = max(row)
        cols_of_max = np.where(row == max_payoff_B)[0]
        max_in_b += zip([i] * len(cols_of_max),cols_of_max)
    return [filter(lambda x: x in max_in_a, max_in_b)]
                      
        
        
    
def parse_game_file(game_file,player_lst):
    f = open(game_file,'r')
    # The assumed file structure is as such:
    # First line: A number N referring to the subsequent N by N payoff matrix
    # Second line: Blank line
    # Next N line: One line per row in the payoff matrix
    # A sample line would be '1,2 3,4 5,3'
    # A's strategic choices are row1, row2...
    # B's strategic choices are col1, col2...

    lines = f.read()
    lines_split = lines.split('\n')
    matrix_dim = int(lines_split[0])
    payoff_matrix_rows = lines_split[2:2+matrix_dim]
    playerA,playerB = split_payoffs(payoff_matrix_rows,matrix_dim)
    playerA_narr = np.array(playerA, np.int32)
    playerB_narr = np.array(playerB, np.int32)
    player_lst.append(playerA_narr)
    player_lst.append(playerB_narr)
    return matrix_dim


def find_nash_eq1(player_lst, matrix_dim):
    lst_of_nash_eq = find_nash_equilibrium1(player_lst[0], player_lst[1],matrix_dim)
    return lst_of_nash_eq


def find_nash_eq2(player_lst, matrix_dim):
    lst_of_nash_eq = find_nash_equilibrium2(player_lst[0], player_lst[1],matrix_dim)
    return lst_of_nash_eq


def main():
    args = sys.argv
    game_file = args[1]
    player_lst = []
    matrix_dim= parse_game_file(game_file,player_lst)
    lst_of_nash_eq = find_nash_equilibrium(player_lst[0], player_lst[1],matrix_dim)
    print 'Algo1: ' + str(lst_of_nash_eq)
    lst_of_nash_eq = find_nash_equilibrium1(player_lst[0], player_lst[1],matrix_dim)
    print 'Algo2: ' + str(lst_of_nash_eq)
    return 0
    


if __name__ == '__main__':
    sys.exit(main())
