import sys
# Part 1: Build a program that outputs a christmas tree of arbitrary height
def christmasTree(n):
	# input n is the height of the tree
	# top is always 1
	# second highest level is 1+2*1
	# thrid highest level is 1+2*2 and so on
	# lowest level will be 1 + 2*(n-1)
	# so the difference between bottom level and top level is (n-1) whitespaces on each side of the top star
	# the whitespaces will decrease by 1 when build from top to bottom

	# print top level
	print(' '*(n-1) + '*' + ' '*(n-1))

	# print the rest levels, build from top to bottom
	for i in range(1,n): 
		whiteSpaces = ' ' * (n-1-i)
		stars = '*'*(1+(2*i))
		print(whiteSpaces + stars + whiteSpaces)




# Part 2: Same as above but with this design. Basically an X of arbitrary height.
def buildX(n): # n is the height of the X
	# build the X from top to bottom
	# every level has two starts except the middle level
	# thus for all levels except the middle on, there are two pointers,
	# One pointer start from left on top level and goes to right by one on next level,
	# another pointer starts from right on top level and goes to left by on on next level



	for i in range(n):
		pointer1 = i
		pointer2 = n-i-1 
		for i in range(n):
			if i == pointer1:
				print('*',end='')
			elif i == pointer2:
				print('*',end='')
			else:
				print(' ',end='')
		print()



def main(argv):
	if len(argv) != 3:
		print("Please enter: python3 test.py T(or X) num \nWhere 'T' stards for building christmas Tree, 'X' stands for building X, and 'num' stands for the height of the tree of X")
	if argv[1] == 'T':
		christmasTree(int(argv[2]))
	if argv[1] == 'X':
		buildX(int(argv[2]))

if __name__ == "__main__":
   main(sys.argv)







