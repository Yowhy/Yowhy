# Ghost: a word game


#           Rules:
##stop condition:
##1. valid word and len(word) > 3
##2. invalid word and not substring (arbitrary len)

##continue when:
##1. valid word with len <= 3
##2. invalid word but is a substring (arbitrary lenght)

import random

LETTERS = 'aeioubcdfghjklmnpqrstvwxyz'

import string

WORDLIST_FILENAME = "F:\Python\Assignments\pset 5-6\words.txt"     #change file directory as per your PC


def load_words():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist


word_list = load_words()

# check if word is in word_list
def is_valid_word(word, word_list):
    if word in word_list:
        return True
    else:
        return False


#check if string is a substring of any word in word_list
def substring(word, word_list):
    for i in word_list:
        if i.find(word) == 0:
            return True
            break
    return False

        

def ghost():
    num = 1
    word = ''
    print 'Player 1 goes first.'
    print
    while True:
        number = 1
        if num%2 == 0:
            number = 2
        else:
            number = 1
        player = str(number)
        print 'Current word fragment: ', word 
        fragment = string.lower(raw_input('Player ' + player + ' says letter: '))
        print
        if len(fragment) > 1:
            print 'Can type one alphabetic character only'
            continue
        if LETTERS.find(fragment) == -1:
            print 'Invalid input. Pls try again!'
            continue
        elif len(fragment) > 1:
            print 'Invalid input. Pls try again!'
            continue
        else:
            word = word + fragment
        if is_valid_word(word, word_list) is True:
            if len(word) > 3:
                print 'Player ', number, ' loses because ', word, ' is a word!'
                break
            else:
                number += 1
                continue 
        elif substring(word, word_list) is True:
            num += 1
            continue
        else:
            print 'Player ', number, ' loses because no word begins with', word, ' !'
            break
