from random import SystemRandom

def passgen(wordcount, sep=''):
    with open('eff_large_wordlist.txt') as fil:
        words = fil.readlines()
    rand = SystemRandom()
    words = [i.split() for i in words]
    nums = [[str(rand.randint(1,6)) for i in range(5)] for j in range(wordcount)]
    nums = [''.join(i) for i in nums]
    password = [None] * wordcount
    for i in range(wordcount):
        password[i] = words[convtoindex(nums[i])]
    return sep.join(password)

def convtoindex(num):
    digits = [int(i) for i in num]
    ind = 0
    for i in range(5):
        ind += (digits[4-i] - 1) * 6**i
    return ind
    