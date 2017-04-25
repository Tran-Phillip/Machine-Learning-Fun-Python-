import numpy as np
import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Practice kNN with the iris dataset

#import the dataset
path = "https://raw.githubusercontent.com/Tran-Phillip/Datasets/master/IntroStats.csv"
full_data_frame = pd.read_csv(path, header = 0)

#Scrubbing the data. 
full_data_frame = full_data_frame.dropna(axis = 'rows', how = 'any')


#impliment kNN with scikit learn
predictors = np.array(full_data_frame.ix[: , 8:10])
response = np.array(full_data_frame['hsGPA'])
pred_train, pred_test, res_train, res_test = train_test_split(predictors, response, test_size = .33, random_state = 42)

#create the nearest neighbor model with k = 10
knn = KNeighborsClassifier(n_neighbors = 10)

#FIST THE MODEL
knn.fit(pred_train.astype(str), res_train.astype(str))

#predict the responses 
fitted_val = knn.predict(pred_test)

#How accurate?

acc_score = accuracy_score(res_test.astype(str),fitted_val.astype(str))
print("This test has an accuracy score of: ",acc_score,"!\n")

def validate(math_score,english_score):
	#checks to see if user input was valid
	if math_score.isdigit() != True:
		return(False)
	if english_score.isdigit() != True:
		return(False)
	return(True)

valid_input = False #used to check input later

while True:
	math_score = None
	english_score = None
	gpa = None 

	#input the scores
	math_score = input("Input math SAT score (enter 0 to quit): " )
	english_score = input("Input english SAT score: ")
	valid_input = validate(math_score,english_score)
	if valid_input == False:
		print("Those are not valid inputs.\n")
		continue;

	gpa = knn.predict([[math_score,english_score]])

	#Prints for funsies 
	print("\nThe machine predicts your high school GPA to be ", gpa, "!\n")
	gpa = gpa.astype(float)
	if gpa > 3.5:
		print("Thats a pretty great GPA!")
	elif gpa > 3.0:
		print("Thats a pretty good GPA!")
	elif gpa > 2.5:
		print("Thats a pretty decent GPA!")
	elif gpa > 2.0:
		print("You made it past high school!")
	elif gpa == 0: 
		print("Wow! Your scores were so low that the machine doesn't consider the fact you exist!")
	else:
		print("Wow you suck!")
	choice = input("\nDo you want to quit (0 for yes, 1 for no): ")
	if choice == "0":
		exit()

# #impliment kNN with scikit learn
# predictors = np.array(df.ix[: ,0:4]) #numpy array of the first 4 columns (sepal_length, width, ect)
# response = np.array(df['class'])

# #split into a train test
# X_train, X_test, y_train, y_test = train_test_split(predictors, response, test_size = .33, random_state = 42)

# #create a nearest neighbor model with k = 3
# knn = KNeighborsClassifier(n_neighbors = 3)

# #FIST THE MODEL
# knn.fit(X_train, y_train)

# #predict the response
# pred = knn.predict(X_test)

# value = knn.predict([[5.1,3.5,1.4,.2]])
# print(value);

# #evaluate accuracy
# print(accuracy_score(y_test,pred))
