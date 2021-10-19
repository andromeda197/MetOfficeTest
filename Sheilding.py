def funcShortestSide(w, l, h) -> int:
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
        
    sum = array[0] * array[1]
    return sum
        

    
       














