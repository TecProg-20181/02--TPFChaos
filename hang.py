import random
import re

WORDLIST_FILENAME = "palavras.txt"

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split(' ')
    print ("  ", len(wordlist), "words loaded.")
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):

    secretLetters = []

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():

     guessed = ''


     return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def hanging(guesses):
    return {
        7: """ 
                    |      
                    |             
                    |             
                    |             
                    |             """,
        
        6 :"""
                    ________      
                    |      |      
                    |             
                    |             
                    |             
                    |             """,
        
        5 : """
                    ________ 
                    |      |      
                    |      0      
                    |             
                    |             
                    |             """,
        
        4 : """
                    ________      
                    |      |      
                    |      0      
                    |     /       
                    |             
                    |             """,
        
        3 : """
                    ________  
                    |      |      
                    |      0      
                    |     /|      
                    |             
                    |             """,
        
        2: """
                    ________      
                    |      |      
                    |      0      
                    |     /|\     
                    |             
                    |             """,
        
        1 : """
                    ________      
                    |      |      
                    |      0      
                    |     /|\     
                    |     /       
                    |             """,
        
        0 : """
                    ________      
                    |      |      
                    |      0      
                    |     /|\     
                    |     / \     
                    |             
                        GAME OVER!"""

    }[guesses]

def diffCharacters(secretWord):
    diff = ''.join(set(secretWord))
    length = len(diff)
    return length

def hangman(secretWord,length):

    
    guesses = 8
    lettersGuessed = []
    print ('Welcome to the game, Hangam!')
    print ('I am thinking of a word that is', len(secretWord), ' letters long.')
    print ('This word has',length,'different characters.' )
    print ('-------------')

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print ('You have ', guesses, 'guesses left.')
        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print ('Available letters', available)
        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print ('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print ('Good Guess: ', guessed)
        else:
            guesses -=1
            print(hanging(guesses))
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print ('Oops! That letter is not in my word: ',  guessed)
        print ('------------')

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print ('Congratulations, you won!')
        else:
            print ('Sorry, you ran out of guesses. The word was ', secretWord, '.')

length = 9
secretWord = ''
while length > 8:
    secretWord = loadWords().lower()
    length = diffCharacters(secretWord)

hangman(secretWord,length)

###The code was adapted from python to python3
