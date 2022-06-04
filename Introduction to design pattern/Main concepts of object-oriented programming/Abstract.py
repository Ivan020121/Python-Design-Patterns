'''
Created on June 4, 2022
@author: Ivan Li
'''

class Adder:
    def __init__(self):
        self.sum = 0
    def add(self, value):
        self.sum += value

acc = Adder()
for i in range(99):
    acc.add(i)

print(acc.sum)
#4851