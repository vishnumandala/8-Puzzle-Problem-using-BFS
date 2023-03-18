# PROJECT 1

## ENPM661 - Planning For Autonomous Robots

## Problem Statement
Find all the possible states of the 8-Puzzle starting from the given initial state until the goal node is reached. Note that, the states should be unique (no repetitions)
1. From the initial state of the puzzle, use different moves in all the directions to generate new states, check the validity of the newly generated node
2. You should use Python for programing
3. Use the Breath First Search(BFS) to find the path to reach the goal
4. Implement back tracking to find the plan to solve the problem

## Objectives
1. Use Breadth First Search to transverse the dataset layer by layer, exploring the nodes directly connected to the initial node (Blank Tile)
2. Create a move set that moves the the blank tile in 4 directions only (Up, Down, Left, Right)
3. Create a list of all possible nodes, but forbid repetition so that infinite looping is avoided
4. Arrive at the given goal state of [1, 4, 7], [2, 5, 8], [3, 0, 6]
5. Find the path between initial and final node using backtracking
6. Generate Text files with the given requirements
		Nodes.txt 		- 	With all explored states
		NodesInfo.txt 	- 	Information about Parent Index, Node Index and Node
		nodePath.txt 	- 	Path to goal from initial state

## Dependencies
1. python 3.11 (any version above 3 should work)
2. Python running IDE (I used VS Code)

## Libraries
1. NumPy
2. Queue

## Contents
1. Code.pdf
2. project1.py
3. plot_path.py
4. Nodes.txt
5. nodePath.txt
6. NodesInfo.txt
7. README.md

## Instructions
1. Download the zip file and extract it
2. Install python and the required dependencies: pip install numpy
3. Run the code: project1.py
4. Type in the input as the state of the 8-Puzzle board in a column wise manner with spaces seperating each value

## Example Output

### Test Case 1:
Enter the start state of the 8-puzzle board in a single line (space-separated, enter 0 for blank tile):
1 6 7 2 0 5 4 3 8 
Start State:
[[1 2 4]
 [6 0 3]
 [7 5 8]]

Enter the goal state of the 8-puzzle board in a single line (space-separated, enter 0 for blank tile):
1 4 7 2 5 8 3 0 6
Goal State:
[[1 2 3]
 [4 5 0]
 [7 8 6]]

Solution found!

### Test Case 2:
Enter the start state of the 8-puzzle board in a single line (space-separated, enter 0 for blank tile):
4 7 8 2 1 5 3 6 0
Start State:
[[4 2 3]
 [7 1 6]
 [8 5 0]]

Enter the goal state of the 8-puzzle board in a single line (space-separated, enter 0 for blank tile):
1 4 7 2 5 8 3 6 0
Goal State:
[[1 2 3]
 [4 5 6]
 [7 8 0]]

Solution found!
