class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visitados = set()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in visitados:
                return [i, nums.index(diff)]
            visitados.add(nums[i])
