file = open("./input", 'r')

values = file.read()

splitedValues = values.split(",")

crabPos = []

for values in splitedValues:
    crabPos.append(int(values))

biggestValue = max(crabPos)
smallestValue = min(crabPos)

minFuel = 100000000

for i in range(smallestValue, biggestValue):
    fuel = 0
    for pos in crabPos:
        tmp = abs(pos - i)
        for j in range(0, tmp + 1):
            fuel += j
    if (fuel < minFuel):
        minFuel = fuel

print(minFuel)