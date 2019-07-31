from random import uniform, random, shuffle
from math import sin, cos, e
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
import numpy as np
data = load_iris()
data = [(x, y) for x, y in zip(data['data'], data['target'])]
shuffle(data)
d, t = [x[0] for x in data], [x[1] for x in data]
SPEED = 1
class DSO:
    def __init__(self, popSize, soluSize, space, T1 = 3,
            T2 = 5, speed=SPEED, A=5, M=3, e=4):
        #Initialization phase 
        self.popSize = popSize
        self.soluSize = soluSize
        self.space = space
        self.T1 = T1
        self.T2 = T2
        self.speed = speed
        SPEED = self.speed
        self.A  = A
        self.M = M
        self.e = e
        self.TS = [[T2 for i in range(popSize)] for x in range(popSize)]
        self.population = [Dolphin([uniform(*space) for i in 
            range(soluSize)]) for x in range(popSize)]
        
        
    def optimaze(self, generations=100):
        incrise = []
        while generations > 0:
            print(generations)
            generations -=1
            incrise.append(testData(((min(self.population, key=lambda x: fitness(x.solution)))).solution))
            open('result.txt', 'w').write(str(incrise))
            #Search Phase
            for sol in (self.population):
                sounds = [getVector(self.soluSize) for x in range(self.M)]
                newSolution = []
                for i in sounds:
                    for j in range(self.T1):
                        vector = [x*(j+1) for x in i]
                        newSolution.append([x+y for x, y in zip(sol.solution, vector)])
                bestSolution = min(newSolution, key = lambda x: fitness(x))
                if(fitness(bestSolution) < fitness(sol.solutionL)): sol.solutionL = [el for el in bestSolution]
                if(fitness(sol.solutionL) < fitness(sol.solutionK)): sol.solutionK = [el for el in sol.solutionL]
            #Call Phase
            for i in range(self.popSize):
                for j in range(self.popSize):
                    if fitness(self.population[i].solutionK) > fitness(self.population[j].solutionK) and\
                        self.TS[i][j] > (DD(self.population[i].solution, self.population[j].solution)/(self.speed*self.A)):
                        self.TS[i][j] = (DD(self.population[i].solution, self.population[j].solution)/(self.speed*self.A))
                        
            #Reception Phase
            for i in range(self.popSize):
                for j in range(self.popSize):
                    self.TS[i][j] -= 1
                    if self.TS[i][j] <= 0:
                        self.TS[i][j] = self.T2
                        if fitness(self.population[i].solutionK) > fitness(self.population[j].solutionK):
                            self.population[i].solutionK = [el for el in self.population[j].solutionK]
            #Predation Phase
            for sol in self.population:
                R1 = self.speed*self.T1
                dsk = DD(sol.solution, sol.solutionK)
                dkl = DD(sol.solutionK, sol.solutionL)
                if dsk <= R1 and dsk > 0:
                    R2 = (1-2/self.e)*dsk
                    ter = [(x-y)*R2 for x, y in zip(sol.solution, sol.solutionK)]
                    ter = [x/dsk for x in ter]
                    sol.solution = [x+y for x, y in zip(ter, sol.solutionK)]
                
                if dsk > R1 and dsk >= dkl:
                    R2 = (1 - (((dsk/fitness(sol.solutionK) + ((dsk-dkl)/fitness(sol.solutionL)))/((e*dsk)/fitness(sol.solutionK)))))*dsk
                    ter = getVector(self.soluSize)
                    ter = [x*R2 for x in ter]
                    sol.solution = [x+y for x, y in zip(sol.solutionK, ter)]
                
                if dsk > R1 and dsk < dkl:
                    R2 = (1 - (((dsk/fitness(sol.solutionK) - ((dsk-dkl)/fitness(sol.solutionL)))/((e*dsk)/fitness(sol.solutionK)))))*dsk
                    ter = getVector(self.soluSize)
                    ter = [x*R2 for x in ter]
                    sol.solution = [x+y for x, y in zip(sol.solutionK, ter)]
                if fitness(sol.solution) < fitness(sol.solutionK):
                    sol.solutionK = [el for el in sol.solution]
        
        return (min(self.population, key=lambda x: fitness(x.solution)).solution)
                
def DD(i, j):
    return (sum([(x-y)**2 for x, y in zip(i, j)]))**(1/2)

class Dolphin:
    def __init__(self, solution):
        self.solution = solution
        self.solutionL = solution
        self.solutionK = solution
    def __str__(self):
        return str(self.solution) + " : " + str(self.solutionL) + " : " + str(self.solutionK)
def getVector(size):
    v = [random() for i in range(size)]
    norm =(sum([x**2 for x in v]))**(1/2)
    v = [x/norm for x in v]
    v = [x*SPEED for x in v]
    return v

def fitness(solution):
    model = MLPClassifier(hidden_layer_sizes =(8, 5))
    model.fit(d, t)
    coef = []
    coef.append(np.asarray([solution[i:i+8] for i in range(4)]))
    coef.append(np.asarray([solution[32+i:32+i+5] for i in range(8)]))
    coef.append(np.asarray([solution[72+i:72+i+3] for i in range(5)]))
    model.coefs_ = coef
    score = model.score(d[:100], t[:100])
    return 1 - score
def testData(solution):
    model = MLPClassifier(hidden_layer_sizes =(8, 5))
    model.fit(d, t)
    coef = []
    coef.append(np.asarray([solution[i:i+8] for i in range(4)]))
    coef.append(np.asarray([solution[32+i:32+i+5] for i in range(8)]))
    coef.append(np.asarray([solution[72+i:72+i+3] for i in range(5)]))
    model.coefs_ = coef
    score = model.score(d[100:], t[100:])
    return 1 - score