def validate_params(permanence_period, target_time):
    if target_time is None:
        return True

    for start_time, end_time in permanence_period:
        if type(start_time) != int or type(end_time) != int:
            return True


def study_schedule(permanence_period, target_time):
    if validate_params(permanence_period, target_time):
        return None

    return sum(
        1 for start_time, end_time in permanence_period
        if start_time == target_time
        or end_time == target_time
        or ((start_time + end_time) // 2) == target_time
    )
