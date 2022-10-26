import os # os.system('cls')
import random # random.sample  

def Clear(): # Clear console
    input('Press return to continue...')
    os.system('cls')

def TrainProgram(database, sizeClassUniqueValues, headerClass, classUniqueValues):
    classTable = [0] * sizeClassUniqueValues # [0,0,0]
    for i in range (database.shape[0]): # For each row in our database
        for j in range (sizeClassUniqueValues):
            if(headerClass[i] == classUniqueValues[j]): # If current class value == class unique value
                classTable[j] += 1 # Increase +1 [1,0,0]
    print('\nClass:')
    print(classUniqueValues)
    print(classTable)
    return classTable

def Predictions(database, classTable, classUniqueValues, headerClass):
    maxClassValue = max(classTable)
    index = classTable.index(maxClassValue) # Get maxClassValue position
    print('Max class value: "',classUniqueValues[index],'"')
    Clear()
    print('\nPredictions with all database:\n')
    hits = 0
    for i in range (database.shape[0]):
        print('ID:',i,'expected value: "',classUniqueValues[index],'" result: "',headerClass[i],'"')
        if(classUniqueValues[index] == headerClass[i]): # If max class value == current row class value
            print('Correct')
            hits +=1
        else:
            print('Incorrect')
    print('Hits:',hits,'of', database.shape[0])
    print('Accuracy: ',(hits * 100) / database.shape[0],'%')
    Clear()

def Get7030(database):
    seventy = round(database.shape[0] * 0.70) # Number of 70% rows 
    completeRowsList = list(range(0,database.shape[0])) # Range (0 to rows)
    seventyList = list(random.sample(completeRowsList,seventy)) # List of 70% random index rows

    for i in range(seventy):
        if(seventyList[i] in completeRowsList):
            completeRowsList.remove(seventyList[i])
    seventyList.sort()
    completeRowsList.sort() # Now 30% index rows
    print('Training IDS:',seventyList) # 70%
    print('Testing IDS:',completeRowsList) # 30%
    input('\n\nPress return to continue...\n')
    return seventyList, completeRowsList

def Predictions7030(classTable, sizeClassUniqueValues, seventyList, headerClass, classUniqueValues, completeRowsList):
    classTable = [0] * sizeClassUniqueValues # Initialize class table [0,0...]
    for i in range (len(seventyList)):
        for j in range (sizeClassUniqueValues):
            if(headerClass[seventyList[i]] == classUniqueValues[j]):
                classTable[j] += 1
    print('Train program with 70% database:\nClass:')
    print(classUniqueValues)
    print(classTable)
    maxClassValue = max(classTable) 
    index = classTable.index(maxClassValue)
    print('Max class value: "',classUniqueValues[index],'"')
    Clear()

    print('\nTesting with 30% data:')
    hits = 0
    for i in range (len(completeRowsList)):
        print('ID:',completeRowsList[i],'expected value: "',classUniqueValues[index],'" result: "',headerClass[completeRowsList[i]],'"')
        if(classUniqueValues[index] == headerClass[completeRowsList[i]]):
            print('Correct')
            hits +=1
        else:
            print('Incorrect')
    print('Hits:',hits,'of', len(completeRowsList))
    print('Accuracy',(hits * 100) / len(completeRowsList), '%')
    Clear()
    