# V0 

# V1' 
# https://blog.csdn.net/fuxuemingzhu/article/details/79247916
# http://bookshadow.com/weblog/2017/07/24/leetcode-set-mismatch/
# IDEA : SUM
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        nset = set(nums)
        missing = N * (N + 1) / 2 - sum(nset)
        duplicated = sum(nums) - sum(nset)
        return [duplicated, missing]
               
# V1' 
# https://blog.csdn.net/fuxuemingzhu/article/details/79247916
# http://bookshadow.com/weblog/2017/07/24/leetcode-set-mismatch/
# IDEA : HASH TABLE 
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashs = [0] * len(nums)
        missing = -1
        for i in range(len(nums)):
            hashs[nums[i] - 1] += 1
        return [hashs.index(2) + 1, hashs.index(0) + 1]

# V2 
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x_xor_y = 0
        for i in range(len(nums)):
            x_xor_y ^= nums[i] ^ (i+1)
        bit =  x_xor_y & ~(x_xor_y-1)
        result = [0] * 2
        for i, num in enumerate(nums):
            result[bool(num & bit)] ^= num
            result[bool((i+1) & bit)] ^= i+1
        if result[0] not in nums:
            result[0], result[1] = result[1], result[0]
        return result


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * 2
        for i in nums:
            if nums[abs(i)-1] < 0:
                result[0] = abs(i)
            else:
                nums[abs(i)-1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                result[1] = i+1
            else:
                nums[i] *= -1
        return result

# Time:  O(n)
# Space: O(1)
class Solution3(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        x_minus_y = sum(nums) - N*(N+1)//2
        x_plus_y = (sum(x*x for x in nums) - N*(N+1)*(2*N+1)/6) // x_minus_y
        return (x_plus_y+x_minus_y) // 2, (x_plus_y-x_minus_y) // 2
