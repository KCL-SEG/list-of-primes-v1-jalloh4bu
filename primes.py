"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []
    count = 0
    number = 1
    while count < number_of_primes:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        if len(factors) == 2:
            list.append(number)
            count += 1
        number += 1

    return list
