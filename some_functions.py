import random

def find_sum(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum


def f(nums, val):
    if val in nums:
        nums.remove(val)
    else:
        nums.append(val)
    return nums
    
def k(num):
    for i in range(1,num):
        if i % 3 == 0 and i % 5 == 0:
            print('FooBar')
        elif i % 5 == 0:
            print('Bar')
        elif i % 3 == 0:
            print('Foo')
        else:
            print(i)


def dice100():
    return random.randint(1,100)
def gtn():
    kakaha = dice100()
    while 1 == 1:
        b = int(input('Guess the number!!!!!!!11!'))
        if b > kakaha:
            print('The number is smaller!')
        elif b < kakaha:
            print('The number is bigger!')
        else:
            print('You won!')
            break
