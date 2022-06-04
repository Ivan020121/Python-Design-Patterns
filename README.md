# Python-Design-Patterns
## Executive summary
`Design pattern` is one of the most powerful methods to build large software systems. Optimizing software architecture and design has gradually become an important topic in the process of software development and maintenance.

Through 11 chapters, this book comprehensively reveals the content of design patterns, and analyzes them by examples in combination with `Python language`. The book includes many design patterns, such as single instance design pattern, factory pattern, facade pattern, agent pattern, observer pattern, command pattern, template method pattern, composite pattern, state design pattern and anti pattern.

This book is suitable for readers who pay attention to `software design principles` and want to apply excellent design patterns to python programming. It is also suitable for ordinary software engineers and architects.

----
## Prologue
```
"Control complexity is the essence of computer programming"
——Brian Kernighan
```
```
"All problems in computer science can be solved through abstraction"
——David Wheeler
```
The above quotes from two famous computer scientists deeply explain the problems faced by modern software designers, that is, the urgent need to provide an excellent, stable, reusable and flexible solution for software design.

In fact, design patterns can solve these problems in the most elegant way. Design patterns are abstract and exist in clean and well-designed components and interfaces, which are valuable experience accumulated by many software designers and architects in solving similar problems for many years. These solutions have been tested for a long time in terms of reusability, flexibility, scalability and maintainability.

----
## Perface
`Design patterns` are one of the most powerful ways to build large software systems. As people pay more and more attention to the optimization of software architecture and design, it is increasingly important for software architects to consider the optimization of object creation, code structure and interaction between objects at the architecture or design level. Because this can not only reduce the maintenance cost of the software, make the code easy to reuse, but also make the code adapt to changes. In addition, the framework with reusability and independence is the key to software development today.

---
## Requirements
* python 3.6

---
## Code layout conventions
The code snippet displays:
```python
class Person(object):
    def __init__(self, name, age):    #constructor
        self.name = name    #data members/ attributes
        self.age = age
    def get_person(self, ):    # member function
        return "<Person (%s, %s)>" % (self.name, self.age)

p = Person("John", 32)    # p is an object of type Person
print("Type of Object:", type(p), "Memory Adress:", id(p))
#Type of Object: <class '__main__.Person'> Memory Adress: 2525564873936
```

---
## Corrigendum
Although I will try my best to ensure the accuracy of the code, mistakes are still inevitable. If you find errors in your code and are willing to submit them to me, I would be grateful. This will not only dispel the doubts of other readers, but also help to improve the follow-up. If you want to submit the error you found, please send the error correction details to the email liwenhao0504@163.com.

