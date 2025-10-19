import random


def get_numbers_ticket(min, max, quantity):
    if quantity < 1 or\
       min < 1 or\
       max > 1000 or\
       (max - min) < quantity:
        return []
    return sorted(random.sample(range(min, max+1), quantity))

print(get_numbers_ticket(1, 36, 5))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 1001, 5))
print(get_numbers_ticket(-1, 10, 2))
print(get_numbers_ticket(1, 10, 11))
