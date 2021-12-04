file = open("./input2", 'r')

values = file.read()

formatedValues = values.split("\n\n")
bingoNumbers = formatedValues[0]

formatedValues.pop(0)

bingoNumbers = bingoNumbers.split(",")
bingoGridArray = []
endNbr = 0
endGrid = 0
alreadyGrid = []

for value in formatedValues:
    bingoGrid = value.split("\n")
    numberLine = []
    for number in bingoGrid:
        numberLine.append(number.split())
    bingoGridArray.append(numberLine)

completedGrid = []

for grid in bingoGridArray:
    completedGrid.append([["o", "o", "o", "o", "o"],
    ["o", "o", "o", "o", "o"],
    ["o", "o", "o", "o", "o"],
    ["o", "o", "o", "o", "o"],
    ["o", "o", "o", "o", "o"]])

def testAlready(nbr):
    for number in alreadyGrid:
        if (nbr == number):
            return 1
    return 0

def isEnd(gridArray):
    for gridIndex in range(len(gridArray)):
        for lineIndex in range(0, 5):
            count = 0
            for itemIndex in range(0, 5):
                if (gridArray[gridIndex][lineIndex][itemIndex] == "x"):
                    count += 1
            if (count == 5 and testAlready(gridIndex) == 0):
                return 1

        for rowIndex in range(0,5):
            count = 0
            for itemIndex in range(0, 5):
                if (gridArray[gridIndex][itemIndex][rowIndex] == "x"):
                    count += 1
            if (count == 5 and testAlready(gridIndex) == 0):
                return 1
    return 0

for bingoNumber in bingoNumbers:
    endNbr = bingoNumber
    for bingoGridIndex in range(len(bingoGridArray)):
        endGrid = bingoGridIndex
        for lineIndex in range(len(bingoGridArray[0])):
            for numberIndex in range(len(bingoGridArray[0][0])):
                if (bingoGridArray[bingoGridIndex][lineIndex][numberIndex] == bingoNumber):
                    completedGrid[bingoGridIndex][lineIndex][numberIndex] = "x"
        if(isEnd(completedGrid) != 0):
            alreadyGrid.append(endGrid)
    if(len(alreadyGrid) == 99):
        break

alreadyGrid.sort()
notAlready = []

for bingoGridIndex in range(len(bingoGridArray)):
    no = 0
    for already in alreadyGrid:
        if (int(already) == bingoGridIndex):
            no = 1
    if (no == 0):
        notAlready.append(bingoGridIndex)

sum = 0

for lineIndex in range(len(bingoGridArray[91])):
    for numberIndex in range(len(bingoGridArray[91][0])):
        if (completedGrid[91][lineIndex][numberIndex] == "o"):
            sum += int(bingoGridArray[91][lineIndex][numberIndex])
print(sum - 97 * 97)

