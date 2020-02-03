import hashlib
import random
import string


def random_string(n):  # helper function that creates a random string of n printable ascii characters
    return ''.join([random.choice(string.printable) for i in range(n)])


def find_preimage(target, n):
    d = {}
    # trials = 0
    while 1:
        # trials += 1
        collisions = 0
        rand = random_string(random.randint(1, 100))
        if rand in d:  # skip previously seen strings
            continue
        else:
            m = hashlib.sha256(rand).digest()
            d[rand] = m
        # print target.encode('hex)
        # print m.encode('hex')
        for (byte1, byte2) in zip(target, m):  # byte comparison to detect collisions
            if byte1 != byte2:
                break
            else:
                collisions += 1
        if collisions >= n:
            break
        else:
            continue
    # print trials
    return rand


# The below comments were used for testing purposes
# testHash = hashlib.sha256(b"The quick brown fox jumps over the lazy dog.").digest()

# find_preimage(testHash, 2)

