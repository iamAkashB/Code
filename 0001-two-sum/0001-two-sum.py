class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            ser = target - nums[i]
            if ser in mp:
                return [mp[ser] , i]
            else:
                mp[nums[i]] = i
