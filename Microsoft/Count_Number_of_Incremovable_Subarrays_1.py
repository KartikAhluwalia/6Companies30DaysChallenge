class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n+1):
                sub = nums[:i] + nums[j:]
                if all(sub[k]<sub[k+1] for k in range(len(sub)-1)):
                    ans+=1

        return ans
        