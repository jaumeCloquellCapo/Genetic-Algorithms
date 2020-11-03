# Introduction to genetic algorithms

## What is it?

It's a group of algorithms aimed at optimization problems inspired by (a very simple interpretation of) the evolution theory. Most of those algorithms a heuristic or stochastic trial-and-error techniques.

The main idea is to create a population of individuals and loop through a succession of survival selection, mating, mutation and generation of a new population, derived from the former one, so we can iteratively aproximate the an ideal or sufficiently acceptable solution to the problem.

## Concepts

**Gene**: The value of a single variable of the problem-space solution.

**Genotype**: The collection of genes of an individual. Sometimes called **chromosome** or **DNA** in GA literature.

**Alphabet**: The solution's variables types. Think of it as the possible values of a gene.

**Fitness**: How 'adequate' a solution is to the given problem. How close or far it is from the optimal or an acceptable solution.

**Fitness function**: An objective function that calculates the fitness of an individual to the problem's solution.

**Population**: Collection of individuals.

**Fenotype**: The visual or functional representation of a genotype.

**Generation**: A group of individuals (population) that is "alive" (active) during a given genetic algorithm iteration.

## The loop

    population.generatePopulation()
    generation = 1
    while population.evaluate():
        population.calculateFitness() 
        population.nextGeneration()
        print("Generation:", generation)
        print("Average fitness:", "%.2f" % population.avg_fitness + "%")
        print("Genomas:", ''.join(map(lambda x: x, population.pop[population.biggest].genes)))
        generation += 1
