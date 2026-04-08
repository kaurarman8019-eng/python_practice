lst = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to count: "))
count = 0

for num in lst:
    if num == x:
        count += 1

print("Count:", count)
