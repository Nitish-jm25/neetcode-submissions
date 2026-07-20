class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # 1. Fill Left products: left[i] stores product of everything before i
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
            
        # 2. Fill Right products: right[i] stores product of everything after i
        right = [1] * n
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            
        # 3. Combine them into final output
        output = []
        for i in range(n):
            output.append(left[i] * right[i])
            
        return output
