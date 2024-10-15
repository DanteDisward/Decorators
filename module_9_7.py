def is_prime(num):
    def wrapper(one, two, three):
        remains = 0
        for i in range(num(one, two, three), 0, -1):
            if num(one, two, three) % i == 0:
                remains += 1
            if remains > 2:
                break
        if remains > 2:
            print('Составное')
        elif remains == 2:
            print('Простое')
        return num(one, two, three)
    return wrapper


@is_prime
def sum_three(one, two, three):
    num = [one, two, three]
    result_def = sum(num)
    return result_def


result = sum_three(2, 3, 6)
print(result)
