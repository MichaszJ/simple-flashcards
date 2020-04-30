class Card:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def poseQuestion(self):
        print('\n')
        print(self.question)
        for choice in self.choices:
            print(choice)

    def tryGuess(self, guess):
        if guess.lower() == self.answer[0].lower() or guess.lower() == self.answer[0:2].lower():
            return True
        else:
            return False