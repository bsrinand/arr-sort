def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))  # Output: True
