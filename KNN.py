import classes
from classes import SATpoint
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#implimenting my own KNN algorithm 

#import the dataset
path = "https://raw.githubusercontent.com/Tran-Phillip/Datasets/master/IntroStats.csv"
full_data_frame = pd.read_csv(path, header = 0)

#Scrubbing the data. 
full_data_frame = full_data_frame.dropna(axis = 'rows', how = 'any')

#split into a train-test
predictors = np.array(full_data_frame.ix[: , 8:10])
response = np.array(full_data_frame['hsGPA'])
pred_train, pred_test, res_train, res_test = train_test_split(predictors, response, test_size = .33, random_state = 42)

#create each individual datapoint and add them to a list of points
data_points = []

for i in range(pred_train.shape[0]):
	hsGPA = res_train[i]
	SATV = pred_train[i][1]
	SATM = pred_train[i][0]
	point = SATpoint(SATV, SATM, hsGPA, 0)
	data_points.append(point)

#create a function that adds the distaces from a given point to every other point
def get_neighbors(point1, data_points):
	#point1 -> the given test point
	#data_points -> the list of data points 
	updated_points = []
	for point in data_points:
		point.dist = point.calc_dist(point1)
		updated_points.append(point)
    #Sort the points.
	updated_points.sort(key=lambda point: point.dist, reverse = False)
	#yes I know this could be combined with the loop above. Shhh
	return(updated_points)

#Now do the k-NN
while(True):
	neighbors = input("Input number of neighbors do you want to use: ")
	math_score = input("Input math SAT score: ")
	read_score = input("Input reading SAT score: ")
	dist = []
	SAT_test = [math_score, read_score]
	dist = get_neighbors(SAT_test, data_points)

	nearest_neighbors = []
	#grab the first "k" points
	for point in dist[1:int(neighbors)]:
		GPA = point.hsGPA
		point.print()
		nearest_neighbors.append(GPA)
	prediction = np.mean(nearest_neighbors)
	print("We predict your HS GPA to be: ", round(prediction,2), "\n")
	cont = input("Continue? (y/n)")
	if cont ==  "y":
		continue;
	else:
		break





