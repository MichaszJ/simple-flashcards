from deck import Deck
from sys import argv

def main():
    deck = Deck(argv[1])
    deck.askQuestions()

if __name__ == '__main__':
    main()