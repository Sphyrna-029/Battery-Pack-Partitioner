import csv
import argparse
import textwrap


class BatteryCell:
    def __init__(self, name, mah):
        self.name = name
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
parser.add_argument("-f", "--file", type=str, help="Input CSV file.")
parser.add_argument("-p", "--parallel", type=int, help="Number of parallel packs in your battery.")
args = parser.parse_args()

inputfile = args.file
groups = args.parallel

pool = []
groupTotal = [[] for _ in range(groups)]
nominalVoltage = 3.7

with open(inputfile, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        cell = BatteryCell(i+1, int(row['mAh']))
        pool.append(cell)

pool.sort(reverse=True, key=lambda x: x.mah)


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

print('Stats:')
print('  - Avg. Cell Capactiy:   %d mAh' % round(avg_mah))
print('  - Tot. Pack Capacity:   %d mAh' % round(groupAverage))
print('  - Pack Nominal Voltage: %d V' % round(len(groupTotal) * nominalVoltage, 2))
print('\n')


for idx, grp in enumerate(groupTotal):
    print('Group #%d (tot. %d mAh)' % (idx, sum(c.mah for c in grp)))
    for cell in grp:
        print('  - Cell N° %-3d - %5d mAh' % (cell.name, cell.mah))
    print()
