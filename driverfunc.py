#Defining the goal state as a global variable to avoid declaring it in every function separately
final_state = [[1,2,3], [4,5,6], [7,8,0]]

#Main function for taking inputs regarding mode of puzzle
def main():
	print('Welcome to my 8-puzzle solver!\n Select one of the following numbers for the puzzle: \n')
	print('1 - Default puzzle or 2 - Create your own custom puzzle!\n')

	puzzle_mode = input()

	if(puzzle_mode == '1'):
		default_mode()
	elif(puzzle_mode == '2'):
		custom_mode_input()
	else:
		print('Please enter a valid input!\n')
		main()


#Function for choosing a puzzle from the pre-defined ones
def default_mode():
	
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

	choose_search_method(start_state)


#Function for choosing a search method
def choose_search_method(start_state):
	
	print('Choose the search method you would like to use :\n')
	
	print('1 - Uniform Cost Search\n')
	print('2 - A* with Manhattan Distance heuristic\n')
	print('3 - A* with Misplaced Tile Heuristic\n')

	search_type = input()

	if(search_type == '1'):
		uniform_cost_search(start_state)
	elif(search_type == '2'):
		astar_manhattan(start_state)
	elif(search_type == '3'):
		astar_misplaced_tile(start_state)
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

def uniform_cost_search(start_state):
	

main()
