def is_monotonic(nums):
    d = len(nums)
    b = True
    t = True
    for i in range (0, d - 1):
        if nums[i] - nums[i + 1] == 0:
            continue
        elif nums[i] - nums[i + 1] == -1:
            t = True
            break
        elif nums[i] - nums[i + 1] == 1:
            t = False
            break
        else:
            return False

    for i in range(0, d - 1):
        if t:
            if nums[i] - nums[i + 1] <= 0:
                continue
            else:
                b = False
        else:
            if nums[i] - nums[i + 1] >= 0:
                continue
            else:
                b = False

    return b