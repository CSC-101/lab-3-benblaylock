print("TASK ONE")
more = [x+1 for x in [1,2,3,4]]
print(more)
# for each value in the list, it adds 1
# more = [2,3,4,5]

def square(n:int) -> int:
    return n*n
squares = [square(x) for x in [1,2,3,4]]
print(squares)
# square is called 4 times with n as 1,2,3,4 and returns 1,4,9,16
# squares = [1,4,9,16] (each value in the list squared)

def check(n:int) -> bool:
    return n>2
answer = [x for x in range(5) if check(x)]
print(answer)
# n = 0,1,2,3,4 and only gets returned at 3,4
# answer = [3,4]

def inc(m:int) -> int:
    return m + 1
def check(n:int) -> bool:
    return n > 2

answer = [inc(x) for x in range(5) if check(x)]
print(answer)
#range(5) gives values 0-4, inc adds 1 to each of them, check only lets 3,4 pass through to inc.
#answer = [4,5]

print("TASK TWO")

def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num
    return total

result = tally([4,9,2,1])
# total goes from 4,13,15,16

def copy(nums:list[int]) -> list[int]:
    newlist = []
    for idx in range(len(nums)):
        newlist.append(nums[idx])
    return newlist
result = copy([4,9,2,1])
print(result)
# idx goes from 0 to 3, and newlist gets appended each index of nums (4,9,2,1)
# this differs from above in that it makes a new list, not connected to the original, whereas the
# other function changes the original

def incrementall(nums:list[int]) -> list[int]:
    newlist = []
    for value in nums:
        newlist.append(value+1)
    return newlist
result = incrementall([4,9,2,1])
print(result)
# newlist is [5,10,3,2]