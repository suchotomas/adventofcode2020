data = open('day5.txt', 'r').readlines()
data = [line.rstrip() for line in data]

# data = ['BBFBBFBRRR']
highest_id = 0
seats = []
for seat in data:
    r0, r1 = 0,127
    c0,c1 = 0,7
    for idx, l in enumerate(seat):

        if l == 'F':
            r1 -= int((r1 - r0)/2 + 1)
        if l == 'B':
            r0 += int((r1-r0)/2 + 1)

        if l == 'L':
            c1 -= int((c1 - c0) / 2 + 1)
        if l == 'R':
            c0 += int((c1 - c0) / 2 + 1)

        if idx == 6:
            r0 = r0 if l =='F' else r1
        if idx == len(seat) - 1:
            c0 = c0 if l=='L' else c1
    seat_id = int(r0*8 + c0)
    seats.append(seat_id)
    highest_id = max(seat_id, highest_id)
seats = set(seats)
print(f'highest seat_id = {highest_id}')

for idx in range(highest_id):
    if idx-1 in seats and idx + 1 in seats and idx not in seats:
        print(f'missing sead_id = {idx}')
