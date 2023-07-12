def merge_sort_string(s):
    if len(s) <= 1:
        return s
    mid = len(s) // 2
    left_half = merge_sort_string(s[:mid])
    right_half = merge_sort_string(s[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    merged = ''
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged += left[i]
            i += 1
        else:
            merged += right[j]
            j += 1
    while i < len(left):
        merged += left[i]
        i += 1
    while j < len(right):
        merged += right[j]
        j += 1
    return merged


def is_anagram(first_string, second_string):
    fs_sorted = merge_sort_string(first_string.lower())
    ss_sorted = merge_sort_string(second_string.lower())

    if (
        len(fs_sorted) != len(ss_sorted)
        or fs_sorted != ss_sorted
        or fs_sorted == ""
        or ss_sorted == ""
    ):
        return (fs_sorted, ss_sorted, False)

    return (fs_sorted, ss_sorted, True)
