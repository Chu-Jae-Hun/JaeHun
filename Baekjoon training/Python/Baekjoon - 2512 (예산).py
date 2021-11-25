n = int(input())
arr = (list(map(int, input().split())))
m = int(input())
low, high = 0, max(arr)

while low <= high:
    mid = (low + high) // 2
    num = 0
    for i in arr:
        if i >= mid:
            num += mid
        else:
            num += i
    if num <= m:
        low = mid + 1
    else:
        high = mid - 1
print(high)
