from telnetlib import EC
from Elf import Elf

#adventofcode.com/2022/day/1
#
#stream reader to string called transalated
#string seperate by /n into array
#
#Elf object {inventory[], inventory total}
#
#elves Elf[];
#elf=__init__();
#while loop through string objects
# if n=="\n" and n==n+1 then start new elf and add to elves[]
# else elf.addInventory(n)
# int most = elves[0].getTotal()
#for each elf in elves
# if most<n.getTotal then most=n.getTotal
#println(most)

file_str = open('Inventory.txt','r').read()
file_list = file_str.split("\n")
elf = Elf()
elves = [elf]

for n in file_list:
    if n=="":
        elf = Elf()
        elves.append(elf)
    else:
        Elf.addInventory(elf, n)

#part one
"""
most = Elf.__getattribute__(elves[0], 'totalCals')
for e in elves:
    if most < Elf.__getattribute__(e, 'totalCals'):
        most = Elf.__getattribute__(e, 'totalCals')

print(most)
"""
#part two
topThree = [0,0,0]
for e in elves:
    eCals = Elf.__getattribute__(e, 'totalCals')
    if eCals > topThree[0]:
        topThree[2] = topThree[1]
        topThree[1] = topThree[0]
        topThree[0] = eCals
    elif eCals > topThree[1]:
        topThree[2] = topThree[1]
        topThree[1] = eCals
    elif eCals > topThree[0]:
        topThree[0] = eCals

total = topThree[0]+topThree[1]+topThree[2]
print(total)

input()    
