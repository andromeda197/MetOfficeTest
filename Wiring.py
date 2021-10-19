i = 0
answer = 0

def func2ShortestSides(w, l, h) -> int:
    temp = 0
       
    if(w <= l and w <= h):
        if(l < h or l == h):
            temp = w + l
            return temp
        else: 
            temp = w * h
            return temp
    
    elif(l <= w and l <= h):
        if(w < h or w == h):
            temp = l + w
            return temp
        else: 
            temp = l * h
            return temp
    
    elif(h <= w and h <= l):
        if(w < l or w == l):
            temp = h + w
            return temp
        else: 
            temp = h + l
            return temp

