import random

def read_random_line():
    with open('dictionary of words.txt', 'r', encoding='utf-8') as file:
        for line in file:
            return random.choice(list(line.split(', ')))

def start():
    secret_word = read_random_line()
    state = ['_'] * len(secret_word)
    unsuccessful_attempts = 0
    max_attempts = 6

    while unsuccessful_attempts < max_attempts and "_" in state:
        answer = input("Введите букву: ")

        if answer in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == answer:
                    state[i] = answer
            print("Вы угадали!")
        else:
            unsuccessful_attempts += 1
            print("Такой буквы нет. Ошибок:", unsuccessful_attempts)

        print("Текущее состояние:", " ".join(state))

    if "_" not in state:
        print("Поздравляем, вы угадали слово:", secret_word)
    else:
        print("Игра окончена. Загаданное слово было:", secret_word)

start()
