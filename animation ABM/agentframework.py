# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:16:18 2021

@author: gaming
"""

import random

class Agent():
    
    def __init__(self, environment, agents):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
        
    def __str__(self):
        return "x=" + str(self.x) +", y=" + str(self.y) +", store=" + str(self.store)
        
    def move(self):
        """
        This modifies the x and y variables for the agent increasing or 
        decreasing them pseudorandomly.

        Returns
        -------
        None.

        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] = 10
            self.store +=10
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
            #print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
        