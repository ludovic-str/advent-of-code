file = open("./value", 'r')

values = file.read()

depth = 0
forward = 0
aim = 0

valuesArray = values.split("\n")

for value in valuesArray:
    splitedValue = value.split()
    if (splitedValue[0] == "forward"):
        forward += int(splitedValue[1])
        depth += int(splitedValue[1]) * aim
    if (splitedValue[0] == "up"):
        aim -= int(splitedValue[1])
    if (splitedValue[0] == "down"):
        aim += int(splitedValue[1])

print(depth * forward)
