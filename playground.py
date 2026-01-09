
def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum

print(add(1,2,3,4,5,6,7,8,9,10))

def calcullate(n,**kwargs):
    print(kwargs["age"])
    n+=kwargs["age"]
    print(n)


calcullate(2,name='A',age=20)
calcullate(5,name='B',age=20)