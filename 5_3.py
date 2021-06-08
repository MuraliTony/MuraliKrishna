'''
5.3
Implement a python script to count number of words in a string and reverse each word in a string at the same location. Example:
Input :Honesty is the best policy
Output :5 ytseno Hsiehttsebycilop.
'''


input_str = input('Enter a string: ')
input_str_list = input_str.split(' ')
count = len(input_str_list)

output_str_list = []

for word in input_str_list:
	output_str_list.append(word[-1::-1])

print('Word Count:',count)
print(' '.join(output_str_list))

'''
Output:
Enter a string: I am Murali
Word Count: 3
I ma ahtraddiS
'''
