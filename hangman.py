from random import randint
from os import system, name

def getRandomWord():
    with open("mywords.txt", "r") as textFile:
        words = textFile.readlines()
    return words[randint(0, len(words) - 1)].strip()

def drawMan(incorrect):
    if incorrect == 0:
        return ''
    if incorrect == 1:
        return '|\n|\n|\n|\n|\n|'
    if incorrect == 2:
        return '______\n|/\n|\n|\n|\n|\n|'
    if incorrect == 3:
        return '______\n|/     |\n|\n|\n|\n|\n|'
    if incorrect == 4:
        return '______\n|/     |\n|      O\n|\n|\n|\n|'
    if incorrect == 5:
        return '______\n|/     |\n|      O\n|      /\\\n|\n|\n|'
    if incorrect == 6:
        return '______\n|/     |\n|      O\n|      /\\\n|      |\n|\n|'
    if incorrect == 7:
        return '______\n|/     |\n|      O\n|      /\\\n|      |\n|     / \\\n|'

def clearScreen():
    if name == 'nt':  # For Windows
        system('cls')
    else:  # For Unix-like systems
        system('clear')

def play():
    word = getRandomWord()
    progress = '_' * len(word)
    incorrect = 0
    guesses = []

    while True:
        clearScreen()
        guessesString = ', '.join(guesses)
        print(f'Past Guesses: {guessesString}')
        print(drawMan(incorrect))
        
        if progress == word:
            print(progress)
            print(f'You Win! The word was {word}')
            break
        if incorrect >= 7:
            print(f'You Lose! The word was {word}')
            break
        print(progress)
        print('Enter a letter: ')
        
        guess = input().strip()
        
        if guess in guesses:
            continue
        guesses.append(guess)
        
        if guess in word:
            progress = ''.join([guess if word[i] == guess else progress[i] for i in range(len(word))])
        else:
            incorrect += 1

if __name__ == '__main__':
    while True:
        play()
        print('Would you like to play again? (y/n)')
        if input().strip().lower() != 'y':
            print('Goodbye!')
            break
