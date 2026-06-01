class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for s in strs:
            ss="".join(sorted(s))
            if ss not in seen:
                seen[ss]=[]
            seen[ss].append(s)
        return list(seen.values())
