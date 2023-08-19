def outputToArray(Output):
    keyArray = []
    keyBool = False
    keyCount = 0

    rhythmArray = []
    rhythmBool = False
    rhythmCount = -1

    for char in Output:
        if(char == '"' and keyBool == False):
            keyBool = True
            keyArray.append('')
            rhythmCount += 1
            continue
        elif (char == '"'):
            keyBool = False
            keyCount += 1
            rhythmBool = True
            rhythmArray.append('')
            continue

        if (keyBool == True):
            keyArray[keyCount] += char

        if (rhythmBool == True and char == "|"):
            rhythmBool = False
        elif (rhythmBool == True and char != " "):
            rhythmArray[rhythmCount] += char

    print(keyArray, rhythmArray)
    return(keyArray, rhythmArray)
