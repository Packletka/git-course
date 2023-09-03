class Solution(object):
    def twoSum(self, nums, target):
        count = -1
        for j in range(0, len(nums) - 1):
            count += 1
            for i in range(count + 1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [j, i]


obj = Solution()
print(obj.twoSum([1, 2, 3, 4, 5, 666, 999, 0], 1))
