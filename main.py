import csv
import argparse
import textwrap

pool = []    
groupTotal = []
nominalVoltage = 3.7

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
parser.add_argument("-p", "--parrallel", type=int, help="Number of parrallel packs in your battery.")
args = parser.parse_args()

inputfile = args.file
groups = args.parrallel

with open(inputfile, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pool.append(int(row['mAh']))

pool.sort(reverse = True) 

for x in range(groups):
    cellGroup = []
    cellGroup.append(x * 0.05)
    groupTotal.append(cellGroup)

def getSmallest(x): #Find the array with the smallest sum.
    sumList = []
    for x in groupTotal:
        sumList.append(sum(x))
    smallestList = sumList.index(min(sumList))
    return smallestList

for x in pool: #Iterate over our list of batteries and divy up the largest capacities to the smallest groups. 
    smallIndex = getSmallest(groupTotal)
    groupTotal[smallIndex].append(x)

#Quick stats
avg_mah = sum(pool) / len(pool)
mAhSum = 0
for x in groupTotal:
    mAhSum += sum(x)
groupAverage = mAhSum / len(groupTotal)

print('==================================')
print('=========== Statistics ===========')
print('==================================')
print('Average Cell Capactiy: ' + str(round(avg_mah)) + 'mAh')
print('Total Pack Capacity: ' + str(round(groupAverage)) + 'mAh')
print('Pack Nominal Voltage: ' + str(round(len(groupTotal) * nominalVoltage, 2)) + 'v')
print('\n')


for x in groupTotal:
    x.pop(0)
    print('==================================')
    print('Group ' + str(groupTotal.index(x)))
    print('Total mAh: ' + str(sum(x)))
    print('Cells: ' + str(x))
    print('==================================\n')
