# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

print(2**65536)

'''
JavaScript outputs Infinity

Computers represent data with bits (short for binary digits)
The JS `Number` type is a 64-bit double-precision floating point number
MAX_SAFE_INTEGER in JS is (2**53 - 1) or 9007199254740991

However, bitwise operators and shift operators operate on 32-bit integers
So in practice, the max safe integer is (2**31 - 1) or 2147483647

In Python 3, the `int` type is unbounded
'''