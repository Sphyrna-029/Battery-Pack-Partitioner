import csv
import argparse
import textwrap

pool = []    

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

#Our cell groups (added small ints so loop knows where to start)
groupA = [0.0001] 
groupB = [0.0002]
groupC = [0.0003]

avg_mah = sum(pool) / len(pool)
print('Average mAh: ' + str(avg_mah))

pool.sort(reverse = True) 

for x in pool: #Iterate over our list of batteries and divy up the largest capacities to the smallest groups. 
    smollest = [sum(groupA), sum(groupB), sum(groupC)] #Find the array with the smallest value
    smol = smollest.index(min(smollest)) #Get the index of that value so we know which array is the smallest, we can then map 0-groupA, 1-groupB, etc.

    if smol == 0:
        groupA.append(x)

    if smol == 1:
        groupB.append(x)

    if smol == 2:
        groupC.append(x)

print('Group A: ' + str(sum(groupA)))
print(str(groupA) + '\n')
print('Group B: ' + str(sum(groupB)))
print(str(groupB) + '\n')
print('Group C: ' + str(sum(groupC)))
print(str(groupC) + '\n')
avg = sum(groupA) + sum(groupB) + sum(groupC)

avg = avg / 3

print('Group average: ' + str(avg))
