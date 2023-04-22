def insertion_sort(A):
    # [5,6,4,3,7,9,2]
    # [5,5,6,3,7,2,2]
    n = len(A)
    for i in range(1, n):
        j = i - 1
        # [j, i ]
        key = A[i]
        print(i)
        while A[j] > key and j >= 0:

            A[j+1] = A[j]
            j = j - 1

        A[j+1] = key
        print(A)
    return A


print(insertion_sort([5, 6, 4, 3, 7, 9, 2]))
