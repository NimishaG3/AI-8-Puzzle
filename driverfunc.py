import heapq as heap #For queueing
import copy
import time

#Main function for taking inputs regarding mode of puzzle
def main():
	print('Welcome to my 8-puzzle solver!\n Select one of the following numbers for the puzzle: \n')
	print('1 - Default puzzle or 2 - Create your own custom puzzle!\n')

	puzzle_mode = input()

	if(puzzle_mode == '1'):
		default_mode()
	elif(puzzle_mode == '2'):
		custom_mode()
	else:
		print('Please enter a valid input!\n')
		main()


#Function for choosing a puzzle from the pre-defined ones
def default_mode():

	#For the default mode, goal state is 3x3 and can be pre-defined
	final_state = [[1,2,3], [4,5,6], [7,8,0]]
	
	easy_peasy = [[1,2,3], [4,5,6], [7,8,0]]
	just_easy = [[1,2,3], [4,5,6], [0,7,8]]
	not_so_easy = [[1,3,6], [5,0,2], [4,7,8]]
	are_we_sure = [[1,3,6], [5,0,7], [4,8,2]]
	really_going_for_it = [[7,1,2], [4,8,5], [6,3,0]]
	oh_boy = [[0,7,2], [4,6,1], [3,5,8]]
	
	print('Choose one of the following default options:\n')
	print('1 - Easy Peasy : ')
	for el in easy_peasy:
		print('[', *el, ']')

	print('\n2 - Just Easy, Not Peasy : ')
	for el in just_easy:
		print('[', *el, ']')

	print('\n3 - Not So Easy : ')
	for el in not_so_easy:
		print('[', *el, ']')

	print('\n4 - Are We Sure? : ')
	for el in are_we_sure:
		print('[', *el, ']')

	print('\n5 - Really Going For It : ')
	for el in really_going_for_it:
		print('[', *el, ']')

	print('\n6 - Oh Boy : ')
	for el in oh_boy:
		print('[', *el, ']')

	def_mode = input()


#Using if-elif-else statements to determine input value since Python does not have switch statements
#Storing the value of user chosen list in an empty list called 'start_state'

	if(def_mode == '1'):
		start_state = easy_peasy
	elif(def_mode == '2'):
		start_state = just_easy
	elif(def_mode == '3'):
		start_state = not_so_easy
	elif(def_mode == '4'):
		start_state = are_we_sure
	elif(def_mode == '5'):
		start_state = really_going_for_it
	elif(def_mode == '6'):
		start_state = oh_boy
	else:
		print('Please enter a valid input from the options above! If you would like to return to the main menu, enter 1. Press any other key to restart the default mode menu!')
		wrong_input = input()

		if(wrong_input == '1'):
			main()
		else:
			default_mode()

	choose_search_method(start_state, final_state)


#Function for choosing a custom-made puzzle 
def custom_mode():
	print('Enter the number of rows (same as columns) to use for your puzzle:\n')

	rows = int(input())

	custom_input = []

	#Creating and initializing the custom final state using these links :
	#https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
	#https://stackoverflow.com/a/20114599
	final_state = [[(j + 1) + (rows * i) for j in range(rows)] for i in range(rows)]
	final_state[rows-1][rows-1] = 0


	print('Custom goal state for' , rows, 'x', rows, 'puzzle is: \n')
	for el in final_state:
		print('[', *el, ']')


	if(rows>0):
		print('**** NOTE: SEPARATE NUMBERS BY SPACE ****')
		#REFERED : https://stackoverflow.com/questions/40336601/python-appending-array-to-an-array
		for el in range(1,rows+1):
			print('Enter row number: ' , str(el))
			el1 = input()
			#REFERED : https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
			el1 = [int(i) for i in el1.split()]
			custom_input.append(el1)

		choose_search_method(custom_input, final_state)

	else:
		print('Oops! Please input a valid number!')
		custom_mode()


#Function for choosing a search method
def choose_search_method(start_state, final_state):
	
	print('Choose the search method you would like to use :\n')
	
	print('1 - Uniform Cost Search\n')
	print('2 - A* with Manhattan Distance heuristic\n')
	print('3 - A* with Misplaced Tile Heuristic\n')

	search_type = input()

	if(search_type > str(0) and search_type < str(4)):
		#Referred https://stackoverflow.com/a/14452178
		#https://docs.python.org/3/library/time.html#time.process_time
		start = time.process_time()
		tree_and_heap_computation(start_state, final_state, search_type)
		print(time.process_time() - start) 
		print('milliseconds taken')

	else:
		print('Please enter a valid input!\n')
		print('Enter 1 to return to the main menu. Press 2 to return to the default mode menu. Press any other key to restart the search method menu!\n')

		wrong_input_2 = input()

		if(wrong_input_2 == '1'):
			main()
		elif(wrong_input_2 == '2'):
			default_mode()
		else:
			choose_search_method(start_state, final_state)

def tree_and_heap_computation(start_state, final_state, search_type):

	parent1 = Node(curr_state = start_state) #Making a root node from the starting state
	queue = [ ]
	heap.heappush(queue,parent1) #Add the first node to our heap (Acting as a priority queue)

	visited_states = []
	
	num_nodes_expanded = 0 #Since no node has been EXPANDED yet
	max_nodes_in_queue = 1 #Since we have already added root to the queue

	while(queue):

		if max_nodes_in_queue < len(queue):
			max_nodes_in_queue = len(queue)

		curr_node = heap.heappop(queue)

		print('The best state for expanding with g(n) = ' , str(int(curr_node.g)), 'and h(n) = ', str(int(curr_node.g)), 'is : \n')
		
		curr_node_state = curr_node.curr_state
		for el in curr_node_state:
			print('[', *el, ']')

		if(state_equality(curr_node_state, final_state)): #If this is our goal state
			print('Solution found! Here are the nodes and the order in which they were expanded for this solution: \n')
			curr_node.print_nodes_traced()
			print('Max no of elements in queue: ' , max_nodes_in_queue, 'and number of nodes expanded: ', num_nodes_expanded, '\n')
			return num_nodes_expanded, max_nodes_in_queue
		
		else:
			visited_states.append(curr_node) #Add the current state to the list of states we have already checked
			child_list = curr_node.tile_operators()
			
			#Remove null values from this list (if any) and if there are no other values in list, continue
			#Referred https://www.geeksforgeeks.org/python-remove-none-values-from-list/
			updated_child_list = [el for el in child_list if el]

			if(updated_child_list == [ ]):
				continue

			for newchildstate in updated_child_list:
				newchildnode = Node(curr_state = newchildstate, g=0, h=0)

				#If this new child node already exists in our queue or already has been visited, we can just continue and don't need to do further calculations for this node
				#LIMITING REPEATED STATES
				if(queue and newchildnode in queue):
					continue
				elif(visited_states and newchildnode in visited_states):
					continue 
				else:
					if(search_type == str(1)):
						newchildnode.h = 0 #Uniform Cost Search
					elif(search_type == str(2)):
						newchildnode.h = manhattan_distance(newchildnode.curr_state,final_state) #AStar with Manhattan Distance heuristic
					else:
						newchildnode.h = count_misplaced_tiles(newchildnode.curr_state, final_state) #AStar with Misplaced Tile heuristic

				curr_node.add_as_child_node(node = newchildnode)

				heap.heappush(queue,newchildnode)

			num_nodes_expanded += 1


	print('No solution found! :( \n')
	return False


def count_misplaced_tiles(start_state, final_state):
	heuristic = 0
	for i in range (0,len(start_state)):
		for j in range (0,len(start_state)):
			if(start_state[i][j] != final_state[i][j] and start_state[i][j] != 0):
				heuristic +=1

	return heuristic

def manhattan_distance(start_state, final_state):
	heuristic = 0

	#Referred https://www.devcubicle.com/find-the-length-of-2d-array-in-python/#:~:text=Use%20len(arr)%20to%20find,of%20elements%20is%20rows%20*%20columns
	#Using three loops : First to loop over all the elements of the 2D array, other two to get locations of each element
	for i in range(1,len(start_state)*len(start_state[0])):
		for j in range (0,len(start_state)):
			for k in range (0,len(start_state)):
				if(i == start_state[j][k]):
					start_row = j
					start_col = k
				if(i == final_state[j][k]):
					final_row = j
					final_col = k

		heuristic += (abs(final_row - start_row) + abs(final_col - start_col))

	return heuristic

def state_equality(state1, state2):
	#Referred : https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
    # Flatten the list of lists for easy comparison
    result_list1 = [el for subel in state1 for el in subel]
    result_list2 = [el for subel in state2 for el in subel]
    
    return result_list1 == result_list2

class Node:
	
	def __init__(self,h=0,g=0,curr_state=0,parent=None):
		#Here, h = Cost to goal, g = Cost from start, curr_state = current state of the puzzle
		self.h = h
		self.g = g
		self.curr_state = curr_state #Current state of the puzzle, changes after every operation
		self.parent = parent #Added for ease of tracing later on
		self.children = []

	def add_as_child_node(self, node, cost=1): #Here cost of 1 is the cost to expand this node
		node.g = self.g + cost # extend the child'd cost from start
		self.children.append(node)
		node.parent = self


	#Function to print and count no. of nodes traced till result using the parent node of each child selected
	def print_nodes_traced(self):

		x = self
		trace = 0
		
		while(x):
			print(x.curr_state)
			trace += 1
			x = x.parent

		print('Number of nodes traced : ' , trace, '\n')

	#Referred https://stackoverflow.com/questions/1061283/lt-instead-of-cmp 
	#Referred https://stackoverflow.com/a/7803240
	#Function to compare costs of two nodes, used to sort nodes in the heap by cost
	def __lt__(self,other):
		return self.g + self.h < other.g + other.h

	#Function to calculate the total f value as h+g
	def f_calculator(self):
		return (self.g + self.f)

	#Like lt function, this is used to compare equality of nodes in the heap
	def __eq__(self,other):
		return self.curr_state == other.curr_state

	#Function to define movements of the 0 tile
	def tile_operators(self):
		valid_states = []
		puzzle = self.curr_state
		
		#Variables to depict coordinates of 0 in the puzzle - initialised as 0,0
		m = 0
		n = 0

		#Find the coordinates of 0 in the 2D array

		for i in range (0,len(puzzle)):
			for j in range (0,len(puzzle)):
				if(puzzle[i][j] == 0):
					m = i
					n = j
					break


		#Moving left			
		if(n!=0):
			newstate = copy.deepcopy(puzzle)
			newstate[m][n] = newstate[m][n-1]
			newstate[m][n-1] = 0

        	#Check if this state is same as it's parent, parent is not null and add only if false
			if (self.parent and state_equality(newstate, self.parent.curr_state)):
				valid_states.append(None) 
			else:
				valid_states.append(newstate)

        #Moving up		
		if(m!=0):
			newstate = copy.deepcopy(puzzle)
			newstate[m][n] = newstate[m-1][n]
			newstate[m-1][n] = 0

			if (self.parent and state_equality(newstate, self.parent.curr_state)):
				valid_states.append(None)
			else:
				valid_states.append(newstate)

        #Moving Right
		if(n!=(len(puzzle)-1)):
			newstate = copy.deepcopy(puzzle)
			newstate[m][n] = newstate[m][n+1]
			newstate[m][n+1] = 0
			if (self.parent and state_equality(newstate, self.parent.curr_state)):
				valid_states.append(None) 
			else:
				valid_states.append(newstate)

        #Moving Down
		if(m!=(len(puzzle)-1)):
			newstate = copy.deepcopy(puzzle)
			newstate[m][n] = newstate[m+1][n]
			newstate[m+1][n] = 0

			if (self.parent and state_equality(newstate, self.parent.curr_state)):
				valid_states.append(None) 
			else:
				valid_states.append(newstate)

		return valid_states


main()
