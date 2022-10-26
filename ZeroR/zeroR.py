import pandas as pd # Read csv file
import functions as fun #functions.py

CLASS_NAME = 'Clase' # Write the class header of your database here
CSV_FILE = 'db.csv' # Write your csv name here

df = pd.read_csv(CSV_FILE) # dataFrame = csv file
headerClass = df[CLASS_NAME] # headerClass = [acc,acc,unacc,unacc... ]
classUniqueValues = headerClass.unique() # [acc,unacc,good]
sizeClassUniqueValues = len(classUniqueValues) # 3

print('Database: ')
print(df.to_string()) 
fun.Clear()

iterations = int(input('Iterations: ')) # Number of times to evaluate the database
for i in range (iterations):
    print('Iteration:',i+1,'°\nTrain program with all database:')
    classTable = fun.TrainProgram(df, sizeClassUniqueValues, headerClass, classUniqueValues) #df = all database
    fun.Predictions(df, classTable, classUniqueValues, headerClass)
    print('In order to develop prediction capacities the program needs 70% of data for training and 30% for testing:')
    seventyList, completeRowsList = fun.Get7030(df)
    fun.Predictions7030(classTable, sizeClassUniqueValues, seventyList, headerClass, classUniqueValues, completeRowsList)
