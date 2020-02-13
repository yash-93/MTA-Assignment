MyList = []
for val in input().split():
    MyList.append(int(val))
even = list(filter(lambda x : x % 2 == 0, MyList))
odd = list(filter(lambda x : x % 2 != 0, MyList))
print("Even elements => ", even)
print("Odd elements => ", odd)