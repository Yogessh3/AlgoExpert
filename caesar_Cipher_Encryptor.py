'''
TimeComplexity O(N) / SpaceComplexity O(N)
This approach works only for lowercase letters properly since we have %122
'''
def caesarCipherEncryptor(word,key):
    newKey=key%26
    encryptedWord=[]
    for char in word:
        newLetter=getNewLetter(char,newKey)
        encryptedWord.append(newLetter)
    return "".join(encryptedWord)
def getNewLetter(char,newKey):
    newLetterValue=ord(char)+newKey
    if(newLetterValue<=122):
        return chr(newLetterValue)
    return chr(96+newLetterValue%122)
string="yogessh"
key=2
print(caesarCipherEncryptor(string,key))
    
    
    
        
    
