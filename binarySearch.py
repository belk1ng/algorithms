def binary_search(array, num):
    high = len(array) - 1
    low = 0
    while low <= high:
        guess = int((high + low) / 2)
        if num == array[guess]:
            return guess
        elif num > array[guess]:
            low = guess + 1
        else:
            high = guess - 1
    return None
