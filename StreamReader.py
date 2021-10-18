from os import close

data = open("example2.txt", "r")
cuboidArray = []
width = []
length = []
height = []
i = 0

for x in data:
     cuboidArray.append(x)
     temp = cuboidArray[i].split("x") 

     width.append(int(temp[0], base = 10))
     length.append(int(temp[1], base = 10))
     height.append(int(temp[2], base = 10))

     i = i + 1
close

    