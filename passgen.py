from random import SystemRandom

def passgen(wordcount, seperator=''):
    with open('eff_large_wordlist.txt') as fil:
        words = fil.readlines()
    rand = SystemRandom()
    words = [i.split() for i in words]
    nums = [[str(rand.randint(1,6)) for i in range(5)] for j in range(wordcount)]
    nums = [seperator.join(i) for i in nums]
    password = ''
    #TODO: binary search
    for i in nums:
        for j in words:
            if i == j[0]:
                password += j[1]
                break
    return password
