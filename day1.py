import numpy as np
import time
list = [1721, 979,366,299,675, 1456]
list = np.loadtxt('day1.txt')
list = sorted(list, reverse=True)
list = np.array(list, dtype=np.int)

print(f'size of list = {len(list)}')
year = 2020
counter = 0
ts = time.time()
# print(list)
def skip(idx):
    if idx > 2020 - list[-1] - list[-2]:
        return True
    return False

done = False
for idx in list:
    if skip(idx):
        continue
    for idy in list:
        if skip(idy):
            continue
        for idz in list:
            if skip(idz):
                continue
            counter +=1
            if idx + idy + idz == year:
                if not done:
                    print(f'{idx} * {idy} * {idz} = {idx*idy*idz}')
                    done = True
print(f'\nnumber of opearations = {counter}')
print(f'Whole process: {time.time()-ts :.02f} sec')



