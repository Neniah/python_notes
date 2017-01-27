# Input from User:
'''
name = input('What is your name?: ')
print('Hello', name)
'''
import statistics

exList = [4,3,4,6,1,7,8,5,9 ]

x = statistics.mean(exList)
print(x)

x = statistics.median(exList)
print(x)

x = statistics.mode(exList)
print(x)

x = statistics.stdev(exList)
print(x)

x = statistics.variance(exList)
print(x)
