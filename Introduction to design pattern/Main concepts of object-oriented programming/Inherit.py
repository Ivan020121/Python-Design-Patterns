'''
Created on June 4, 2022
@author: Ivan Li
'''

class A:
    def a1(self):
        print("a1")

class B(A):
    def b(self):
        print("b")

b = B()
b.a1()
#a1