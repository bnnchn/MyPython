#!/usr/bin/env python3

def add(myList):
    """Returns the sum of the elements in the given list."""
    sum = 0
    for num in myList:
        sum = sum + num
    return sum


print(add([0, 1, 2, 3]))

myNumbers = range(101)
print(add(myNumbers))


def addUpTo(largest):
    """Returns the sum of the integers from 0 to largest."""
    sum = 0
    for num in range(0, largest + 1):
        sum = sum + num
    return sum


print(addUpTo(100))


def gum(times):
    """Apologizes for gum chewing the given number of times."""
    for line in range(times):
        print('I will not chew gum in class')


print(gum(2))
print(gum(5))


def countCCAAT(DNA):
    """Computes number of occurrences of CCAAT in input string."""
    counter = 0
    for index in range(len(DNA)):
        if DNA[index:index + 5] == 'CCAAT':
            counter = counter + 1
    return counter


print(countCCAAT('GGCCAATT'))


def multiCountCCAAT(DNAList):
    """Prints the number of occurences of CCAAT in each string in given DNAList."""
    for DNA in DNAList:
        counter = 0
        for index in range(len(DNA)):
            if DNA[index:index + 5] == 'CCAAT':
                counter = counter + 1
        print(counter)


multiCountCCAAT(['GGCCAATT', 'CAT', 'CCAATCCAAT'])