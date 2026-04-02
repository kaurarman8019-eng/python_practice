num = int(input("Enter number: "))

while num > 9:
    sum = 0
    
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
        
    num = sum

print("Super number:", num)