from card import Card
from random import choice

class Deck:
    def __init__(self, path):
        with open(path, 'r') as file:
            lines = file.readlines()

        choices = []
        deck = []
        for count, line in enumerate(lines):
            if line[0:3] == 'Q: ':
                question = line[3:].strip()
            elif line[0:3] == 'C: ':
                choices.append(line[3:].strip())
            elif line[0:3] == 'A: ':
                answer = line[3:].strip()

                if count == len(lines) - 1:
                    deck.append(Card(question, choices, answer))
                    choices = []
            else:
                deck.append(Card(question, choices, answer))
                choices = []

        self.cards = deck

    def printAllQuestions(self):
        for count, card in enumerate(self.cards):
            print('{0}.'.format(count + 1), card.question)

    def printAllQuestionsChoices(self):
        for count, card in enumerate(self.cards):
            print('\n')
            print('{0}.'.format(count + 1), card.question)
            for choice in card.choices:
                print('  ', choice)

    def printAll(self):
        for count, card in enumerate(self.cards):
            print('\n')
            print('{0}.'.format(count + 1), card.question)
            for choice in card.choices:
                print(choice)
            print('Answer:', card.answer)

    def printQuestion(self, cardNum):
        card = self.cards[cardNum]
        print('\n')
        print('{0}.'.format(cardNum + 1), card.question)
        for choice in card.choices:
            print('  ', choice)

    def askQuestions(self):
        cardNums = list(range(0, len(self.cards)))

        while len(cardNums) > 0:
            num = choice(cardNums)
            card = self.cards[num]

            self.printQuestion(num)
            guess = input()

            if card.tryGuess(guess):
                cardNums.remove(num)
                print('True')
            else:
                print('False')