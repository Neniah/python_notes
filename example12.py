
# Expected an indent
def func1():
    def func2():
        print(2)

# Unexpected indent:
def task():
    print('1')
print('2')
    print('3')

#or
print('hello)
