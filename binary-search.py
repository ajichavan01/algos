def binarySearch(arr, key, low, high):
    while low < high:
        mid = (low + high) // 2

        if arr[mid] == key:
            print("Found key at ", mid)
            return
        elif arr[mid] > key:
            high = mid
        else:
            low = mid + 1

    print("Key not found in arr")


arr = [2, 4, 5, 9, 15, 39, 88, 102, 133]
key = 15

binarySearch(arr, key, 0, len(arr) - 1)
