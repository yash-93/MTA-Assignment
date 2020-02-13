MyList = []
for val in input().split():
    MyList.append(int(val))
max_ele = max(MyList)
MyList.remove(max_ele)
if max_ele in MyList:
    MyList.remove(max_ele)
print(max(MyList))