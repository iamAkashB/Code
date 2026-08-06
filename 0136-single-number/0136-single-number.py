class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = {}
        for arr in nums:
            if arr in mp:
                mp[arr] +=1
            else:
                mp[arr] = 1
        
        for m in mp:
            if mp[m] == 1:
                return m