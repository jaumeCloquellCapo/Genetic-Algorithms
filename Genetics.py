import random
import numpy as np
import string

class DNA(object):
    genes = []
    fitness = 0
    def __init__(self, size):
        self.genes = [random.choice(string.ascii_letters) for i in range(size)]

    def mutate(self, parentA, parentB, mutation_rate):
        newGenes = [random.choice(string.ascii_lowercase) for i in range(len(parentB.genes))]
        midPoint = random.randint(0, len(parentA.genes))
        for ix in range(len(self.genes)):
            if random.random() < mutation_rate:
                newGenes[ix] = random.choice(string.ascii_lowercase)
            else:
                newGenes[ix] = parentA.genes[ix][:midPoint] + parentB.genes[ix][midPoint:]
        self.genes = newGenes

class Population(object):
    def __init__(self, target, maxPop, mutation_rate):
        self.target = [i for i in target]       
        self.maxPop = maxPop
        self.biggest = 0
        self.avg_fitness = 0
        self.mutation_rate = mutation_rate
        self.pop= []

    def generatePopulation(self):
        self.pop = [DNA(len(self.target)) for i in range(self.maxPop)]


    def __fitness(self, genes, target):
        fitness = 0
        for i in range(len(genes)):
            if genes[i] == target[i]:
                fitness += 1

        return fitness

    def evaluate(self):
        return not all([(x == y) for x, y in zip(self.pop[self.biggest].genes, self.target)])
        # return not (self.pop[self.biggest].genes == self.target).all()

    def calculateFitness(self):
        self.biggest = 0
        self.second = 0
        self.avg_fitness = 0
        
        for ix in range(len(self.pop)):
            #Fitness score is the sum of the correct letters
            self.pop[ix].fitness = self.__fitness(self.pop[ix].genes, self.target)
            self.avg_fitness+= float(self.pop[ix].fitness) / len(self.target)            
            #Save the 2 highest fitness for reproduction
            if self.pop[ix].fitness > self.pop[self.biggest].fitness:
                self.biggest = ix
            elif self.pop[ix].fitness > self.pop[self.second].fitness:
                self.second = ix
        #Calculate average fitness
        self.avg_fitness = (self.avg_fitness / len(self.pop)) * 100.0

    def nextGeneration(self):
        """Re-populate in an elitist way with the 2 best genes"""        
        #Get parents genes
        parentA =  self.pop[self.biggest]
        parentB =  self.pop[self.second]

        for ix in range(len(self.pop)):
            child = DNA(len(parentA.genes))
            #Crossover
            child.mutate(parentA, parentB, self.mutation_rate)
            self.pop[ix] = child