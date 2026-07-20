class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen={}
        op=[]
        for i in range(n):
            pd=1
            for j in range(n):
                if i!=j:
                    pd*=nums[j]
            op.append(pd)
        return op