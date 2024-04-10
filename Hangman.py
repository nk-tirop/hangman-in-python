import random
from words import words
from hangman_visuals import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)#randomly chooses a word from the provided list
    while "-" in word or' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #words guessed by user

    lives = 7
    #getting user input
    while len(word_letters) > 0 and lives > 0:

        print('You have ',lives ,' lives left' 'You have used these letters: ', ' '.join(used_letters))
        #what current word is (ie W _ R D)
        word_list = [ letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print('current word', ' '.join(word_list))

        user_letter = input('Guess a latter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives-1
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('you have already used the character. Please try again:')

        else:
            print('Invalid character. Please try again')

    if lives ==0:
        print('GAME OVER!!\n You are out of lives. Anyway the word was  ',word)
    else:
        print('YAAAYYY!! YOU GUESSED THE WORD ',word, 'CORRECTLY!!')

    
if __name__ == '__main__':
    hangman()

