# Name = Muhammad Ali Ahson
# Roll = 21i-3535
# Assignment 1



import random
import numpy as np

class Reflex_Agent:
    def __init__(self, working_grid,starting,Goal_grid,no_of_steps):
        self.working_grid = working_grid
        self.state = starting
        self.Goal_grid = Goal_grid
        self.no_of_steps = no_of_steps
        self.correct_steps = 0
        self.step_used = 0

    def random_number(self,start, end,grid=False):
        return random.randint(start,end)
        


    def check_termination(self):
        if self.no_of_steps == 0:
            return False
        elif np.array_equal(self.working_grid, self.Goal_grid):
            return False
        else:
            return True
        

    def __val_(self):
        return self.random_number(1,self.Goal_grid.shape[0]* self.Goal_grid.shape[0])


    def performance_measure(self):
        performance = (self.correct_steps/self.step_used)*100
        print("The Performance of the Reflex Agent is " , performance, "%")
    
    def __check_boundaries(self):
        if self.state[0] < 0:
            self.state[0] += 1
        elif self.state[1] < 0:
            self.state[1] +=1
        elif self.state[0] > self.Goal_grid.shape[0]-1:
            self.state[0] -= 1
        elif self.state[1] > self.Goal_grid.shape[1]-1:
            self.state[1] -= 1
        else:
            return True
        return False

    def movement(self):
        while True:
            val = self.random_number(1,8)
            if val == 1:  # left
                self.state = [self.state[0]-1, self.state[1]]
            elif val == 2:  # right
                self.state = [self.state[0]+1, self.state[1]]
            elif val == 3:  # Up
                self.state = [self.state[0], self.state[1]-1]
            elif val == 4:  # Down
                self.state = [self.state[0], self.state[1]+1]
            elif val == 5:
                self.state = [self.state[0]-1, self.state[1]-1]
            elif val == 6:
                self.state = [self.state[0]+1, self.state[1]-1]
            elif val == 7:
                self.state = [self.state[0]-1, self.state[1]+1]
            elif val == 8:
                self.state = [self.state[0]+1, self.state[1]+1]
            
            flag = self.__check_boundaries()
            if flag:
                break

    def display_working_grid(self):
        print(self.working_grid)
        print()

    def display_Goad_grid(self):
        print(self.Goal_grid)

    def play_game(self):
        val = self.__val_()
        flag = True
        while(flag):
            if self.Goal_grid[self.state[0],self.state[1]] == val:
                self.working_grid[self.state[0],self.state[1]] = val
                self.correct_steps += 1
                self.step_used += 1
                self.no_of_steps -=1
                val = self.__val_()

            flag = self.check_termination()
            if flag == False:
                break
            else:
                self.movement()
                self.step_used += 1
                self.no_of_steps -=1


