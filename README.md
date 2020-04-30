# Simple Flashcards
This is a simple Python program that allows you to test yourself using a bank of multiple choice questions. It was designed in a way to allow for arbitrary number of choices, allowing for true/false questions as well. This was created for personal use and to learn more about how classes work.

## Usage
To use, call `main.py` and specify the path to the deck and the deck name:
```python
python main.py pathtodeck/deckname.txt
```

To create a deck, refer to the example deck, or create your own using this example format in a .txt file:
```
Q: Question 1
C: A. Choice 1
C: B. Choice 2
A: B. Choice 2 

Q: Question 2
C: A. Choice 1
C: B. Choice 2
A: B. Choice 2 
```

## To-Do
- [ ] Write deck generation script
- [ ] Implement "smarter" functionality, as program simply repeats questions blindly until all questions have been answered correctly
