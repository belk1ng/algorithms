def eratosthen(n):
    nums = [elem for elem in range(2, n + 1)]
    for num in range(2, int(n / 2)):
        t = 2 * num
        while t <= n:
            nums[t - 2] = 0
            t += num
    nums = list(set(nums))
    nums.remove(0)
    nums.sort()

    return nums

