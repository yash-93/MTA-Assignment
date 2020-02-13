class Test:
    def __init__(self, v1, v2):
        self.k1 = v1
        self.k2 = v2


V1 = int(input("Enter value 1 :: "))
V2 = int(input("Enter value 2 :: "))
obj = Test(V1, V2)
d = obj.__dict__
print(d)
