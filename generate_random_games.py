import random
import sys


def get_dim_from_user():
    dim_str = raw_input("Enter dimension of square, or <ENTER> to exit:")
    dim = 0
    if len(dim_str) == 0:
        print 'Exiting'
        return -1
    try:
        dim = int(dim_str)
    except ValueError:
        print 'Malformed input, exiting program'
        return -1
    return dim

def get_dim_from_user_errorcheck():
    dim = 0
    while True:
        dim_str = raw_input("Enter dimension of square:")
        try:
            dim = int(dim_str)
            break
        except ValueError:
            print 'Malformed input, please enter a number greater than 0'
    return dim


def create_file(dim,game_file):
    file = open(game_file,'w')
    file.write(str(dim) + '\n\n')
    for i in range(dim):
        for j in range(dim):
            payoff1 = random.randint(0,100)
            payoff2 = random.randint(0,100)
            payoff_str = str(payoff1) + ',' + str(payoff2) + ' '
            file.write(payoff_str)
        file.write('\n')
    file.close()


def main():
    FILE_NAME = 'game.txt'
    while True:
        dim = get_dim_from_user()
        if dim < 0:
            break
        create_file(dim,FILE_NAME)
    return 0

def generate_random_games(game_file):
    dim = get_dim_from_user_errorcheck()
    create_file(dim,game_file)

if __name__ == '__main__':
    sys.exit(main())
