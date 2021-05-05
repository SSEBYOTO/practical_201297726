# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:18:23 2021

@author: gaming
"""

import random
import operator
import matplotlib.pyplot
import agentframework
import csv

num_of_agents = 100
num_of_iterations = 10
neighbourhood = 20
seed = 1

random.seed(seed)

num_of_agents = 10
num_of_iterations = 100

f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#Lines here happen before any data is processed
environment =[]
agents =[]

for row in reader:
    rowlist = []
    #lines here happen before each row is processed
    for values in row:
        #do something with values
        rowlist.append(values)
        #lines here happen after row is processed
        environment.append(rowlist)
        
#for values in agents:
#    agents.append(agents)
#lines happen here after all the data is processed
f.close()

#create function
def distance_between(agents_row_a, agents_row_b):
    """
    
    Parameters
    .............
    agents_row_a : TYPE
          DESCRIPTION 
    agents_row_b: TYPE
          DESCRIPTION.
    
    Returns
    ........
    TYPE A number
         The distance between agents_row_a and agents_row_b
    """
    return (((agents_row_a.x - agents_row_b.x)**2) +
            ((agents_row_a.y - agents_row_b.y)**2))**0.5
     
def print_agents():
    for i in range(num_of_agents):
        print(agents[i])

# Make the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

print_agents()

            

# Move the agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#check agents
print("After eating and moving")
print_agents()
        
#plot data in a graph
matplotlib.pyplot.ylim(0.99)
matplotlib.pyplot.xlim(0.99)
matplotlib.pyplot.imshow(environment)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
        
        
        
        

       
    