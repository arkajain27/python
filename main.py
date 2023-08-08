'''
import sequencesolver

def getList(sequence):
    try:
        list1=sequence.split(',')
        sequenceList=list(map(int, list1))
        return sequenceList
    except:
        return -1

def isQuad(numberList):
    if len(numberList)>=4:
        diff = numberList[2]-2*numberList[1]+numberList[0]
        for i in range(1, len(numberList)-2):
            if (numberList[i+2]-2*numberList[i+1]+numberList[i] != diff):
                return False
            return True
        else:
            return False

def isLinear(numberList):
    if len(numberList)>=3:
        diff = numberList[1]-numberList[0]
        for i in range(1, len(numberList)-1):
            if (numberList[i+1]-numberList[i] != diff):
                return False
            return True
        else:
            return False

quad = sequencesolver.Quadratic()
linear = sequencesolver.Linear()

f = open ('sequences.txt', 'r')

for line in f:
    myList = getList(line)
    if (myList == -1):
        print('\n[%s] is not a linear/quadratic sequence' % (line.strip()))
    else:
        if  isLinear(myList):
            linear.numberList = myList
            print(linear)  
            print(linear.findFormula())
        elif isQuad(myList):
            quad.numberList = myList
            print(quad)
            print(quad.findFormula())
        else:
            print('\n[%s] is not a linear/quadratic sequence' % (line.strip()))

f.close()
'''