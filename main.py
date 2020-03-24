import Genetics
import string
import numpy as np
from matplotlib import pyplot as plt

def main():
    target = "hellowworld"    
    maxPop = 500
    mutation_rate = 0.01
    evolutions = 100
    evolution = 0
    population = Genetics.Population(target, maxPop, mutation_rate)

    population.generatePopulation()
    generation = 1
    while population.evaluate():
        population.calculateFitness() 
        population.nextGeneration()
        print("Generation:", generation)
        print("Average fitness:", "%.2f" % population.avg_fitness + "%")
        print("Genomas:", ''.join(map(lambda x: x, population.pop[population.biggest].genes)))
        generation += 1

if __name__ == '__main__':
    main()