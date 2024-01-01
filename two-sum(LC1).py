def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1 = list()
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if j!=i :
                    sum=nums[i]+nums[j]
                    if sum==target:
                        list1 = [i, j]
                        list1.sort()
                        return list1
