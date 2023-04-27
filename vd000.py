n = int(input("enter a number: "))

def sum_of_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    print(sum)
    if sum > n:
        print(True)
    else:
        print(False)
sum_of_number(n)


