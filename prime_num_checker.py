def prime_num_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i ==0:
            is_prime = False
    if is_prime:
        print("PRIME NUMBER")
    else:
        print("NON PRIME NUMBER")
n = int(input("check this number: "))
prime_num_checker(number=n)