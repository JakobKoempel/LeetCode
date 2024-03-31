class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n >= 2:
            return 0.5
        else:
            return 1