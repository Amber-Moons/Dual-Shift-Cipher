
def encodeInt(int1, int2):
    encodedInt = int1 + int2
    if encodedInt > codeNum:
        encodedInt -= codeNum
    return encodedInt

def decodeInt(int1, int2):
    decodedInt = int1 - int2
    if decodedInt < 1:
        decodedInt += codeNum
    return decodedInt

def findfromInt(outPutInt):
    encodedLet = key[outPutInt]
    outPut.co(encodedLet)

def type():
    typeV = input("Type 1 for encrypt, 2 for decrypt: ")
    if int(typeV) == 1:
        return 1
    elif int(typeV) == 2:
        return 2
    else:
        print("Type a valid number")
        return 3

def plainGet():
    plainTxtIn = input("Enter plain text: ")
    plainTxtList = list(plainTxtIn)
    plainTxtClear = [s for s in plainTxtList if s.strip()]
    keyfail = set(plainTxtClear) - set(keySort)
    if keyfail:
        print(f"Plain text contains values not in key: {keyfail}")
    return plainTxtClear
    
        
keyBase = [None]
key = list("abcdefghijlmnopqrstuvwxyz")
#key = input("Enter key: ")
keySort = keyBase + key
testkey = (len(set(keySort)) == len(keySort))
if testkey == False:
    print("Key contains duplicates please try again")
codeNum = len(keySort) - 1
typeV = 3
plainText = 0
while typeV == 3:
    typeV = type()
if typeV == 1:
    plainFail = 1
    while plainFail == 1:
        plainText = plainGet()
        if plainText != 0:
            plainFail = 0
print(plainText)
quit