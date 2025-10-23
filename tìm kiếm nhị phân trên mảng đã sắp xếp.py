def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid   # trả về chỉ số tìm thấy
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # không tìm thấy


# Ví dụ sử dụng
arr = [1, 3, 5, 7, 9, 11, 15, 20]
x = 7

result = binary_search(arr, x)

if result != -1:
    print(f"Tìm thấy {x} tại vị trí {result}")
else:
    print(f"Không tìm thấy {x} trong mảng")
