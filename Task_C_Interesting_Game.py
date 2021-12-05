import numpy as np


def interesting_game(max_point, cards_count):

    cards_list = np.random.randint(0, 1000, cards_count)

    print(cards_list)
    points_Vasya = 0
    points_Petya = 0

    for i in cards_list:
        if points_Vasya == max_point or points_Petya == max_point:
            break
        elif i % 5 == 0:
            if i % 3 == 0:
                continue
            else:
                points_Vasya += 1
        elif i % 3 == 0:
            points_Petya += 1

    if points_Vasya == points_Petya:
        print('Ничья!')
    elif points_Vasya > points_Petya:
        print('Победил Вася!')
    else:
        print('Победил Петя!')


def sanity_check(in_str):
    while True:
        try:
            var = int(input(in_str))
            if not (var <= 0):
                break
        except ValueError:
            print('Неверный ввод, необходимо ввести целочисленное значение больше нуля.')
    return var


max_point = sanity_check('Введите очки, которые надо набрать, чтобы игра закончилась:')
cards_count = sanity_check('Введите количество карточек:')
interesting_game(max_point, cards_count)
