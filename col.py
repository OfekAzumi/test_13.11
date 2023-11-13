# Zip Function:
#   - myZip (x,y) --> function to zip 2 arrays together.
# ******************* if one array is longer, the data at the end get ignored.


def myZip(x,y):
    newLength = min(len(x),len(y)) # if one array is bigger, ignore this data
    newArr = []
    for i in range(newLength):
        newArr.append({x[i],y[i]})
    return newArr