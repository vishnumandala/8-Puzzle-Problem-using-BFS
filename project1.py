import numpy as np
from queue import Queue

'''Define a function to find the coordinates of the blank tile (value 0) in the given state'''
def find_blank_tile(state):
    i, j = np.where(state == 0)
    return i[0], j[0]

'''Define four functions to move the blank tile left, right, up, or down in the given state, respectively
Each function checks if the move is valid 
(i.e., whether the blank tile is at the edge of the board in the given direction), 
and returns a boolean flag indicating success and the resulting state after the move.'''

def ActionMoveLeft(state):
    i, j = find_blank_tile(state)
    if j == 0:
        return False, None
    else:
        new_state = np.copy(state)
        new_state[i][j] = new_state[i][j-1]
        new_state[i][j-1] = 0
        return True, new_state

def ActionMoveRight(state):
    i, j = find_blank_tile(state)
    if j == 2:
        return False, None
    else:
        new_state = np.copy(state)
        new_state[i][j] = new_state[i][j+1]
        new_state[i][j+1] = 0
        return True, new_state

def ActionMoveUp(state):
    i, j = find_blank_tile(state)
    if i == 0:
        return False, None
    else:
        new_state = np.copy(state)
        new_state[i][j] = new_state[i-1][j]
        new_state[i-1][j] = 0
        return True, new_state

def ActionMoveDown(state):
    i, j = find_blank_tile(state)
    if i == 2:
        return False, None
    else:
        new_state = np.copy(state)
        new_state[i][j] = new_state[i+1][j]
        new_state[i+1][j] = 0
        return True, new_state

'''Define a function to generate all possible states that can be obtained by moving the blank tile in the given state in any of the four directions.
The function loops through the four move functions, applies each move to the given state, and adds the resulting state to a list if the move was successful.'''

def generate_next_states(state):
    next_states = []
    for move in [ActionMoveLeft, ActionMoveRight, ActionMoveUp, ActionMoveDown]:
        success, new_state = move(state)
        if success:
            next_states.append(new_state)
    return next_states

'''Define a function called "bfs" that takes two arguments: the starting state of the puzzle board and the goal state'''
def bfs(start_state, goal_state):
    
    # Initialize the queue and visited set
    queue = Queue()
    visited = set()

    # Add the start state to the queue with parent index -1
    start_index = 0
    parent_node_index_i = -1
    queue.put((start_index, parent_node_index_i, start_state))
    visited.add(tuple(map(tuple, start_state)))

    # Initialize the nodes list and nodes_info list
    nodes = [start_state]
    nodes_info = [(start_index, parent_node_index_i, start_state)]

    # Start BFS algorithm
    while not queue.empty():
        # Pop the first node from the queue
        node_index_i, parent_node_index_i, current_node = queue.get()

        # Generate next possible states
        next_states = generate_next_states(current_node)

        # Loop through each next state
        for next_node in next_states:
            # Check if the next state is the goal state
            if np.array_equal(current_node, goal_state):
                # Generate the path and write to nodePath.txt
                path = generate_path(nodes_info, node_index_i)
                with open("nodePath.txt", "w") as f:
                    for node in path:
                        np.savetxt(f, np.array(path).reshape(-1,9), fmt="%d", delimiter='\t')

                # Write explored states to Nodes.txt
                with open("Nodes.txt", "w") as f:
                    for node in nodes:
                        np.savetxt(f, node.reshape(-1,9), fmt="%d", delimiter='\t')
                
                # Write nodes_info to NodesInfo.txt
                with open("NodesInfo.txt", "w") as f:
                    for info in nodes_info:
                        f.write(f"{info[0]} {info[1]} ")
                        np.savetxt(f, info[2].reshape(-1,9), fmt="%d", delimiter=",")

                return True # Return True to indicate that a solution has been found.

            # Check if the next state has not been visited
            if tuple(map(tuple, next_node)) not in visited:
                # Add the next state to the queue and visited set
                next_index = len(nodes)
                queue.put((next_index, node_index_i, next_node))
                visited.add(tuple(map(tuple, next_node)))

                # Add the next state to nodes and nodes_info lists
                nodes.append(next_node)
                nodes_info.append((next_index, node_index_i, next_node))

    return False    # Return False to indicate that no solution has been found.

'''Define a function called "generate_path" that takes two arguments: the nodes information list and the index of the goal state'''
def generate_path(nodes_info, goal_index):
    # Create an empty list for the path and set the current index to the index of the goal state.
    path = []
    current_index = goal_index

    # Traverse the nodes_info list backwards to generate the path
    while current_index != -1:
        node = nodes_info[current_index][2]
        path.append(node)
        current_index = nodes_info[current_index][1]
    # Reverse the path to get it in the correct order
    path.reverse()
    return path

'''Take input for the start state in a single line'''
start_state = np.zeros((3,3), dtype=int)
print("Enter the start state of the 8-puzzle board in a single line (space-separated, enter 0 for blank tile):")
input_line = input()
input_list = list(map(int, input_line.strip().split()))

for i in range(3):
    for j in range(3):
        start_state[i][j] = input_list[3*j+i]
        
print("Start State:")
print(start_state,'\n')

'''Take input for the goal state in a single line'''
goal_state = np.zeros((3,3), dtype=int)
print("Enter the goal state of the 8-puzzle board in a single line (space-separated, enter 0 for blank tile):")
input_line = input()
input_list = list(map(int, input_line.strip().split()))

for i in range(3):
    for j in range(3):
        goal_state[i][j] = input_list[3*j+i]

print('Goal State:')
print(goal_state,'\n')

# Transpose so that format is readable by plot_path.py
start_state = np.transpose(start_state)
goal_state = np.transpose(goal_state) 

'''Run the BFS algorithm and check if it finds a solution'''
if bfs(start_state, goal_state):
    print("Solution found!\n")
else:
    print("No Solution found\n")