import sys

def atr(file):
    '''
    This function takes the average of a file containing floats
    Input: File with iterable float values
    Output: Average of float values
    '''
    myfile = open(file)
    mylist = []
    for line in myfile:
        mylist.append(float(line))
    return round(sum(mylist) / len(mylist) , 5)

file = sys.argv[1]
print(atr(file))
