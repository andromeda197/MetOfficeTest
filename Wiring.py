def func2ShortestSides(w, l, h) -> int:
    array = [w, l, h]
    i = 0
    temp = 0
    sum = 0

    for i in range (0, 2):
        if(array[i] > array[i+1]):
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
        else:
            i = i + 1
        
    sum = 2 * array[0]
    sum += 2 * array[1]
    return sum
       


