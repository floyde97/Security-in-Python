import hashlib
import random
import string


def random_string(n):  # helper function that creates a random string of n printable ascii characters
    return ''.join([random.choice(string.printable) for i in range(n)])


def find_collision(n):
    d = {}
    trials = 0
    while 1:
        trials += 1
        collisions = 0
        rand_int = random.randint(1, 100)
        rand1 = random_string(rand_int)
        rand2 = random_string(rand_int)
        h1 = hashlib.sha256(rand1).digest()
        h2 = hashlib.sha256(rand2).digest()
        test1 = ''
        test2 = ''
        for index in range(n):
            test1 = test1 + str(h1[index])
            test2 = test2 + str(h2[index])

        if rand1 == rand2:
            continue
        if test1 in d:  # checks if the first n bytes has been seen before
            # print(test1)
            if rand1 != d[test1]:
                # print h1.encode('hex')
                # print hashlib.sha256(d[test1]).hexdigest()
                # print trials
                return rand1, d[test1]
            else:
                continue
        else:
            d[test1] = rand1

        if test2 in d:
            # print(test2)
            if rand2 != d[test2]:
                # print h2.encode('hex')
                # print hashlib.sha256(d[test2]).hexdigest()
                # print trials
                return rand2, d[test2]
            else:
                continue
        else:
            d[test2] = rand2

        for (byte1, byte2) in zip(h1, h2):  # byte comparison to detect collisions
            if byte1 != byte2:
                break
            else:
                collisions += 1
        if collisions >= n:
            # print h1.encode('hex')
            # print h2.encode('hex')
            break
        else:
            continue
    # print trials
    return rand1, rand2
