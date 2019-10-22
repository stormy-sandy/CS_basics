# V0

# V1
# https://blog.csdn.net/zhangpeterx/article/details/100056015
class Solution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        a, b = 0, 1
        for i in range(1, N):
            a, b = b, a+b
        return b

# V2
# Time:  O(logn)
# Space: O(1)
import itertools
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        def matrix_expo(A, K):
            result = [[int(i==j) for j in range(len(A))] \
                      for i in range(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result

        def matrix_mult(A, B):
            ZB = zip(*B)
            return [[sum(a*b for a, b in itertools.izip(row, col)) \
                     for col in ZB] for row in A]

        T = [[1, 1],
             [1, 0]]
        return matrix_expo(T, N)[1][0]

# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in range(N):
            prev, current = current, prev + current,
        return prev