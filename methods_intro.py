def do(thing):
    return str(thing)+str(1)
print do(5)
print'----------------'

def do(one, two=5):
    return one+two
print do(6)
print'-------------------'


def do(a,b):
    a=5
    b=5
    return a*b
inp=8
do(inp,5)
print inp
print'----------------'

def try_to_change_list_contents(the_list):
    the_list.append('four')

outer_list=['one','two','three']

try_to_change_list_contents(outer_list)
print outer_list
