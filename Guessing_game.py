import os
def guessing_game():
    Toguess = input("User 1 input the word to be guessed: ")
    os.system('cls')
    Triedword = ""
    result = False
    Timesgussed = 0
    print('User 2 find the word... :P You have 3 chances')

    while result == False:
        print(Toguess[0], '_ _ _', Toguess[4], '_ _', Toguess[-1:])
        Triedword = input('Guess the right word: ')
        os.system('cls')
        Timesgussed += 1
        print('Attempt', Timesgussed)
        if Timesgussed == 3:
            print('You are out of chances')
            break
        if Toguess != Triedword:
            print('Wrong answer :( Try again')
        elif Toguess == Triedword:
            print('That is the correct answer :D')
            result = True
            break
guessing_game()

import os
def guessing_game():
    Toguess = input("User 1 input the word to be guessed: ")
    os.system('cls')
    Triedword = ""
    result = False
    Timesgussed = 0
    midindex = len(Toguess)/2
    print('User 2 find the word... :P You have 3 chances')

    while result == False:
        print(Toguess[0], '__', Toguess[midindex], '__', Toguess[-1:])
        Triedword = input('Guess the right word: ')
        os.system('cls')
        Timesgussed += 1
        print('Attempt', Timesgussed)
        if Timesgussed == 3:
            print('You are out of chances')
            print('The correct answer is', Toguess)
            break
        if Toguess != Triedword:
            print('Wrong answer :( Try again')
        elif Toguess == Triedword:
            print('That is the correct answer :D')
            result = True
            break
guessing_game()