'''A grand Team Chess Tournament will be held at your University. Two teams, smarties and cleveries, will clash to determine whose chess skills are better. The teams have the same number of members, and the ith member of smarties will play against the ith member of cleveries in the ith game for each valid i

Given the names of the players of both smarties and cleveries, return the games in the order they will be played.

Example

For smarties = ["Jane", "Bob", "Peter"] and
cleveries = ["Oscar", "Lidia", "Ann"], the output should be

chessTeams(smarties, cleveries) = [["Jane",  "Oscar"],
                                   ["Bob",   "Lidia"],
                                   ["Peter", "Ann"]]'''

def chessTeams(smarties, cleveries):
    return [[i,j] for i, j in zip(smarties, cleveries)]



'''Your teacher asked you to implement a function that calculates the Answer to the Ultimate Question of Life, the Universe, and Everything and returns it as an array of integers. After several hours of hardcore coding you managed to write such a function, and it produced a quite reasonable result. However, when you decided to compare your answer with results of your classmates, you discovered that the elements of your result are roughly 10 times greater than the ones your peers got.

You don't have time to investigate the problem, so you need to implement a function that will fix the given array for you. Given result, return an array of the same length, where the ith element is equal to the ith element of result with the last digit dropped.

Example

For result = [42, 239, 365, 50], the output should be
fixResult(result) = [4, 23, 36, 5].'''

def fixResult(result):
    def fix(x):
        return x // 10

    return list(map(fix, result))




'''John has just entered a college, and should now pick several courses to take. He knows nothing, except that number x is a bad luck for him, which is why he won't even consider courses whose title consist of x letters.

Given a list of courses, remove the courses with titles consisting of x letters and return the result.

Example

For x = 7 and
courses = ["Art", "Finance", "Business", "Speech", "History", "Writing", "Statistics"],
the output should be
collegeCourses(x, courses) = ["Art", "Business", "Speech", "Statistics"].'''

def collegeCourses(x, courses):
    def shouldConsider(course):
        return len(course) != x

    return list(filter(shouldConsider, courses))



'''A pair of numbers is considered to be cool if their product is divisible by their sum. More formally, a pair (i, j) is cool if and only if (i * j) % (i + j) = 0.

Given two lists a and b, find cool pairs with the first number in the pair from a, and the second one from b. Return the number of different sums of elements in such pairs.

Example

For a = [4, 5, 6, 7, 8] and b = [8, 9, 10, 11, 12],
the output should be
coolPairs(a, b) = 2.

There are three cool pairs that can be formed from these arrays: (4, 12), (6, 12) and (8, 8). Their respective sums are 16, 18 and 16, which means that there are just 2 different sums: 16 and 18. Thus, the output should be equal to 2.'''

def coolPairs(a, b):
    uniqueSums = {i+j for i in a for j in b if (i*j)%(i+j)==0}
    return len(uniqueSums)




'''You need to sum up a bunch of fractions that have different denominators. In order to do this, you need to find the least common denominator of all the fractions. As a professional programmer, you know that the least common denominator is in fact their LCM.

For the given list of denominators, find the least common denominator by finding their LCM.

Example

For denominators = [2, 3, 4, 5, 6], the output should be
leastCommonDenominator(denominators) = 60.'''

from fractions import gcd
from functools import reduce

def leastCommonDenominator(denominators):
    return reduce(lambda x,y: x*y/gcd(x,y), denominators)