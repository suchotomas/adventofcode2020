import numpy as np
import time
# _list = [1721, 979, 366, 299, 675, 1456]
_list = np.loadtxt('day1.txt', dtype=int)
_list = np.flip(np.sort(_list))

print(f'size of the list = {len(_list)}')

def skip(idx):
    if idx > 2020 - _list[-1] - _list[-2]:
        return True
    return False

done = False
year = 2020
counter = 0
ts = time.time()

for idx in _list:
    if skip(idx):
        continue
    for idy in _list:
        if skip(idy):
            continue
        for idz in _list:
            if skip(idz):
                continue
            counter +=1
            if idx + idy + idz == year:
                if not done:
                    print(f'{idx} * {idy} * {idz} = {idx*idy*idz}')
                    done = True
                    #exit()

print(f'\nCounter = {counter}')
print(f'Whole process: {time.time()-ts :.02f} sec')
