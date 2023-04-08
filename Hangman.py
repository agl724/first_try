import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = [
    "camel", "abyss", "blizzard", "duplex", "espionage", "equip", "embezzle", "dwarves", "fishhook", "galvanize", "gazebo",
    "santa", "haphazard", "gnarly", "ivory", "jinx", "knapsack", "zombie", "zodiac", "wizard", "whiskey", "vixen",
    "music", "auspicious", "psyche", "megahertz",
    "moon", "sketch", "play", "juice", "football", "cricket", "wolf", "antarctica", "seoul", "drink", "number", "azure", "vinyl"]
chosen_word = random.choice(word_list)
lives = 6
print("chosen wrd = ", chosen_word)
display = []
for fun in chosen_word:
    display += "_"
print(logo)
while "_" in display:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("YOU LOSE.")
            print(stages[lives])
            break
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("YOU WIN.")

    print(stages[lives])
