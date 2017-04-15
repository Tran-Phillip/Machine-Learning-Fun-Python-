	
import numpy as np
import pandas as pd 
from sklearn import tree
from IPython.display import Image
from sklearn.externals.six import StringIO
import pydotplus as pydot
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


#Attempts to predict GPA from Math SAT score and Vocab SAT score (Wheres the writing score Melcon? Smh)

input_file = "https://raw.githubusercontent.com/Tran-Phillip/Datasets/master/IntroStats.csv"
#the entire set not subsetted yet
full_data_frame = pd.read_csv(input_file, header = 0)




#Scrubbing the data. 
full_data_frame['hsGPA'] = full_data_frame['hsGPA'].fillna(full_data_frame['hsGPA'].mean()) #Fill the NaN with the means
full_data_frame['SATM'] = full_data_frame['SATM'].fillna(full_data_frame['SATM'].mean())
full_data_frame['SATV'] = full_data_frame['SATV'].fillna(full_data_frame['SATV'].mean())

#split into train test
train, test = train_test_split(full_data_frame, test_size = .33, random_state = 43) 


#Contains the labels from the SATM and SATV score
SAT_frame = list(full_data_frame.columns[8:10]); 

hsGPA = train["hsGPA"] #high school gpa
SAT_scores = train[SAT_frame] #SAT scores



clf = tree.DecisionTreeClassifier() #create the classifier (Obj that contains decision tree stuff)
clf.fit(SAT_scores.astype(str),hsGPA.astype(str)) #Create a line of best fit 

#Stuff that lets me print out the graphs 
# dot_data = StringIO()
# tree.export_graphviz(clf,out_file = dot_data, feature_names = SAT_frame)
# graph = pydot.graph_from_dot_data(dot_data.getvalue())
# graph.write_png('PredictionGraph.png')

clf = RandomForestClassifier(n_estimators = 10)
clf.fit(SAT_scores.astype(str), hsGPA.astype(str))

##actually user prompt time
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

	#Gets rid of brackets
	gpa = clf.predict([[math_score,english_score]])
	if gpa == None:
		gpa = 0;
	
	gpa = gpa.astype(str)

	
	

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



