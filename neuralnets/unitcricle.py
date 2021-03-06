import numpy as np
import itertools
import copy
import math
import random

#classes defined: Percept and Input(extends Percept)
#parameters: the weights (w_ij) and thresholds (t_j)

class Percept:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold
        self.percepts = None
    def set_inputs(self, percepts):
        self.percepts = percepts
    def actuator(self, value):
        val = 1/(1+math.e**(-5 * value))
        if val > self.threshold:
            return 1
        else:
            return 0
        # return 1 if val > self.threshold else 0
        
    def evaluate(self):
        total = 0
        for index in range(len(self.percepts)):
            total += self.weights[index] * self.percepts[index].evaluate()
        return self.actuator(total)

class Input(Percept):
    def __init__(self):
        self.value = None
    def set_value(self, val):
        self.value = val
    def evaluate(self):
        return self.value

x1 = Input()
x2 = Input()

nand_gate = Percept([-1,-1],-1.5) # nand
or_gate = Percept([1, 1],0.5) # or
and_gate = Percept([1, 1],1.5) # and 
nor_gate = Percept([-1, -1],-0.5) # nor

xor_gate = copy.copy(and_gate)
xor_gate.set_inputs([nand_gate, or_gate])

xnor_gate = copy.copy(nand_gate)
xnor_gate.set_inputs([nand_gate, or_gate])

square_gate = copy.copy(and_gate)
square_gate.set_inputs([xor_gate, xnor_gate])

x1.set_value(0)
x2.set_value(0)
nand_gate.set_inputs([x1, x2])
or_gate.set_inputs([x1, x2])

iterations = 10
count = 0

for i in range(0, iterations):
    compare = 0
    x1.set_value(random.uniform(-1.5, 1.5))
    x2.set_value(random.uniform(-1.5, 1.5))
    if(x1.value**2 + x2.value**2) < 1:
        compare = 0
    else:
        compare = 1
    if(square_gate.evaluate() == compare):
        count += 1
        
    print(x1.value, x2.value)
    print("real: ", compare)
    print(square_gate.evaluate())
    print("")

"""
values = [[-0.5, -0.5, -1.5],
[ 0.5,  0.5, -0.5],
[ 1.5, -2.5, -0.5],
[ 1.5,  0.5, -0.5],
[-1.5,  1.5, -0.5],
[-0.5,  1.5, -0.5],
[ 1.5,  1.5, -0.5],
[-0.5, -0.5,  0.5],
[ 0.5, -1.5,  0.5],
[ 1.5, -0.5,  0.5],
[-2.5,  0.5,  1.5],
[-0.5,  1.5,  0.5],
[-2.5, -1.5,  3.5],
[ 0.5,  0.5,  0.5]]

nodes = []
for value in values:
    output = Percept([value[0], value[1]], -1 * value[2])
    nodes.append(output)
    
counter = 0

for a in nodes:
    first = copy.copy(a)
    for b in nodes:
        second = copy.copy(b)
        for c in nodes:
            third = copy.copy(c)
            first.set_inputs([x1,x2])
            second.set_inputs([x1,x2])
            third.set_inputs([first, second])
            xor = third
            # print(first.name, second.name, third.name)
            result = []
            for a in range(2):
                for b in range(2):
                    x1.set_value(a)
                    x2.set_value(b)
                    endEval = xor.evaluate()
                    result.append(endEval)
                    # print(a, b, endEval)
            # print(result)
            if result == target:
                counter += 1
            # print('\n')

print(counter)
"""




