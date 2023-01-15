import matplotlib.pyplot as plt
import sys
import math
import collections

class Solution(object):
    def maxPoints(self, points):
        y_points, angs, result = [y for x, y in points], [], 1
        if len(points) == 1:
            return result
        for i in range(0,len(points)):
            for j in range(0,len(points)):
                if j != i:
                    ang = math.atan2((points[j][1]-points[i][1]),(points[j][0]-points[i][0]+1e-6))
                    angs.append(ang)
            c = collections.Counter(angs)
            angs = []
            if c.most_common()[0][1] > result:
                result = c.most_common()[0][1]
        return result+1
            
    points = [[1, 1], [2, 2], [3, 3]]
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    points = [[5151,5150],[0,0],[5152,5151]]
    print(maxPoints(maxPoints, points))
    
    y, x = [y for x, y in points], [x for x, y in points]
    plt.plot(x,y, 'bo')
    plt.grid()