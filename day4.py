'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

arr = [3, 4, -1, 1]
arr = [1, 2, 0]

def getLowestMissingInt(arr):
    length = len(arr)
    number = 0

    for e in arr:
        if e > 0:
            number = number | (1 << (e-1))
        else:
            length -= 1
    for i in range(len(arr)):
        digit = 1 << i
        if digit & number == 0:
            return i + 1
    return len + 1

a = getLowestMissingInt(arr)
print(a)
