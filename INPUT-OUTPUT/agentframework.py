# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 23:49:16 2021

@author: gaming
"""
import random


class Agent():
    def __init__(self, i, x, y,environment):
           self.i = i
           self.environment = environment
           self.store = 0
           self.x = x
           self.y = y
           
           #print (self.environment ,self.store)
           
    def __str__(self):
        return "Agent" + str(self.i) + "x=" + str(self.x) + "y=" + str(self.y) + "store=" + str(self.store)
    
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] = 10
            self.store += 10
           
    def randomize (self):   
          self.environment = random.randint(0,99)
          self.store = random.randint(0,99)

    
 
           
   
            
    
