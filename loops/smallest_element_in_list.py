lst = list(map(int, input("Enter elements: ").split()))
smallest = lst[0]

for num in lst:
    if num < smallest:
        smallest = num

print("Smallest:", smallest)
