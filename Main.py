from Cubiod import cube
from Sheilding import funcShortestSide
from Wiring import func2ShortestSides

w =cube.w 
l = cube.l
h = cube.h
sheilding = 0
wiring = 0
i = 0
y = 0

for x in w:
    sheilding += 2 * (l[i] * w[i]) + 2 * (w[i] * h[i]) + 2 * (l[i] * h[i])
    sheilding += funcShortestSide(w[i], l[i], h[i])
    i = i + 1

print ("Total Provisions for Sheilding: ", sheilding,"mm squared", "\n")

for x in w:
    wiring += w[y] * l[y] * h[y]
    wiring += func2ShortestSides(w[y], l[y], h[y])
    y = y + 1

print ("Total Provisions for Wiring: ", wiring,"mm squared","\n")