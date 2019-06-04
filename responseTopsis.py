import numpy as np
import math

class topsis:
	
	def __init__(self,alternatives,criteria,weights,idealSolution,margins,ranges):
		self.alternatives = alternatives
		self.criteria = criteria
		self.weights = weights
		self.InitialidealSolution = idealSolution
		self.margins = margins
		self.ranges = ranges
		self.col = len(criteria)
		self.row = len(alternatives)
		self.weightedMatrix = np.zeros((len(alternatives),len(criteria)))
		self.weightedIdeal = np.array([[0.0, 0.0, 0.0, 0.0]])
		self.distIdealSolution = np.zeros((len(alternatives),len(criteria)))
		self.decisionMatrix = np.array([[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]])
		self.idealSolution = np.array([[0.0, 0.0, 0.0, 0.0]])
		self.Si = np.zeros((1,len(alternatives)))
		self.sortedSi = np.zeros((1,len(alternatives)))
		
	def define_policy_values(self): 
		self.initialdecisionMatrix = np.array([[6, 5, 4, 1], [5, 9, 2, 7], [1, 8, 3, 8]])
		print("----Matrix with policy values----")
		print(self.initialdecisionMatrix)
		print("\n")
		self.normalizationOfDM()
		
	def normalizationOfDM(self):
		for i in range(self.col):
			for j in range(self.row):
				n = (self.initialdecisionMatrix[j][i]-1)/(self.ranges[0][i])
				self.decisionMatrix[j][i] = n	
		for i in range(self.col):
			nn = (self.InitialidealSolution[0][i]-1)/(self.ranges[0][i])
			self.idealSolution[0][i] = nn
		print("----Normalized DM----")
		print(self.decisionMatrix)
		print("\n") 
		print("----Normalized CV----")
		print(self.idealSolution)
		print("\n")	
		self.combineWeights()
	
	def combineWeights(self):
		for i in range(self.col):
			for j in range(self.row):
				self.weightedMatrix[j][i] = self.decisionMatrix[j][i]*self.weights[0][i]
		print("----Weighted Matrix----")
		print(self.weightedMatrix)
		print("\n")
		self.combineWeightsIdealSolution()
		
	def combineWeightsIdealSolution(self):
		for i in range(self.col):
			self.weightedIdeal[0][i] = self.weights[0][i]*self.idealSolution[0][i]
		print("----Ideal Solution Matrix----")
		print(self.idealSolution)
		print("\n")
		print("----Ideal Solution Weighted Matrix----")
		print(self.weightedIdeal)
		print("\n")
		self.distance()
	
	def distance(self):
		for i in range(self.row):
			for j in range(self.col):
				self.distIdealSolution[i][j] = (self.weightedMatrix[i][j]-self.weightedIdeal[0][j])**2
		
		for i in range(self.row):
			sum1 = 0
			for j in range(self.col):
				sum1 = sum1 + self.distIdealSolution[i][j] 
			self.Si[0][i] = math.sqrt(sum1)
		
		#print(self.distIdealSolution)
		print("----Distance from Ideal Solution----")
		print(self.Si)
		print("\n")
		self.sortedSi = np.argsort(self.Si)
		print(self.sortedSi)
		
		#range definition
		print(self.Si[0][self.sortedSi[0][0]])
		print(self.margins[0][self.sortedSi[0][0]])
		if(self.Si[0][self.sortedSi[0][0]] <= self.margins[0][self.sortedSi[0][0]]):
			print("Role is: " + alternatives[self.sortedSi[0][0]])
		elif(self.Si[0][self.sortedSi[0][1]] <= self.margins[0][self.sortedSi[0][1]]):
			print("Role is: " + alternatives[self.sortedSi[0][1]])
		elif(self.Si[0][self.sortedSi[0][2]] <= self.margins[0][self.sortedSi[0][2]]):
			print("Role is: " + alternatives[self.sortedSi[0][2]])
		else:
			print("Undefined")
	
alternatives = ["manager","employee","intern"]
criteria = ["department","identifier","time","connectionType"]
weights = np.array([[0.4, 0.4, 0.1, 0.1]])
idealSolution = np.array([[5, 5, 4, 1]])
margins = np.array([[0.01, 0.05, 0.15]])
ranges = np.array([[19.0, 99.0, 7.0, 9.0]])
result = topsis(alternatives,criteria,weights,idealSolution,margins, ranges)
result.define_policy_values()