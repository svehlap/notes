"""Sample solutions from various students"""

## Exercise 1

# Martin's solution:
def vowelcount(s):
    """Count vowels in s"""
    s = s.lower()
    nv = 0
    for v in 'aeiou':
        nv += s.count(v)
    return nv


# Student solution 1:
def vowelcount(string):
    """This function counts the number of vowels in the string 'string'"""
    """ Input: string, Output: number of vowels as integer              """
    vowels = ['a', 'e', 'i', 'o', 'u'] #define vowels
    num_vowels = 0 #start counting from 0
    for i in range(len(string)):
        if string[i] in vowels or string[i].lower() in vowels: #doesn't matter if in lower or upper case
            num_vowels += 1 #add 1 to count if this is true
        else:
            continue
    return num_vowels


# Student solution 2:
def vowelcount(x):
    """Returns the number of vowels in a given string"""
    low = (str.lower(x))
    count = low.count('a') + low.count('e') + low.count('i') + low.count('o') + low.count ('u')
    print ('"' + x + '"' + ' contains %i vowels' %count)


# Student solution 3:
def vowelcount(str):
    vowel_list = "aeiouAEIOU"
    vowel_count = 0
    for letter in str:
        if letter in vowel_list:
            vowel_count = vowel_count + 1
    return (vowel_count)


# Student solution 4:
"""counts the number of vowels in a word"""
def vowelcount(word):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    number_of_vowels = 0
    for all_vowels in vowels:
        number_of_vowels = number_of_vowels + word.count(all_vowels)
        return number_of_vowels


# Student solution 5:
def vowelcount(string):
    """returns number of vowels in a string"""
    l = string.lower()
    a = l.count('a')
    e = l.count('e')
    i = l.count('i')
    o = l.count('o')
    u = l.count('u')
    return a, e, i, o, u


# Student solution 6:
def vowelcount(string):
    """Take a string, returns number of vowels"""
    s2 = string.lower()
    new = s2.replace('a','x').replace('e','x').replace('i','x').replace('o','x').replace('u','x')
    result = new.count('x')
    return result


## Exercise 2

# Martin's solution:
def metric(x, y):
    """Calculate difference over sum"""
    d = x - y
    s = x + y
    print('difference is %g, sum is %g' % (d, s))
    # optional: handle divide by zero:
    #if s == 0:
    #    return 0
    return d / s


# Student solution 1:
def metric(x, y):
    """this function prints the difference and sum of x and y and returns diff/sum"""
    sum = x + y
    diff = x - y
    if type(sum) == float and type(diff) == float:
        print('sum is %f and difference is %f' %(sum, diff))
    else:
        print('sum is %i and difference is %i' %(sum, diff))
    if sum == 0:
        print('output error: sum is zero')
        return None
    else:
        return diff / sum


# Student solution 2:
def metric(x,y):
    """calculates difference, sum and difference/sum"""
    difference = x - y
    sum = x + y
    print("difference is %f" % difference)
    print("sum is %f" % sum)
    return 0 if sum == 0 else difference / sum


# Student solution 3:
def metric(x, y):
    """Prints difference, sum  auf x and y and returns difference/sum"""
    sum1 = x + y
    dif = x - y
    if sum1 != 0:
        divide = dif // sum1
    else:
        divide = 'N/A, sum is zero'
    return 'difference is ', dif, 'sum is', sum1, '; difference/sum=', divide


## Exercise 3

# Martin's solution:
def multtable(n):
    """Print multiplication table from 1 to n"""
    for i in range(1, n+1): # rows
        for j in range(1, n+1): # columns
            print(i * j, end=' ')
        print() # move to new line for next row


# Student solution 1:
def multtable(n):
    """Prints the mutliplication table from 1 to n in rows"""
    for i in range(1,n+1):
        for n in range(1,11):
            print(n*i, end = ' ')
        print()


# Student solution 2:
def multtable(n):
    """ This function takes a number n as an argument and prints out the multiplication table
    for integers 1 through n. """
    for i in range(n):
        row = []
        for j in range(n+1):
            num = (i + 1) * (j + 1)
            row.append(num)
        print(row[:n], sep = ',', end = '\n')
