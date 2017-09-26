# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:36:20 2017

@author: Shruthi
"""

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    word_sum = 0
    for i in word:
        word_sum += SCRABBLE_LETTER_VALUES[i]
    word_sum *= len(word)
    if len(word) == n:
        word_sum += 50;
    
    return word_sum

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand =  dict(hand)
    for i in word:
        new_hand[i] -= 1

    return new_hand

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    copy_hand = dict(hand)
    if word in wordList:
        for i in word:
            if (copy_hand.get(i,0)):
                copy_hand[i] -= 1
            else:
                return False
    else:
        return False
    return True

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    len_hand = 0
    for i in hand:
        len_hand += hand[i]

    return len_hand

def playHand(hand, wordList, n):
    copy_hand =  dict(hand)
    score = 0
    len_hand = 0
    new_score = 0
    #new_word = 'word'
    while (copy_hand):
        if (calculateHandlen(copy_hand) > 0):
            print("Current Hand: ", end="")
            displayHand(copy_hand)
            new_word = input("Enter word, or a . to indicate that you are finished: ")
            if (new_word == '.'):
                print("Goodbye! Total score: " + str(score) + " points. ")
                return
            else:
                if (type(new_word) !=  str):
                    print("Invalid word, please try again.")
                else:
                    if (isValidWord(new_word, copy_hand, wordList)):
                        new_score = getWordScore(new_word,calculateHandlen(hand))
                        copy_hand = updateHand(copy_hand, new_word)
                        score += new_score
                        print("\""+str(new_word)+"\"" + " earned " + str(new_score) + " points. Total: " + str(score) + " points")
                    else:
                        print("Invalid word, please try again.") 
        else:
            print("Run out of letters. Total score: " + str(score) + " points.")
            return 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    last_hand = {}

    while(1):
        play_inp = input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")   
        if (play_inp == 'r' and last_hand == {}):
            print("You have not played a hand yet. Please play a new hand first!")
        elif (play_inp == 'n'):
            new_hand = dealHand(HAND_SIZE)
            last_hand = new_hand
            playHand(new_hand,wordList,HAND_SIZE)
        elif (play_inp == 'e'):
            return
        elif (play_inp == 'r'):
            playHand(last_hand,wordList,HAND_SIZE)
        else:
            print("Invalid command.")
            
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    last_hand = {}
    while(1):
        play_inp = input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")   
        if (play_inp == 'e'):
            return
        if (play_inp == 'r' and last_hand == {}):
            print("You have not played a hand yet. Please play a new hand first!")
        elif (play_inp != 'r' and play_inp != 'e' and play_inp != 'n') :
            print("Invalid command.")
        else:
            play_choice = input("Enter u to have yourself play, c to have the computer play:")
            if (play_choice != 'u' and play_choice != 'c'):
               print("Invalid command.")
            elif (play_inp == 'n'):
                new_hand = dealHand(HAND_SIZE)
                if (play_choice == 'u'):
                    last_hand = new_hand
                    playHand(new_hand,wordList,HAND_SIZE)
                else:
                    last_hand = new_hand
                    compPlayHand(new_hand,wordList,HAND_SIZE)
            elif (play_inp == 'e'):
                return
            elif (play_inp == 'r'):
                if (play_choice == 'u'):
                    playHand(last_hand,wordList,HAND_SIZE)
                else:
                    compPlayHand(last_hand,wordList,HAND_SIZE)
            else:
                print("Invalid command.")
