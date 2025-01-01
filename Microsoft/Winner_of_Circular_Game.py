class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        q = deque()
        for i in range(1,n+1):
            q.append(i)

        while len(q)>1:
            for i in range(k-1):
                num = q.popleft()
                q.append(num)
            q.popleft() #At kth element we remove it from the game
            
        return q[0]
        