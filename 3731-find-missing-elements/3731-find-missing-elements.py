class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        low = min(nums)
        high = max(nums)

        for i in range(low,high+1):
            if i not in nums:
                ans.append(i)
        return ans