import random


def read_random_line():
    """Случайное слово из файла"""
    with open('dictionary of words.txt', 'r', encoding='utf-8') as file:
        words = file.read().split(', ')
        return random.choice(words).lower()


def validator():
    """Запрашивает букву и проверяет, что это кириллица"""
    while True:
        entered_letter = input("Введите букву (Кириллица): ").lower()
        if len(entered_letter) == 1 and 1072 <= ord(entered_letter) <= 1103:
            return entered_letter
        else:
            print("Неверный ввод. Введите одну букву кириллицы.")


def play_hangman():
    secret_word = read_random_line()
    state = ['_'] * len(secret_word)
    unsuccessful_attempts = 0
    max_attempts = 6

    while unsuccessful_attempts < max_attempts and "_" in state:
        answer = validator()

        if answer in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == answer:
                    state[i] = answer
            print("Вы угадали!")
            draw_hangman(unsuccessful_attempts)
        else:
            unsuccessful_attempts += 1
            print("Такой буквы нет. Ошибок:", unsuccessful_attempts)
            draw_hangman(unsuccessful_attempts)

        print("Текущее состояние:", " ".join(state))

    if "_" not in state:
        print("Поздравляем, вы угадали слово:", secret_word)
    else:
        print("Игра окончена. Загаданное слово было:", secret_word)


def draw_hangman(attempts):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(stages[attempts])


# Запуск игры
play_hangman()
