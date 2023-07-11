def validate_params(permanence_period, target_time):
    if target_time is None:
        return True

    for time in permanence_period:
        if type(time[0]) != int or type(time[1]) != int:
            return True


def study_schedule(permanence_period, target_time):
    if validate_params(permanence_period, target_time):
        return None

    target_counter = 0

    for period in permanence_period:
        average_hour = period[0] + period[1] / len(period)

        if period[0] == target_time or period[1] == target_time:
            target_counter += 1

        if average_hour == target_time:
            target_counter += 1

    return target_counter
