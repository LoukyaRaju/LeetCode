class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for i in range(len(strs)):
            word=sorted(strs[i])
            res[tuple(word)].append(strs[i])
        return list(res.values())


            