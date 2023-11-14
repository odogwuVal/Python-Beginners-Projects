import random
import math


def numberGuessing():
    # Taking user inputs
    smallest = int(input('Enter lower bound: '))
    highest = int(input('Enter upper bound: '))

    system_number = random.randint(smallest, highest)
    trial = round(math.log2(highest - smallest + 1))
    print(f'You have {trial} trials')

    count = 0
    while count < trial:
        guess = int(input('Guess a number: '))
        count += 1
        if guess < smallest or guess > highest:
            print(f'choose a number between {smallest} and {highest}')
        elif guess == system_number:
            print(f'Congratulations!...you guessed right in {count} trials')
            break
        elif guess < system_number:
            print('Try again!...your guess is too small')
        elif guess > system_number:
            print('Try again!...your guess is too high')
    if count >= trial:
        print(f'The number is {system_number}!')
        print(f'Better Luck Next time')

if __name__ == '__main__':
    numberGuessing()