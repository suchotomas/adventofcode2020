
data = open('day3.txt', 'r').readlines()


def is_tree(line, position):
    while position >= len(line):
        position -= len(line)

    # print(position)
    return line[position]=='#'

def count_slope(x,y):
    tree_counter = 0
    x_position = 0
    skip_lines_counter = y-1
    for line_idx, line in enumerate(data):
        if skip_lines_counter > 0 and line_idx !=0:
            skip_lines_counter-=1
            continue
        line = line.split()[0]
        tree_counter += is_tree(line, x_position)
        x_position += x
        skip_lines_counter = y-1

    return tree_counter

offsets = [(1,1),(3,1),(5,1), (7,1), (1,2)]

total_count = 1
for x,y in offsets:
    print(f'\n{x}, {y}')
    slope = count_slope(x,y)
    print(slope)
    total_count *= slope
print(total_count)
