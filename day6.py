data = open('day6.txt', 'r').readlines()
data = [line.rstrip() for line in data]
records = []
record = []
for _record in data:
    if not len(_record):
        records.append(record)
        record = []
        continue
    record.append(_record)
if len(record):
    records.append(record)

### part1 ###
counter = 0
for groups in records:
    group = ''.join(groups)
    count = len(set(group))
    counter += count
print(counter)

### part2 ###
counter = 0
for groups in records:
    used_letters = {}
    for idx, group in enumerate(groups):
        unique_letters = list(set(group))
        for letter in unique_letters:
            if idx == 0:
                used_letters[letter] = 1
                continue
            if letter in used_letters:
                used_letters[letter]+=1
    counter += len([True for l in used_letters.values() if l == len(groups)])
print(counter)