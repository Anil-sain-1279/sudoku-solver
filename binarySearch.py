def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [10, 20, 30, 40, 50]
x = int(input())
b = binary_search(arr, x)
for i in range(len(arr)):
    if arr[i] == x:
        print(f"Element found at index {i}")
        break
if b == -1:
    print("Element not found in the array")