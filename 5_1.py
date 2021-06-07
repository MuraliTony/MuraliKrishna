'''
5.1) Implement a python script to count frequency of characters in a given string.
'''

input_str = input('Enter a string: ')

alphabet_count = {}

for character in input_str:
	alphabet_count[character] = alphabet_count.get(character,0) + 1


for key in sorted(alphabet_count.keys()):
	print('Count of {} is {}'.format(key,alphabet_count[key]))


'''
Output:
Enter a string: python programs
Count of   is 1
Count of a is 1
Count of g is 1
Count of h is 1
Count of m is 1
Count of n is 1
Count of o is 2
Count of p is 2
Count of r is 2
Count of s is 1
Count of t is 1
Count of y is 1
'''
