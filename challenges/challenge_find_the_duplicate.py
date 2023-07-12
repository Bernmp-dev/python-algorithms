def find_duplicate(nums):
    if nums is None or len(nums) <= 1:
        return False

    seen = set()

    for num in nums:
        if (type(num) != int or num <= 0):
            return False
        if num in seen:
            return num
        seen.add(num)

    return False
