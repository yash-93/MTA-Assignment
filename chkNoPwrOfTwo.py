val = int(input())


def check(x):
   while x % 2 == 0:
       x = x / 2
   return x == 1


if check(val):
    print("Power of 2")
else:
    print("Not Power of 2")