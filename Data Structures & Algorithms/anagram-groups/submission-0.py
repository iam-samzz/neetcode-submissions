class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for i in strs:
            val = str(sorted(i))
            if val not in d:
                d[val] = [i]
            else:
                d[val].append(i)
        for key in d:
            res.append(d[key])
        return res 