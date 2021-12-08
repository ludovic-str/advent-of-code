file = open("./input", 'r')

values = file.read()

splitedValues = values.split("\n")

digitKeys = ["", "", "", "", "", "", "", "", "", ""]

def countCommon(str1, str2):
    count = 0
    for letter in str1:
        if letter in str2:
            count += 1
    return count

result = 0

for index in range(0, len(splitedValues)):
    digitStr = splitedValues[index].split("|")[0].split()
    output = splitedValues[index].split("|")[1].split()
    for digit in digitStr:
        if (len(digit) == 2):
            digitKeys[1] = digit
        if (len(digit) == 4):
            digitKeys[4] = digit
        if (len(digit) == 3):
            digitKeys[7] = digit
        if (len(digit) == 7):
            digitKeys[8] = digit

    for digit in digitStr:
        if (len(digit) == 5):
            if countCommon(digitKeys[1], digit) == 2:
                digitKeys[3] = digit
            if countCommon(digitKeys[4], digit) == 3 and countCommon(digitKeys[1], digit) != 2:
                digitKeys[5] = digit
            if countCommon(digitKeys[4], digit) != 3 and countCommon(digitKeys[1], digit) != 2:
                digitKeys[2] = digit
        if (len(digit) == 6):
            if countCommon(digitKeys[1], digit) == 1:
                digitKeys[6] = digit
            if countCommon(digitKeys[4], digit) == 4:
                digitKeys[9] = digit
            if countCommon(digitKeys[4], digit) != 4 and countCommon(digitKeys[1], digit) != 1:
                digitKeys[0] = digit
    finalDigit = ""
    for digit in output:
        for keyIndex in range(len(digitKeys)):
            if set(digitKeys[keyIndex]) == set(digit):
                finalDigit += str(keyIndex)
    result += int(finalDigit)

print(result)
