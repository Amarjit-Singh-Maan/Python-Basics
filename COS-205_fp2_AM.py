# Amarjit Maan
# COS 205, Python Programming
# Problem # 2

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    #print(nums)

def sumList(nums):
    total = 0
    for num in nums:
        total = total + num
    return total

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
       

fName = input("Enter filename: ")
infile = open(fName,'r')
line = infile.readlines()

for l in line: # each line
    strList = l.rstrip().split(' ')
    
toNumbers(strList)
squareEach(strList)
total = sumList(strList)
print(total)
