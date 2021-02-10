pool = [10, 20, 5, 2, 50, 7, 32, 90, 75, 1] #our pool of batteries

#Our cell groups (added small ints so loop knows where to start)
groupA = [0.0001] 
groupB = [0.0002]
groupC = [0.0003]

print('Average mAh: ' + str(sum(pool) / len(pool)))

pool.sort(reverse = True) 

for x in pool: #Iterate over our list of batteries and divy up the largest capacities to the smallest groups. 
    smollest = [sum(groupA), sum(groupB), sum(groupC)] #Find the array with the smallest value
    smolIndex = smollest.index(min(smollest)) #Get the index of that value so we know which array is the smallest, we can then map 0-groupA, 1-groupB, etc.

    if smolIndex == 0:
        groupA.append(x)

    if smolIndex == 1:
        groupB.append(x)

    if smolIndex == 2:
        groupC.append(x)

print(pool)


print('Group A: ' + str(sum(groupA)))
print(groupA)
print('Group B: ' + str(sum(groupB)))
print(groupB)
print('Group C: ' + str(sum(groupC)))
print(groupC)
avg = sum(groupA) + sum(groupB) + sum(groupC)

avg = avg / 3

print('Group average: ' + str(avg))
