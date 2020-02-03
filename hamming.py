import binascii
import sys


def hammingdistance(hex1, hex2):
    bin1 = format((int(hex1, 16)), '032b')     # binary representation of the provided hex values
    bin2 = format((int(hex2, 16)), '032b')
    dist = 0
    for (bit1, bit2) in zip(bin1, bin2):  # iteration over each bit of both binary numbers
        if bit1 != bit2:
            dist += 1                     # tracks num of differing bits

    return dist


# statements used to create test values for hamming function
'''with open(sys.argv[1]) as file1:
    h1 = binascii.hexlify(file1.read())

with open(sys.argv[2]) as file2:
    h2 = binascii.hexlify((file2.read()))
'''
# testing
# print hammingdistance('ab13c', 'ab123')
