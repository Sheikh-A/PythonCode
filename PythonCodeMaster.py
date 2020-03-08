#Pick even numbers from a list

def myfunc(*args):
    output = []
    for num in args:
        if (num%2==0):
            output.append(num)
    return output


#Take string return uppercase if even lowercase if odd
def myfunc(string):
    new_string = ''
    for x in range(len(string)):
        if (x+1)%2==0:
            new_string += string[x].upper()
        else:
            new_string += string[x].lower()
    return new_string
