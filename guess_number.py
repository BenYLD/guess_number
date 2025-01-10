from random import randint


number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    guess = int(input('Введите число: '))
    if number < guess:
        print('Ваше число меньше того, что загадано.')
    elif number > guess:
        print('Ваше число больше того, что загадано.')
    
    elif guess == number:
        break
print('Отличная интуиция! Вы угадали число :)')
