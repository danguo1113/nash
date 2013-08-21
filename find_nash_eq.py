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

def find_nash_equilibrium(playerA_narr, playerB_narr, matrix_dim):
    # The algorithm is as such
    # playerA_narr strategies are reflected in rows
    # For each row, find the greatest elements and look in columns if B has incentive to deviate 
    lst_of_nash_eq = []
    for row in range(matrix_dim):
        row_in_A = playerA_narr[row]
        max_payoff_A = max(row_in_A)
        indices_of_max = np.where(row_in_A == max_payoff_A)[0]
        for col in indices_of_max:
            max_payoff_B = max(playerB_narr[:,col])
            if playerB_narr[row][col] == max_payoff_B:
                lst_of_nash_eq.append((row,col))
    return lst_of_nash_eq
    
def parse_game_file(game_file):
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
    print playerA_narr
    print playerB_narr

    lst_of_nash_eq = find_nash_equilibrium(playerA_narr, playerB_narr,matrix_dim)

def main():
    args = sys.argv
    game_file = args[1]
    a_matrix,b_matrix = parse_game_file(game_file)
    

if __name__ == 'main':
    main()