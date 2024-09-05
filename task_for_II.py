numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:
    flag = True
    for j in numbers[1:]:
        if i/j in numbers[1:]:
            flag = not True
            break
    if (flag == True):
        primes.append(i)
    elif (flag == False):
        not_primes.append(i)
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')
