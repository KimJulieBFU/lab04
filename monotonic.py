def is_monotonic(nums):
    up_down = 1  # индикатор возрастания или убывания списка (0 - возрастает, 1 - убывает)
    monotonic = 1 # индикатор монотонности списка
    length = len(nums)  # длинна данного списка nums
    
    for i in range (0, length - 1): # узнаём, список возрастает или убывает
        if nums[i] - nums[i + 1] == 0:
            continue
        elif nums[i] - nums[i + 1] == -1:
            up_down = 1
            break
        elif nums[i] - nums[i + 1] == 1:
            up_down = 0
            break
        else:
            return False

    for i in range(0, length - 1): # узнаём, монотонна ли список
        if up_down:
            if nums[i] - nums[i + 1] <= 0:
                continue
            else:
                monotonic = 0
        else:
            if nums[i] - nums[i + 1] >= 0:
                continue
            else:
                monotonic = 0
    if monotonic == 1:
        return True
    else:
        return False
