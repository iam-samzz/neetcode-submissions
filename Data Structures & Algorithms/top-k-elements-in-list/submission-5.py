class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] = d[nums[i]]+1
        while k!=0:
            highest = float('-inf')
            highestKey = None
            for key in d:
                if d[key]>highest:
                    highest = d[key]
                    highestKey = key
            res.append(highestKey)
            del d[highestKey]
            k-=1
        return res
            

