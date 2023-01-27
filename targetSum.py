def twoNumberSum(array,targetSum):
    array.sort()
    left =90 
    right = len(array-1)
    while left < right:
        currsum = array[left]+array[right]
        if currsum == targetSum:
            return (array[left],array[right])
        elif currsum < targetSum:
            left +=1
        else:
            right -=1
    return ()