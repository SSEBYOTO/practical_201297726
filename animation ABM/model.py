# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:18:23 2021

@author: gaming
"""

import random
import operator
import matplotlib.pyplot
import agentframework
import matplotlib.animation 
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

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

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
carry_on = True
print_agents()

            

# Move the agents
def update(frame_number):
    fig.clear()   
    global carry_on
        
   
    for i in range(num_of_agents):        
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

    carry_on = True

    #check agents
    print("After eating and moving")
    print_agents()
            
    #plot data in a graph
    matplotlib.pyplot.ylim(0,299)
    matplotlib.pyplot.xlim(0,299)
    matplotlib.pyplot.imshow(environment)
    
    for i in range (num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    matplotlib.pyplot.show()

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
        
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)



matplotlib.pyplot.show()
        
        
        
        
        

       
    