class Solution:
    def twoSum(self, nums, target):
        mydict = []
        for i, num in enumerate(nums):
            if target - num in mydict:
                return [i, nums.index(target - num)]
            else:
                mydict.append(num)


nums = [3, 3]
target = 6

solution = Solution()
print(solution.twoSum(nums, target))
