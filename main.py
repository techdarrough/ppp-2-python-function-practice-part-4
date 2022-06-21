# Write a Python function called max_num()to find the maximum of three numbers.




def maxNum(a, b, c):
    return max([a, b, c])


print(maxNum(1, 2, 3))

# Write a Python function called mult_list()  to multiply all the numbers in a list.


def multList(list):
    if len(list) == 0:
        return 0
    prod = list[0]
    if len(list) > 1:
        for i in list[1:]:
            prod = prod * i
    return prod


print(multList([1, 2, 3]))
print(multList([]))
print(multList([15]))

# Write a Python function called rev_string() to reverse a string.


def revString(string):
    if len(string) == 0:
        return

    temp = string[0]
    revString(string[1:])
    print(temp, end='')


print(revString(""))
print(revString("apple"))
print(revString("mt string"))

# Write a Python function called num_within() to check whether a number falls in a given range.


def numWithin(n, fist, last):
    return n in range(fist, last+1)


print(numWithin(3, 2, 4))
print(numWithin(3, 1, 3))
print(numWithin(10, 2, 5))


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.


def pascal(number):
  for i in range(number): #for is the most apporaite approach
    print(' '*(number-i), end='') #adjusting space on left
    print(' '.join(map(str, str(11**i)))) #join computations
pascal(2)
pascal(5)