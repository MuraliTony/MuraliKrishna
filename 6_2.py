'''
6.2) Implement a Python Script to rotate list of elements towards right up
     to given number of times. Example: Input: [23,34,9,45,19] and 2.
     Output: [45,19,23,34,9]
'''
list1 = [int(i) for i in input().split()]
rotations = int(input('Enter the number of Rotations:'))
list1 = (list1[-rotations:] + list1[:-rotations])
print(list1)
'''
Output:
23 34 9 45 19
Enter the number of Rotations:2
[45, 19, 23, 34, 9]
'''
