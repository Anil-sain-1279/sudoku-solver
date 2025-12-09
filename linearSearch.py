arr = [10,20,30,40,50]
x = int(input())
found = False
for i in range(len(arr)):
    if arr[i] == x:
        print(f"Element found at index {i}")
        found = True
        break
if not found:
    print("Element not found in the array")