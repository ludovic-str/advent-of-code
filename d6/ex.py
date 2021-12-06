file = open("./input", 'r')

values = file.read()

splitedValues = values.split(",")

fishs = [0] * 9

for value in splitedValues:
    fishs[int(value)] += 1

for i in range(0, 256):
    birth = fishs[0]
    fishs[0] = 0
    for fishIndex in range(0, 8):
        fishs[fishIndex] = fishs[fishIndex + 1]
    fishs[8] = birth
    fishs[6] += birth

print(fishs)
print(sum(fishs))

