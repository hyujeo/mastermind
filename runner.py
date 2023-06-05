from Mastermind import Mastermind

NUM_HOLES = 4
NUM_TRIES = 10
# COLORS = ["red", "green", "blue", "brown", "purple", "yellow"]
COLORS = []

# used for filling out COLORS with just numbers
NUM_COLORS = 6
if len(COLORS) == 0:
    for i in range(NUM_COLORS):
        COLORS.append(str(i+1))

def main():
    Game = Mastermind(NUM_HOLES, NUM_TRIES, COLORS)
    while not Game.ended():
        Game.print_board()
        userinput = input("type your guess in the format 'COLOR COLOR ... COLOR'.\n")
        Game.guess(userinput.split(" "))
    Game.print_board()
    if (Game.won()):
        print("YOU WON!")        
    else:
        print("YOU LOST!")
        print("the answer was:")
        print(Game.answer)
main()