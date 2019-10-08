# TO-DO: Complete the selection_sort() function below

list = [2, 4, 1, 5, 3, 6, 8, 7]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # print(f"Current index is {cur_index}")
        # print(f"Smallest index is {smallest_index}")
        # For all indices EXCEPT the last index:
        # a. Loop through elements on right-hand-side of current index
        for j in range(i + 1, len(arr)):
            # print(j)
            # find the smallest element
            # Compares the index of j with the index of i
            # print(f"[{arr[smallest_index]}, {arr[j]}]")
            if arr[smallest_index] > arr[j]:
                # print(arr[smallest_index])
                # print(arr[j])
                # print(f"[{arr[smallest_index]}, {arr[j]}]")
                smallest_index = j

        # b. Swap the element at current index with the
        # smallest element found in above loop
        # Swap variables without using temp variable > x,y = y,x
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

        # TO-DO: swap

    return arr


print(selection_sort(list))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
