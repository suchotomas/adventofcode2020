import re

data = open('day2.txt', 'r').readlines()


def first_validation(key, passw, f, t):
    return f <= len([p for p in passw if p == key]) <= t


def second_valitadion(key, passw, p1, p2):
    return (passw[p1 - 1] == key) != (passw[p2 - 1] == key)


valid_part1 = 0
valid_part2 = 0
for l in data:
    f, t, key, _, passw  = re.split('[- :]', l.strip())
    f, t = int(f), int(t)
    if first_validation(key, passw, f, t):
        valid_part1 += 1

    if second_valitadion(key, passw, f, t):
        valid_part2 += 1

print(f'First part = {valid_part1}')
print(f'Second part = {valid_part2}')
