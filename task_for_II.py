numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(numbers[1], len(numbers)+1):
    flag = True
    for j in range(2,i):
        if i/j in numbers:
            flag = False
            break

    if (flag == False):
        not_primes.append(i)
    elif (flag == True):
        primes.append(i)
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')