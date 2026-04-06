lst = list(map(int, input("Enter elements: ").split()))
product = 1

for num in lst:
    product *= num

print("Product:", product)