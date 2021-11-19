import random
DNA_SIZE =10

def randomInt():
    return int(random.random()*DNA_SIZE)

def random_population():
    pop = []
    for c in range(DNA_SIZE):
        dna = randomInt()
        pop.append(dna)
    return pop

def crossover(dna1, dna2):
    pos = int(random.random()*DNA_SIZE)
    return (dna1[:pos]+dna2[pos:], dna2[:pos]+dna1[pos:])

dna1=random_population()
print(dna1)
dna2=random_population()
print(dna2)
child=crossover(dna1, dna2)
print(child)
