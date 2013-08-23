import find_nash_eq
import generate_random_games
import sys
import time

def main():
    while True:
        game_file = 'game.txt'
        generate_random_games.generate_random_games(game_file)
        with open(game_file, 'r') as f:
            print f.read()
        player_lst = []
        matrix_dim= find_nash_eq.parse_game_file(game_file,player_lst)
        start = time.time()
        find_nash_eq.find_nash_eq1(player_lst, matrix_dim)
        print time.time() - start
        start = time.time()
        find_nash_eq.find_nash_eq2(player_lst, matrix_dim)
        print time.time() - start

if __name__ == '__main__':
    sys.exit(main())
