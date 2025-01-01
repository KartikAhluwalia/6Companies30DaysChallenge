class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        if x1 <= xCenter <= x2:
            x = 0
        else:
            x = min(abs(x1 - xCenter), abs(x2 - xCenter))
        
        if y1 <= yCenter <= y2:
            y = 0
        else:
            y = min(abs(y1 - yCenter), abs(y2 - yCenter))
        
        return x**2 + y**2 <= radius**2
