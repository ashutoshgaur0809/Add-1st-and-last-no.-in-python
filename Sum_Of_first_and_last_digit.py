T = int(input("Enter how many test cases you want = "))
for i in range(T):
    n = int(input("Enter an no- "))
    # first digit
    a = n
    while a >= 10:
        a = a // 10
    print("Fisrt digit = ", a)

    # last digit
    b = n % 10
    c = a+b
    print(c)
