'''A spiral matrix is a square matrix of size n × n. It contains all the integers in range from 1 to n * n so that number 1 is written in the bottom right corner, and all other numbers are written in increasing order spirally in the counterclockwise direction.

Given the size of the matrix n, your task is to create a spiral matrix.

Example

For n = 3, the output should be

createSpiralMatrix(n) = [[5, 4, 3],
                         [6, 9, 2],
                         [7, 8, 1]]'''

def createSpiralMatrix(n):
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    curDir = 0
    curPos = (n - 1, n - 1)
    res = [[0 for x in range(n)] for y in range(n)]

    for i in range(1, n * n + 1):
        res[curPos[0]][curPos[1]] = i
        nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        if not (0 <= nextPos[0] < n and
                0 <= nextPos[1] < n and
                res[nextPos[0]][nextPos[1]] == 0):
            curDir = (curDir + 1) % 4
            nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        curPos = nextPos

    return res


'''A 2D list lst of size 2 * n - 1 is called a shell if it is filled with zeros and has the following configuration:

    lst[0] contains one element;
    lst[1] contains two elements;
    ...
    lst[n - 2] contains n - 1 elements;
    lst[n - 1] contains n elements;
    lst[n] contains n - 1 elements;
    ...
    lst[2 * n - 3] contains two elements;
    lst[2 * n - 2] contains one element.

Given an integer n, return a shell list.

Example

For n = 3, the output should be

constructShell(n) = [[0],
                     [0, 0],
                     [0, 0, 0],
                     [0, 0],
                     [0]]'''

def constructShell(n):
    return [[0]*min(i,2*n-i) for i in range(1, 2*n)]


'''You've heard somewhere that a word is more powerful than an action. You decided to put this statement at a test by assigning a power value to each action and each word. To begin somewhere, you defined a power of a word as the sum of powers of its characters, where power of a character is equal to its 1-based index in the plaintext alphabet.

Given a word, calculate its power.

Example

For word = "hello", the output should be
wordPower(word) = 52.

Letters 'h', 'e', 'l' and 'o' have powers 8, 5, 12 and 15, respectively. Thus, the total power of the word is 8 + 5 + 12 + 12 + 15 = 52.'''

def wordPower(word):
    num = num = {char : ord(char) - 96 for char in word}
    return sum([num[ch] for ch in word])

