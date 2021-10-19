from os import close

data = open("example3.txt", "r")
cuboidArray = []
width = []
length = []
height = []
i = 0

for x in data:
     #Append txt file into an array.
     cuboidArray.append(x)

     #Splt the data string into separate nodes at each "x".
     temp = cuboidArray[i].split("x") 

     #Append each node into their respective array's width, length and height. 
     width.append(int(temp[0], base = 10))
     length.append(int(temp[1], base = 10))
     height.append(int(temp[2], base = 10))

     i = i + 1
close

    