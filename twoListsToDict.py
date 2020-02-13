L1 = []
for val in input("Enter space separated List 1 :: ").split():
    L1.append(val)
L2 = []
for val in input("Enter space separated List 2 :: ").split():
    L2.append(val)
D = {}
i = 0
try:
    for k in L1:
        D[k] = L2[i]
        i += 1
except Exception as e:
    print("Error : ", e)
finally:
    print(D)
