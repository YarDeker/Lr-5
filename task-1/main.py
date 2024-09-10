n = int(input("Введіть довжину масива: "))
while n < 2:
    n = int(input("Введіть довжину масива більшу за 1: "))

arr = []
sum = 0

for num in range(n):
    if len(arr) < 2:
        arr.append(num)
    else:
        num = arr[len(arr) - 1] + arr[len(arr) - 2]
        arr.append(num)

for num in range(n):
    print(arr[num], end=" ")
