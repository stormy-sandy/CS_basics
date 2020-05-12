"""
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Example 1:
Input: ["5","2","C","D","+"]
Output: 30
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.  
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
Example 2:
Input: ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3's data is invalid. The sum is: 3.  
Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.
Note:
The size of the input list will be between 1 and 1000.
Every integer represented in the list will be between -30000 and 30000.

"""
# Time:  O(n)
# Space: O(n)

# You're now a baseball game point recorder.
# Given a list of strings, each string can be one of the 4 following types:
#
# 1. Integer (one round's score): Directly represents the number of points
#    you get in this round.
# 2. "+" (one round's score): Represents that the points you get in
#                             this round are the sum of the last two valid
#                             round's points.
# 3. "D" (one round's score): Represents that the points you get in this round
#                             are the doubled data of the last valid round's
#                             points.
# 4. "C" (an operation, which isn't a round's score): Represents the last
#                             valid round's points you get were invalid and
#                             should be removed.
#
# Each round's operation is permanent and could have an impact on the round
# before and the round after.
# You need to return the sum of the points you could get in all the rounds.
#
# Example 1:
#
# Input: ["5","2","C","D","+"]
# Output: 30
# Explanation:
# Round 1: You could get 5 points. The sum is: 5.
# Round 2: You could get 2 points. The sum is: 7.
# Operation 1: The round 2's data was invalid. The sum is: 5.
# Round 3: You could get 10 points (the round 2's data has been removed).
#          The sum is: 15.
# Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
#
# Example 2:
#
# Input: ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# Round 1: You could get 5 points. The sum is: 5.
# Round 2: You could get -2 points. The sum is: 3.
# Round 3: You could get 4 points. The sum is: 7.
# Operation 1: The round 3's data is invalid. The sum is: 3.
# Round 4: You could get -4 points (the round 3's data has been removed).
#          The sum is: -1.
# Round 5: You could get 9 points. The sum is: 8.
# Round 6: You could get -4 + 9 = 5 points. The sum is 13.
# Round 7: You could get 9 + 5 = 14 points. The sum is 27.
#
# Note:
# The size of the input list will be between 1 and 1000.
# Every integer represented in the list will be between -30000 and 30000.

# V0 
# IDEA : STACK
class Solution(object):
    def calPoints(self, ops):
        stack=[]
        for op in ops:
            if op=='C':
                stack.pop()
            elif op=='D':
                stack.append(stack[-1]*2)
            elif op=='+':
                stack.append(stack[-2] + stack[-1]) 
            else:
                stack.append(int(op))
        return sum(stack)

# V1 
# http://bookshadow.com/weblog/2017/09/24/leetcode-baseball-game/
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)

### Test case
s=Solution()
assert s.calPoints(["5","2","C","D","+"]) == 30
assert s.calPoints(["5","-2","4","C","D","9","+","+"]) == 27
assert s.calPoints([]) == 0
assert s.calPoints(["10","10","10"]) == 30
assert s.calPoints(["10","10","+"]) == 40
assert s.calPoints(["10","10","C"]) == 10
assert s.calPoints(["10","10","D"]) == 40

# V2
class Solution(object):
    def calPoints(self, ops):
        history = []
        for op in ops:
            if op == '+':
                history.append(history[-1] + history[-2])
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == 'C':
                history.pop()
            else:
                history.append(int(op))
            print (history)
        return sum(history)

# V3
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        history = []
        for op in ops:
            if op == '+':
                history.append(history[-1] + history[-2])
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == 'C':
                history.pop()
            else:
                history.append(int(op))
        return sum(history)

# V4 
# Time:  O(n)
# Space: O(n)
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        history = []
        for op in ops:
            if op == '+':
                history.append(history[-1] + history[-2])
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == 'C':
                history.pop()
            else:
                history.append(int(op))
        return sum(history)
