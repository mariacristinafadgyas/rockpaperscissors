"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import sys

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            user_move = input("Rock, paper, scissors? (q to quit) > ").lower()
            if user_move == "q":
                sys.exit()
            elif user_move in moves:
                return user_move
            else:
                print("Please select on of the following: ")


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return "rock"
        return self.their_move


class CyclePlayer(Player):
    def __init__(self):
        self.index = 0

    def move(self):
        if self.index % 3 == 0:
            self.index = 0
        while self.index <= len(moves):
            move = moves[self.index]
            self.index += 1
            return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def chose_rounds_no():
    while True:
        try:
            rounds_no = int(input("\u001b[35mHow many rounds do you want to play? \u001b[0m"))
            if isinstance(rounds_no, int):
                return rounds_no + 1
        except Exception:
            print("Please insert an integer! ")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.wins_p1 = 0
        self.wins_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played - {move1}.")
        print(f"Opponent played - {move2}.")
        if beats(move1, move2):
            self.wins_p1 += 1
            print("\u001b[34m*** PLAYER 1 WINS ***\u001b[0m")
        elif beats(move2, move1):
            self.wins_p2 += 1
            print("\u001b[31m*** PLAYER 2 WINS ***\u001b[0m")
        else:
            print("\u001b[33m*** TIE ***\u001b[0m")
        print(f"\u001b[32mScore: Player One: {self.wins_p1}, Player Two(Computer): {self.wins_p2}\u001b[0m")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")

        for round_no in range(1, chose_rounds_no()):
            print("****************************************")
            print(f"Round {round_no}:")
            self.play_round()

        print("Game over!")

        print("Final Results:")
        if self.wins_p1 > self.wins_p2:
            print("\u001b[34m*** PLAYER 1 WINS THE GAME ***\u001b[0m")
        elif self.wins_p1 < self.wins_p2:
            print("\u001b[31m*** PLAYER 2 WINS THE GAME ***\u001b[0m")
        else:
            print("\u001b[33m*** IT IS A TIE ***\u001b[0m")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
