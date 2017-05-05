class SATpoint:
	""" Contains the SATM, SATV, hsGPA """
	import math 
	def __init__(self, V,M,GPA, dist1):
		self.SATV = V 
		self.SATM = M
		self.hsGPA = GPA
		self.dist = dist1
		self.mtx = [M , V]

	def calc_dist(self, point):
		"""Calculates the distance between two points"""
		dist = 0
		for i in range(len(point)):
			temp = (int(self.mtx[i]) - int(point[i]))**2
			dist += temp
		return(dist**(1/2)) 

	def print(self):
		print("SATV: ", self.SATV, "\nSATM: ", self.SATM, "\nGPA: ", self.hsGPA, "\nDist: ", self.dist, "\n")

