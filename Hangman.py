stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
import random
import 
lives = 6
word_list = ["door", "balloon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

underscore = ""
word_length = len(chosen_word)
for letter in range(word_length):
    underscore += "_"
print(underscore)


c_words = []
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    for letter in chosen_word :
        if letter == guess:
            display += letter
            c_words.append(letter)
        elif letter in c_words:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -=1
    elif lives == 0:
        print("You Lose!")

    if "_" not in display:
        game_over = True
        print("You Win!")

    print(stages[lives])







