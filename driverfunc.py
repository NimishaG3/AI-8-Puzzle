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






main()
