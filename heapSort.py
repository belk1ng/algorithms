def heapify(arr, heap_size, root_index):  # finding the max elem
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        heapify(arr, heap_size, largest)


def heap_sort(arr):
    length = len(arr)

    for elem in range(length - 1, -1, -1):
        heapify(arr, length, elem)

    for elem in range(length - 1, 0, -1):
        arr[elem], arr[0] = arr[0], arr[elem]
        heapify(arr, elem, 0)

    return arr
