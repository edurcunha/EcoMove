################################################################################
#  indGenesis
################################################################################

#  FUNCTION DESCRIPTION:  
#                         
#                        

#  ARGUMENTS
# x: 
# 


import random

class Individual:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.x += dx
        self.y += dy


#  AUTHORSHIP:
# Name: Eduardo Ribeiro da Cunha
# Email: edurcunha@gmail.com

