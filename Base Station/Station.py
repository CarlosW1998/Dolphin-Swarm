from shapely.geometry import Polygon
from shapely.ops import cascaded_union
import math


CASE = 0
cases = [[(219,287), (219,393), (312,234), (312,340), (312,448), (405,287), (405,393)],
    [(127,124), (127,231), (127,340), (127,448), (220,178), (220,286),
    (220,394), (220,502), (312,124), (312,231), (312,340), (312,448), (406,178),
    (406,286), (406,394), (406,502), (499,124), (499,231), (499,340), (499,448)]]
radiosCenter = [63, 63]
radiosCircle = [63, 170]
nBases = [7, 3]

def createPoints2Poly(side, center, radius):
    angle = 2*math.pi/side
    points = []
    for i in range(side):
        x = center[0] + radius*math.cos((i)*angle)
        y = center[1] + radius*math.sin((i)*angle)
        points.append((x, y))

    return tuple(points)

def getCircles(circles):
    circles = [(circles[i], circles[i+1]) for i in range(0, len(circles), 2)]
    stationsBase = []
    for i in circles:
        stationsBase.append(createPoints2Poly(100, i, radiosCenter[CASE]))
    return stationsBase

def getCity():
    city = []
    for i in cases[CASE]:
        city.append(createPoints2Poly(6, i, radiosCenter[CASE]))
    
    
    return city

def fitness(circles):
    
    citys = getCity()
    cityArea = []
    for i in citys:
        cityArea.append(Polygon(i))
    cityArea = cascaded_union(cityArea)
    stationsBase = []
    for i in circles:
        stationsBase.append(Polygon(createPoints2Poly(100, i, radiosCenter[CASE])))
    stationsBase = cascaded_union(stationsBase)
    finalp = cascaded_union([stationsBase, cityArea]) 
    return (finalp.area - stationsBase.area)