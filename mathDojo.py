class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for i in nums:
            num += i
        self.result += num        
        return self
    def subtract(self, num, *nums):
        for i in nums:
            num += i
        self.result -= num
        return self

md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result
y = md.add(1,2).add(3,4,5).add(6,7,8,9).subtract(1,3).subtract(2,4,6).subtract(1,1,1,1).result


print("Test_1:", x, "\nTest_2:", y)