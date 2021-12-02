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


def count_alarms_in_defined_time(time_alarm, time, period):
    if time_alarm > time:
        return 0
    return 1 + (time - time_alarm) // period


alarm_count = sanity_check('Введите количество будильников, которые заводит Алексей:')
alarm_repeat = sanity_check('Введите частоту повторения будильников (в минутах):')
required_alarms = sanity_check('Введите количество необходимых будильников:')
alarms = []
for i in range(alarm_count):
    alarms.append(time_check('Введите время {} будильника (в формате hh:mm):'.format(i + 1)))
alarms.sort()
alarms.reverse()
alarm_dict = {}
for i in alarms:
    alarm_dict[i % alarm_repeat] = i
cleared_alarms = []
for alarm in alarms:
    if alarm in alarm_dict.values():
        cleared_alarms.append(alarm)
alarms = cleared_alarms

for i in range(24 * 60):
    k = 0
    for j in alarms:
        k += count_alarms_in_defined_time(j, i, alarm_repeat)
    if k >= required_alarms:
        print('Алексей проснется в {}:{}'.format(i // 60, i % 60))
        break
