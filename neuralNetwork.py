# neuralNetwork.py
# Authors: Logan Anderson
# Written for CS445, Spring 2022

# This is the nearal network appoach to finding stable seeds

import numpy as np

class neuralNetwork:
    
    def __init__(self, sideLength, hiddenLayerSize):
        self.worldSize = int(sideLength**2)
        #For the following lists, [0] is for the input layer and [1] is the hidden layer
        self.weights = []
        self.weights.append((np.random.rand(self.worldSize, hiddenLayerSize) * 0.1) - 0.05)
        self.weights.append((np.random.rand(hiddenLayerSize, self.worldSize) * 0.1) - 0.05)
        self.biases = []#Biases are using an implied 1. Since 1*w = w, the biases value is just w
        self.biases.append((np.random.rand(hiddenLayerSize) * 0.1) - 0.05)
        self.biases.append((np.random.rand(self.worldSize) * 0.1) - 0.05)
        self.weightChange = []
        self.weightChange.append(np.zeros([self.worldSize, hiddenLayerSize]))
        self.weightChange.append(np.zeros([hiddenLayerSize, self.worldSize]))
        self.biasesChange = []
        self.biasesChange.append(np.zeros(hiddenLayerSize))
        self.biasesChange.append(np.zeros(self.worldSize))
        self.momentum = 0.9
        self.learningRate = 0.1

    def sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-x)) #np.exp is better than ** cause you can pass it a vector/matrix

    def applyWeights(self, inputGame):
        sideLen = int(np.sqrt(self.worldSize))
        newGame = []
        for i in range(sideLen):
            newGame.append([[] for x in range(sideLen)])

        inputGameArray = []
        for i in range(self.worldSize):
            inputTile = inputGame[i//sideLen][i%sideLen]
            inputTile = 1 if inputTile == "O" else 0
            inputGameArray.append(inputTile)

        layerOutputs = []
        layerOutputs.append(self.sigmoid(inputGameArray@self.weights[0] + self.biases[0]))
        layerOutputs.append(self.sigmoid(layerOutputs[0]@self.weights[1] + self.biases[1]))

        for i in range(self.worldSize):
            newGame[i//sideLen][i%sideLen] = "O" if layerOutputs[1][i] >= .5 else "."
        return newGame

    def updateaWeights(self):
        pass

#Test Main
n = neuralNetwork(3, 20)
newGame = [["O","O","."],[".",".","O"],["O",".","."]]
for i in range(3):
    newGame = n.applyWeights(newGame)
    n.updateaWeights()