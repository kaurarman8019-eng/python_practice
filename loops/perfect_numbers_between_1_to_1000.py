for num in range(1, 1001):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num, end=" ")
