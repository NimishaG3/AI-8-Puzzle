import heapq as heap #For queueing
import copy

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

	if(search_type == '1'):
		uniform_cost_search(start_state, final_state)
	elif(search_type == '2'):
		astar_manhattan(start_state, final_state)
	elif(search_type == '3'):
		astar_misplaced_tile(start_state, final_state)
	else:
		print('Please enter a valid input!\n')
		print('Enter 1 to return to the main menu. Press 2 to return to the default mode menu. Press any other key to restart the search method menu!\n')

		wrong_input_2 = input()

		if(wrong_input_2 == '1'):
			main()
		elif(wrong_input_2 == '2'):
			default_mode()
		else:
			choose_search_method(start_state)

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


class Node:
	
	def __init__(self,h=0,g=0,curr_state=0,parent=None):
		"""
		Here, h = Cost to goal, g = Cost from start, curr_state = current state of the puzzle
		"""
		self.h = h
		self.g = g
		self.curr_state = curr_state #Current state of the puzzle, changes after every operation
		self.parent = parent #Added for ease of tracing later on
		self.children = []
		self.f = h+g


	#Function to print and count no. of nodes traced till result using the parent node of each child selected
	def print_nodes_traced(self):

		x = self.curr_state
		trace = 0
		
		while(x != None):
			print(x.curr_state)
			trace += 1
			x = x.parent

		print('Number of nodes traced : ' , trace, '\n')

	#Referred https://stackoverflow.com/questions/1061283/lt-instead-of-cmp 
	#Function to compare costs of two nodes and return lowest cost
	def __lt__(self,other):
		return self.f < other.f


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

        	#Check if this state is same as it's parent and add only if false
        	#Referenced https://stackoverflow.com/a/6105826 to convert state to set for ease of comparison

        	newstatelist = set(map(tuple, newstate))
        	parentlist = set(map(tuple, self.parent.curr_state))

        	if(newstatelist != parentlist):
        		valid_states.append(newstate)

        #Moving up		
        if(m!=0):
        	newstate = copy.deepcopy(puzzle)
			newstate[m][n] = newstate[m-1][n]
        	newstate[m-1][n] = 0

        	#Check if this state is same as it's parent and add only if false
        	#Referenced https://stackoverflow.com/a/6105826 to convert state to set for ease of comparison

        	newstatelist = set(map(tuple, newstate))
        	parentlist = set(map(tuple, self.parent.curr_state))

        	if(newstatelist != parentlist):
        		valid_states.append(newstate)

        #Moving Right
        if(n!=(len(puzzle)-1)):
        	newstate = copy.deepcopy(puzzle)
			newstate[m][n] = newstate[m][n+1]
        	newstate[m][n+1] = 0

        	#Check if this state is same as it's parent and add only if false
        	#Referenced https://stackoverflow.com/a/6105826 to convert state to set for ease of comparison

        	newstatelist = set(map(tuple, newstate))
        	parentlist = set(map(tuple, self.parent.curr_state))

        	if(newstatelist != parentlist):
        		valid_states.append(newstate)

        #Moving Down
        if(m!=(len(puzzle)-1)):
        	newstate = copy.deepcopy(puzzle)
			newstate[m][n] = newstate[m+1][n]
        	newstate[m+1][n] = 0

        	#Check if this state is same as it's parent and add only if false
        	#Referenced https://stackoverflow.com/a/6105826 to convert state to set for ease of comparison

        	newstatelist = set(map(tuple, newstate))
        	parentlist = set(map(tuple, self.parent.curr_state))

        	if(newstatelist != parentlist):
        		valid_states.append(newstate)



        return valid_states





main()
