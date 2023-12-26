################################################################################
#  simulation
################################################################################

#  FUNCTION DESCRIPTION:  
#                         
#                        

#  ARGUMENTS
# x: 
# 


class Simulation:
    def __init__(self, num_individuals, num_iterations):
        self.individuals = [Individual(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_individuals)]
        self.num_iterations = num_iterations

    def run(self):
        for iteration in range(self.num_iterations):
            print(f"Iteration {iteration + 1}:")
            for individual in self.individuals:
                individual.move()
                print(f"Individual at ({individual.x}, {individual.y})")
            print("\n")


#  AUTHORSHIP:
# Name: Eduardo Ribeiro da Cunha
# Email: edurcunha@gmail.com