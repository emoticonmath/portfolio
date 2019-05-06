import random
import time
def game_end():#game lose function (runs when player loses)
    #allows player to reset the game
    time.sleep(1)
    restart = raw_input('Do you want to try again? Y or N: ')
    answer = restart
    if answer == 'Y' or answer == 'y':
        time.sleep(1)
        print('--<>--')
        print('Starting new game')
        print('--<>--')
        hangman()
    else:
        time.sleep(1)
        print('--<>--')
        print "You win nothing. You lose! Good day sir!"
        return
def game_win():#game win function (runs when player wins)
    #allows player to reset the game
    time.sleep(1)
    restart = raw_input('Do you want to try again? Y or N:')
    answer = restart
    if answer == 'Y' or answer == 'y':
        time.sleep(1)
        print('--<>--')
        print('Starting new game')
        hangman()
    else: 
        time.sleep(1)
        print('--<>--')
        print('Congrats! You won!')
        return
def hangman_display(guessed, secret):
    '''Replaces letters in secret based on characters in guessed'''
    for x in secret: 
        if x not in guessed:
            if x != " ":
                secret = secret.replace(x,"-")
    return secret
def hangman():
    '''This is a simple hangman game based off of Pokemon!'''
    print """\
                                      ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|





            """
    time.sleep(1)    
    print "Welcome to Poke-Hangman, fellow contemporaries."
    time.sleep(1)
    print "Get ready to guess."
    print "Make sure to turn on CAPS LOCK."

    word = random.choice(["VENUSAUR", "CHARIZARD", "BLASTOISE", "PIKACHU", 
                          "EKANS", "ARBOK", "HO OH", "LUGIA", "RESHIRAM",    
                          "PROFESSOR OAK", "ASH KETCHUM", "POKEBALL", "CYNTHIA",
                          "SUN", "MOON", "EXEGGUTOR", "ALAKAZAM", "ABRA",
                          "MASTER BALL", "JINX", "DUGTRIO", "PICHU", "RAICHU",
                          "SNORLAX", "RATICATE", "MISTY", "BROCK", "HITMONLEE",
                          "WEEZING", "LEGENDARY", "BATTLE", "EVOLVE", 
                          "ELITE FOUR", "PSYCHIC", "LEVEL"]) 
                          #list of words used, word is randomly chosen from list
    guess = 6 #amount of guesses
    fails = 0 #counter till game over (once reaches 6 game will be over)
    guessed = "" #letters used
    print hangman_display(guessed, word)
    while fails < 6:
        r = raw_input("Guess... \n") 
        #\n" makes it so that the code isn't case sensitive
        if len(r) > 1: #checks if input is 1 letter
            print ('Your input is more than 1 letter. Please try again.')
            fails += 1
            print hangman_display(guessed, word)
            continue
        elif not r.isalpha(): #checks if input is letter
            print ('That is not a letter. Please try again.')
            fails += 1
            print hangman_display(guessed, word)
            continue
        elif r in guessed: #checks if input is already guessed
            print ('You have already guessed that letter. Please try again.')
            fails += 1
            print hangman_display(guessed, word)
            continue
        guess += 1 #increases amount of guesses
        r = r.upper()
        guessed += r #adds guesses into guessed list
        x = hangman_display(guessed, word)
        if r in word: #checks if guess is in word
            print "You have guessed correctly."
            print hangman_display(guessed, word)
        else: #checks if guess isn't in word
            print "You have guessed incorrectly."
            fails += 1
            print x 
            if fails == 1: #prints part of hanging man if they guess wrong
                print """\
        _________
        |        |
        |        0
        |        
        |         
        |
        |
                """
            if fails == 2:
                print """\
        _________
        |        |
        |        0
        |        |
        |         
        |
        |
                """
            if fails == 3:
                print """\
        _________
        |        |
        |        0
        |        |
        |         \
        |
        |
                """
            if fails == 4:
                print """\
        _________
        |        |
        |        0
        |        |
        |       / \
        |
        |                
                """
            if fails == 5:
                print """\
        _________
        |        |
        |        0
        |        |\
        |       / \
        |
        |                
                """
        if x == word:
            print "Conglaturations. You have won."
            game_win()
            break
    if fails == 6: #What happens when they lose
        time.sleep(1)
        print """\
         _________
        |        |
        |        0
        |       /|\
        |       / \
        |
        |                
                """
        time.sleep(.5)
        print "You have no more guesses!"
        time.sleep(.5)
        print "The word is " + word, "." #gives them answer
        game_end() #runs game over function
hangman()