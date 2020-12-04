'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''
import re
data = open('day4.txt', 'r').readlines()
data = [line.rstrip() for line in data]
records = []
record = {}
for _record in data:
    if not len(_record):
        records.append(record)
        record = {}
        continue
    for r in _record.split(' '):
        key, value = r.split(':')
        record[key] = value
if len(record):
    records.append(record)
valid = 0




def validated(rec):
    '''byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.'''
    byr = rec['byr']
    iyr = rec['iyr']
    eyr = rec['eyr']
    hgt = rec['hgt']
    hcl = rec['hcl']
    ecl = rec['ecl']
    pid = rec['pid']
    ecl_flags = ['amb','blu', 'brn','gry','grn','hzl','oth']

    hgt_val, hgt_metric = hgt[:-2], hgt[-2:]
    if hgt_val.isnumeric():
        hgt_val = int(hgt_val)
    else:
        return False
    condition = [
        len(byr) == 4 and 1920 <= int(byr) <= 2002,
        len(iyr) == 4 and 2010 <= int(iyr) <= 2020,
        len(eyr) == 4 and 2020 <= int(eyr) <= 2030,
        (hgt_metric == 'cm' and 150 <= hgt_val <= 193) or (hgt_metric == 'in' and 59 <= hgt_val <=76),
        hcl[0] == '#'  and  re.compile(r'^[a-f0-9]+$').fullmatch(hcl[1:]) and len(hcl) == 7,
        ecl in ecl_flags,
        str(pid).isnumeric(), len(pid) == 9
    ]
    if False in condition:
        return False
    return True

flags = sorted(['byr','iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

for record in records:
    record_keys = sorted([r for r in record.keys() if r != 'cid'])
    if record_keys == flags:
        if validated(record):
            valid+=1
print(valid)

