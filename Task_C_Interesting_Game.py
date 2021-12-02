from random import randint


def interesting_game(max_point, cards_count):
    cards_list = []
    for i in range(cards_count):
        # cards contain random numbers from 0 to 1000
        cards_list.append(randint(0, 1000))
    print(cards_list)
    points_Vasya = 0
    points_Petya = 0
    for i in cards_list:
        if i % 5 == 0 and i % 3 != 0:
            points_Vasya = points_Vasya + 1
        elif i % 3 == 0 and i % 5 != 0:
            points_Petya = points_Petya + 1
        elif points_Vasya == max_point or points_Petya == max_point:
            break
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
