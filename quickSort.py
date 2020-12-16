from random import randint


def quicksoriting(array):
    if len(array) < 2:
        return array
    else:
        choice = array[0]
        higher = [elem for elem in array[1:] if elem > choice]
        less = [elem for elem in array[1:] if elem <= choice]

        return quicksoriting(less) + [choice] + quicksoriting(higher)


def quicksorting_2(arr):  # a little faster
    if len(arr) < 2:
        return arr
    else:
        rand_elem = randint(1, len(arr) - 1)
        less = [elem for elem in arr[:rand_elem] + arr[rand_elem + 1:] if elem <= arr[rand_elem]]
        greater = [elem for elem in arr[:rand_elem] + arr[rand_elem + 1:] if elem > arr[rand_elem]]

        return quicksorting_2(less) + [arr[rand_elem]] + quicksorting_2(greater)
