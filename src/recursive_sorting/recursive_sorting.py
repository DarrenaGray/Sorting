# TO-DO: complete the helper function below to merge 2 sorted arrays
list = [2, 4, 1, 5, 3, 6, 8, 7]


def merge(arrA, arrB):
    # print(f"Merge: {arrA} - {arrB}")
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    #
    # Write for loop that iterates over elements in arrA and arrB
    a = 0
    b = 0
    for i in range(elements):
        print(i)
        # Find the smallest first-item between arrA and arrB
        if a >= len(arrA):
            print(f"a is {a}")
            print(f"b is {b}")
            print(f"length of arrA: {len(arrA)}")
            print(f"arrB[b] is {arrB[b]}")
            merged_arr[i] = arrB[b]
            # print(f"arrB[b] is {arrB[b]}")
            print(f"merged_arr is {merged_arr[i]}")
            b += 1
            print(f"b is {a}")
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
            print(f"a is {b}")
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    # Add that to 'elements' at the given index
    # Increment the a/b counter

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # While data set contains more than one item
    if len(arr) > 1:
        print(f"Length is {len(arr)}")
        # Split it in half
        split = len(arr) // 2
        # Split lists in half on each side
        split_left = arr[:split]
        split_right = arr[split:]
        # Sort split arrays
        sort_left = merge_sort(split_left)
        sort_right = merge_sort(split_right)
        arr = merge(sort_left, sort_right)

    return arr


print(merge_sort(list))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
