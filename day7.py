'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''


def get_permutations(number_string):
    if len(number_string) < 2:
        return 1

    if len(number_string) == 2:
        if can_permute(number_string):
            return 2
        return 1

    number = get_permutations(number_string[2:])

    if can_permute(number_string[:2]):
        number += get_permutations(number_string[2:])

    if can_permute(number_string[1:3]):
        number += get_permutations(number_string[3:])

    return number


def can_permute(string):
    assert len(string) == 2
    if string[0] == "1":
        return True
    return string[0] == "2" and string[1] in "123456"

a = get_permutations("111")
print(a)
