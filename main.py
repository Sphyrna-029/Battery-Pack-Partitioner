import csv
import argparse
import textwrap
import matplotlib.pyplot as plt
from random import choice, randint


class BatteryCell:
    def __init__(self, id, mah):
        self.id = id
        self.mah = mah


parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
████████████████████████████████████
██                                ██
██  ████  ████  ████  ████  ████  ████
██  ████  ████  ████  ████  ████  ████
██  ████  ████  ████  ████  ████  ████
██  ████  ████  ████  ████  ████  ████
██  ████  ████  ████  ████  ████  ████
██                                ██
████████████████████████████████████
    - 18650 Cell Partitioner +'''))
parser.add_argument("-f", "--file", type=str, help="Input CSV file")
parser.add_argument("-p", "--parallel", type=int, help="Number of parallel packs in your battery")
parser.add_argument("-i", "--iterations", type=int, default=0,
                    help="Number of branch-&-bound iterations to optimize the result")
parser.add_argument("--hist", action='store_true',
                    help="Display a histogram with capacity distribution at the end of the process")
args = parser.parse_args()


groups = args.parallel
pool = []
groupTotal = [[] for _ in range(groups)]
nominalVoltage = 3.7

with open(args.file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        cell = BatteryCell(i+1, int(row['mAh']))
        pool.append(cell)

pool.sort(reverse=True, key=lambda x: x.mah)


# If extra cells are present in the list, remove the smallest ones
extra_cells = len(pool) % groups
if extra_cells != 0:
    pool = pool[:-extra_cells]


def getSmallestListIdx():  # Find the array with the smallest sum
    sumList = []
    for grp in groupTotal:
        sumList.append(sum(c.mah for c in grp))
    smallestList = sumList.index(min(sumList))
    return smallestList


for cell in pool:  # Iterate over our list of batteries and divy up the largest capacities to the smallest groups.
    smallIndex = getSmallestListIdx()
    groupTotal[smallIndex].append(cell)

# Quick stats
avg_mah = sum(c.mah for c in pool) / len(pool)
mAhSum = 0
for grp in groupTotal:
    mAhSum += sum(c.mah for c in grp)
groupAverage = mAhSum / len(groupTotal)


for _ in range(args.iterations):
    groupTotal.sort(key=lambda x: sum(c.mah for c in x))
    A, B = choice(groupTotal[:groups//2]), choice(groupTotal[groups//2:])
    i1, i2 = randint(0, 3), randint(0, 3)
    delta1 = abs(sum(c.mah for c in A) - sum(c.mah for c in B))
    A[i1], B[i2] = B[i2], A[i1]
    delta2 = abs(sum(c.mah for c in A) - sum(c.mah for c in B))

    if delta2 > delta1:
        A[i1], B[i2] = B[i2], A[i1]


print('Stats:')
print('  - Avg. Cell Capactiy:   %d mAh' % round(avg_mah))
print('  - Tot. Pack Capacity:   %d mAh' % round(groupAverage))
print('  - Pack Nominal Voltage: %d V' % round(len(groupTotal) * nominalVoltage, 2))
print('\n')


for idx, grp in enumerate(groupTotal):
    print('Group #%d (tot. %d mAh)' % (idx, sum(c.mah for c in grp)))
    for cell in grp:
        print('  - Cell N° %-3d - %5d mAh' % (cell.id, cell.mah))
    print()

if args.hist:
    plt.hist([sum(c.mah for c in grp) for grp in groupTotal])
    plt.title("Distribution of pack capacity")
    plt.xlabel("Pack capacity (mAh)")
    plt.ylabel("Num. of packs")
    plt.show()
