
def BalancedAB(string):
    matchA = 'A'
    matchB = 'B'
    if((checkValidString(string)) == False): #check if string is valid
        return 'Error, enter a string'
    else:
        if((checkForChar(string,matchA)) == False):#if a is not present then it is true
             return True
        else:
            indexA = getIndex(string,matchA)

            if((checkForChar(string,matchB)) == True):
                matchB = 'B'
                indexB = getIndex(string,matchB)

                if(indexB > indexA):
                    return True
                else:
                    return False
            else:
                return False

def checkValidString(string):
    testString = 'test'
    inputType = type(string)
    string = type(testString)
    if(inputType == string):
        return True
    else:
        return False


def checkForChar(string,char):
    result = False
    if char in string:
        result = True
    return result

def getIndex(string,match):
    index = string.rindex(match)
    return index


print(BalancedAB('AB'))







