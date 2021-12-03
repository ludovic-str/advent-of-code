file = open("./input", 'r')

values = file.read()

formatedValues = values.split("\n")

moreList = formatedValues
lessList = formatedValues


for i in range(0, len(moreList)):
    if(len(moreList) == 1):
        break
    zero = 0
    one = 0
    for value in moreList:
        if (int(value[i]) == 0):
            zero += 1
        if (int(value[i]) == 1):
            one += 1
    if (one >= zero):
        newList = []
        for j in range(0, len(moreList)):
            if(int(moreList[j][i]) != 0):
                newList.append(moreList[j])
        moreList = newList
    else:
        newList = []
        for j in range(0, len(moreList)):
            if(int(moreList[j][i]) != 1):
                newList.append(moreList[j])
        moreList = newList

for i in range(0, len(lessList)):
    if(len(lessList) == 1):
        break
    zero = 0
    one = 0
    for value in lessList:
        if (int(value[i]) == 0):
            zero += 1
        if (int(value[i]) == 1):
            one += 1
    if (one < zero):
        newList = []
        for j in range(0, len(lessList)):
            if(int(lessList[j][i]) != 0):
                newList.append(lessList[j])
        lessList = newList
    else:
        newList = []
        for j in range(0, len(lessList)):
            if(int(lessList[j][i]) != 1):
                newList.append(lessList[j])
        lessList = newList

print(int(moreList[0], 2) * int(lessList[0], 2))