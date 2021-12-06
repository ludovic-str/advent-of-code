file = open("./input", 'r')

values = file.read()

valuesArray = values.split("\n")

map = []
for i in range(0, 1000):
    line = ""
    for j in range(0, 1000):
        line += "."
    map.append(line)

def handleHorizontale(begin, end, line):
    i = begin
    if (i < end):
        while (i <= end):
            if (map[line][i] == "."):
                tmp = list(map[line])
                tmp[i] = "1"
                map[line] = "".join(tmp)
            else:
                tmp = list(map[line])
                newValue = int(map[line][i]) + 1
                tmp[i] = str(newValue)
                map[line] = "".join(tmp)
            i += 1
    else:
        while (i >= end):
            if (map[line][i] == "."):
                tmp = list(map[line])
                tmp[i] = "1"
                map[line] = "".join(tmp)
            else:
                tmp = list(map[line])
                newValue = int(map[line][i]) + 1
                tmp[i] = str(newValue)
                map[line] = "".join(tmp)
            i -= 1

def handleVertical(begin, end, column):
    i = begin
    if (i < end):
        while (i <= end):
            if (map[i][column] == "."):
                tmp = list(map[i])
                tmp[column] = "1"
                map[i] = "".join(tmp)
            else:
                tmp = list(map[i])
                newValue = int(map[i][column]) + 1
                tmp[column] = str(newValue)
                map[i] = "".join(tmp)
            i += 1
    else:
        while (i >= end):
            if (map[i][column] == "."):
                tmp = list(map[i])
                tmp[column] = "1"
                map[i] = "".join(tmp)
            else:
                tmp = list(map[i])
                newValue = int(map[i][column]) + 1
                tmp[column] = str(newValue)
                map[i] = "".join(tmp)
            i -= 1

def handleDiag(pointArray):
    for point in pointArray:
        if (map[point[1]][point[0]] == "."):
                tmp = list(map[point[1]])
                tmp[point[0]] = "1"
                map[point[1]] = "".join(tmp)
        else:
            tmp = list(map[point[1]])
            newValue = int(map[point[1]][point[0]]) + 1
            tmp[point[0]] = str(newValue)
            map[point[1]] = "".join(tmp)

for value in valuesArray:
    splitedValue = value.split("->")
    beginValue = splitedValue[0].split(",")
    endValue = splitedValue[1].split(",")
    if (int(beginValue[0]) == int(endValue[0]) or int(beginValue[1]) == int(endValue[1])):
        if (int(beginValue[1]) == int(endValue[1])):
            handleHorizontale(int(beginValue[0]), int(endValue[0]), int(endValue[1]))
        else:
            handleVertical(int(beginValue[1]), int(endValue[1]), int(endValue[0]))
    else:
        if (int(beginValue[0]) < int(endValue[0])):
            firstList = list(range(int(beginValue[0]), int(endValue[0]) + 1))
        else:
            firstList = list(range(int(endValue[0]), int(beginValue[0]) + 1))
            firstList.reverse()
        if (int(beginValue[1]) < int(endValue[1])):
            secondList = list(range(int(beginValue[1]), int(endValue[1]) + 1))
        else:
            secondList = list(range(int(endValue[1]), int(beginValue[1]) + 1))
            secondList.reverse()
        finalList = []
        for index in range(len(firstList)):
            finalList.append([firstList[index], secondList[index]])
        handleDiag(finalList)

count = 0

for line in map:
    for elem in line:
        if (elem != "." and int(elem) >= 2):
            count += 1

print(count)
