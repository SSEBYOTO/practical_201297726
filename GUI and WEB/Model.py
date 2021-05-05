# -*- coding: utf-8 -*-
"""
Created on Wed May  5 01:27:26 2021

@author: gaming
"""

import tkinter 
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework
import matplotlib.animation 
import csv
import requests
import bs4

#run the animation
def run():
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()
    
#request data from an online source
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)
 

    
num_of_agents = 100
num_of_iterations = 10
neighbourhood = 20
seed = 1

random.seed(seed)

num_of_agents = 10
num_of_iterations = 100

f = open('in.txt', newline='')  #open the text file
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#Lines here happen before any data is processed
environment =[]
agents =[]

#define figure size
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
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
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
        

#define and create menu 
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()





