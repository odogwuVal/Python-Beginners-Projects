import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

system_word = random.choice(words)

user_name = input('input your name: ')
print(f'Goodluck {user_name}!')

turn = 12

while turn > 0:
    failed = 0
    guess = input('guess an alphabet: ')
    if not guess:
        print(f'you have to enter an alphabet')
    else:
        for char in system_word:
            if guess in system_word:
                print(f'Congratulations!.....{char} is in {system_word}!')
                failed += 1
                break
                
        if failed > 0:
            break

        print(f'try again. you have {turn} turns left')

        if turn == 1:
            print(f'better luck next time....the word is {system_word}')
    turn -= 1