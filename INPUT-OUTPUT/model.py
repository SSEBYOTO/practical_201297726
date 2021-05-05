# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 23:01:37 2021

@author: gaming
"""
#import csv
import csv
import matplotlib.pyplot
import agentframework
import random

#read in the environment
environment = []
f = open("in.txt")
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist =[]
    for value in row: #its possible to also test the shape of the data here
        print(value)
        rowlist.append(value)
        environment.append(rowlist)
f.close()
    
nrows = len(environment)
ncols0 = len(environment[0])
ncolslast =len(environment[nrows -1])
print("ncol0", ncols0)
print("ncolslast", ncolslast)
#test the environment was initialised correctly
#print(environment[0])
#print(environment[nrows -1])

#create agents
agents = []
num_of_agents = 3
for i in range (num_of_agents):
    x = random.randint(0,99)
    y = random.randint(0,99)
    agents.append(agentframework.Agent(i, x, y, environment))
#print agents
for agent in agents:
    print(agent)
    
#Main loop
num_of_iterations = 2
for j in range(num_of_iterations):
    for i in range (num_of_agents):
        #agents[i].move()
        agents[i].eat()

#Plot
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()






