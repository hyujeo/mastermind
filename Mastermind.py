import random
import itertools

class Mastermind:
    board = []
    answer = []
    current_row = -1
    def __init__(self, holes, tries, colors):
        self.holes = holes
        self.tries = tries
        self.colors = colors
        
        # initialize board and set the pins to 0
        self.board = [[" "] * (holes + 2) for _ in range (tries)]
        for row in self.board:
            row[-2], row[-1] = 0, 0
        
        # create a random answer
        for _ in range(holes):
            self.answer.append(random.choice(colors))
    
    def print_board(self):
        size = max(len(str(x)) for x in self.colors)
        print("Colors:", self.colors)
        for row in self.board:
            for i in range(self.holes):
                print("| " + row[i] + " " * (size - len(str(row[i])) + 1), end='')
            print("|| " + str(row[-2]) + ", " + str(row[-1]))
            print()
    
    def guess(self, userguess):
        self.current_row += 1

        answer = self.answer.copy()
        
        for i in range(self.holes):
            self.board[self.current_row][i] = userguess[i]

        i = 0
        # finds all the black pins
        while i < len(answer):
            if answer[i] == userguess[i]:
                answer.pop(i)
                userguess.pop(i)
                self.board[self.current_row][-2] += 1
            else:
                i += 1
        
        # finds all white pins
        for hole in userguess:
            try:
                loc = answer.index(hole)
                answer[loc] = None
                self.board[self.current_row][-1] += 1
            except ValueError:
                continue

    def ended(self):
        return self.current_row >= self.tries or self.won()

    def won(self):
        return self.board[self.current_row][-2] == self.holes

        



                
                
            