# Name = Muhammad Ali Ahson
# Roll = 21i-3535
# Assignment 1

import sys
import numpy as np
import random
from Reflex_agent import Reflex_Agent
from Model_based import Model_Based


def welcome():
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                                                                ║")
    print("║                    Welcome to the Jigsaw Game!                 ║")
    print("║                                                                ║")
    print("║            Get ready to challenge your puzzle-solving          ║")
    print("║            skills and enjoy hours of fun and excitement!       ║")
    print("║                                                                ║")
    print("║   Actions available:                                           ║")
    print("║   - Left          : Move the agent left                        ║")
    print("║   - Right         : Move the agent right                       ║")
    print("║   - Up            : Move the agent up                          ║")
    print("║   - Down          : Move the agent down                        ║")
    print("║   - NoOp          : Take no action                             ║")
    print("║   - Rotate_left   : Rotate the cell content 90° counterclockwise║")
    print("║   - Rotate_right  : Rotate the cell content 90° clockwise      ║")
    print("║                                                                ║")
    print("║   Remember:                                                    ║")
    print("║   - The environment is deterministic and partially observable. ║")
    print("║   - Your goal is to correctly place as many items as possible  ║")
    print("║     within the allowed number of moves.                        ║")
    print("║                                                                ║")
    print("║            Let the game begin and may the best agent win!      ║")
    print("║                                                                ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print("\nPlease select the type of agent you would like to use:")
    print("1) Reflex Agent")
    print("2) Reflex Agent with State (Model-Based Agent)")

def select_agent_type():
    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            print("You have selected Reflex Agent.")
            return 'reflex'
        elif choice == '2':
            print("You have selected Reflex Agent with State (Model-Based Agent).")
            return 'model_based'
        else:
            print("Invalid choice. Please enter 1 or 2.")


def random_number(start, end,grid=False):
    if grid:
        a = random.randint(start,end-1)
        b = random.randint(start,end-1)
        return [a,b]
  


def create_grid(size):
    number = list(range(1,size*size+1))
    random.shuffle(number)
    grid = np.array(number).reshape(size,size)
    return grid


def main():
    grid_size = int(sys.argv[1])
    no_Movement = int(sys.argv[2])
    game_grid = create_grid(grid_size)
    input_grid = np.zeros((grid_size,grid_size))
    starting = random_number(0,grid_size-1,True)
    print("The Size of the Grid is ",grid_size)
    print("The Movements defined are ",no_Movement)
    welcome()
    choice = select_agent_type()
    if choice == 'reflex':
        agent = Reflex_Agent(input_grid,list(starting),game_grid,no_Movement)
        agent.play_game()
        agent.display_working_grid()
        agent.display_Goad_grid()
        agent.performance_measure()
 
    else:
        agent = Model_Based(input_grid,list(starting),game_grid,no_Movement)
        agent.play_game()
        agent.display_working_grid()
        agent.display_Goad_grid()
        agent.performance_measure()
    

if __name__ == "__main__":
    main()


