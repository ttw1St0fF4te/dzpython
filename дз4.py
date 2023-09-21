def sum_digits(num):
    if num > 0 and isinstance(num, int):
        sum = 0
        while num > 0:
            digit = num % 10
            sum += digit
            num = num // 10
        return sum
    else:
        return 0 
while True:
    print("Введите число")
    try:
        value = int(input())
        print(sum_digits(value))
    except ValueError:
        print("not int number")
    break