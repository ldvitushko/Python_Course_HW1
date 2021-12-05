def sanity_check(in_str):
    while True:
        try:
            var = int(input(in_str))
            if not (var <= 0):
                break
        except ValueError:
            print('Неверный ввод, необходимо ввести целочисленное значение больше нуля.')
    return var


def time_check(in_str):
    while True:
        try:
            hour, minute = input(in_str).split(':')
            hour = int(hour)
            minute = int(minute)
            if not ((0 <= hour <= 23) and (0 <= minute <= 59)):
                raise ValueError()
            break
        except ValueError:
            print('Неверный формат ввода времени')
    return 60 * hour + minute


def get_alarms_count(time, alarms):
    sum = 0
    for alarm in alarms:
        sum += max(((time-alarm)//alarm_repeat) + 1, 0)
    return sum

alarm_count = sanity_check('Введите количество будильников, которые заводит Алексей:')
alarm_repeat = sanity_check('Введите частоту повторения будильников (в минутах):')
required_alarms = sanity_check('Введите количество необходимых будильников:')
alarms = []
for i in range(alarm_count):
    alarms.append(time_check('Введите время {} будильника (в формате hh:mm):'.format(i + 1)))

alarms.sort(reverse=True)
alarm_dict = {}
for i in alarms:
    alarm_dict[i % alarm_repeat] = i
cleared_alarms = []
for alarm in alarm_dict.values():
    cleared_alarms.append(alarm)
alarms = cleared_alarms

min_time = min(alarms)
max_time = min_time + (required_alarms-1)*alarm_repeat

while min_time <= max_time:
    middle_time = min_time + (max_time - min_time) // 2
    if get_alarms_count(middle_time, alarms) == required_alarms:
        print('Алексей проснется в {}:{}'.format(middle_time // 60, middle_time % 60))
        break
    elif get_alarms_count(middle_time, alarms) > required_alarms:
        max_time = middle_time
    else:
        min_time = middle_time + 1
