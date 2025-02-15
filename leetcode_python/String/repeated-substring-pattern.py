"""

459. Repeated Substring Pattern
Easy


Share
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

"""

# V0
# IDEA : # only have to go through till HALF of s's length, since it's not possbile to find the SubstringPattern if len(s[:x]) > size//2
class Solution(object):
    def repeatedSubstringPattern(self, s):
        _len_s = len(s)
        i = 0
        tmp = ""
        while i < _len_s:
            if i == 0:
                multiply = 0
            if i != 0:
                multiply = _len_s // i
            if multiply * tmp == s:
                return True
            if i > _len_s // 2:
                return False
            tmp += s[i]
            i += 1
        return False

# V0'
# IDEA : # only have to go through till HALF of s's length, since it's not possbile to find the SubstringPattern if len(s[:x]) > size//2
class Solution(object):
    def repeatedSubstringPattern(self, s):
        _len = len(s)
        if _len == 0:
            return True
        if _len == 1:
            return False
        tmp = ""
        for i in range(_len):
            tmp += s[i]

            if ( _len // len(tmp) ) * tmp == s:
                return True
            if len(tmp) >= _len // 2 and ( _len // len(tmp) ) * tmp != s:
                return False
        return False

# V0'
# IDEA : # only have to go through till HALF of s's length, since it's not possbile to find the SubstringPattern if len(s[:x]) > size//2
class Solution(object):
    def repeatedSubstringPattern(self, s):
        _len = len(s)
        if _len == 0:
            return True
        if _len == 1:
            return False
        tmp = ""
        for i in range(_len//2):
            tmp += s[i]
            if ( _len // len(tmp) ) * tmp == s:
                return True
            if len(tmp) >= _len // 2:
                return False
        return False

# V0''
class Solution(object):
    def repeatedSubstringPattern(self, str):
        size = len(str)
        # only have to go through till HALF of s's length, since it's not possbile to find the SubstringPattern if len(s[:x]) > size//2
        for x in range(1, size // 2 + 1):
            # if len(s) is not len(s[:x]) 's  multiple
            if size % x == 1:
                continue
            # if len(s) is  len(s[:x]) 's  multiple, check if SubstringPattern 
            if str[:x] * (size // x) == str:
                return True
        return False

# V0'
class Solution(object):
    def repeatedSubstringPattern(self, str):
        size = len(str)
        # only have to go through till half of s's length, since it's not possbile to find the SubstringPattern if len(s[:x]) > size//2
        for x in range(1, size // 2 + 1):
            # if len(s) is  len(s[:x]) 's  multiple, check if SubstringPattern 
            if str[:x] * (size // x) == str:
                return True
        return False

# V0''
class Solution(object):
    def repeatedSubstringPattern(self, str):
        size = len(str)
        cur_size = 0
        for i in range(1, size//2+1):
            cur_size += 1 
            sample = str[:i]
            if size % cur_size == 0 \
               and sample * (size//cur_size) == str:
                return True
        return False

# V1
# http://bookshadow.com/weblog/2016/11/13/leetcode-repeated-substring-pattern/
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        size = len(str)
        for x in range(1, size // 2 + 1):
            if size % x:
                continue
            if str[:x] * (size // x) == str:
                return True
        return False

### Test case:
s=Solution()
assert s.repeatedSubstringPattern("abab") == True
assert s.repeatedSubstringPattern("aba") == False
assert s.repeatedSubstringPattern("ababab") == True
assert s.repeatedSubstringPattern("") == False
assert s.repeatedSubstringPattern("a") == False
assert s.repeatedSubstringPattern("aaaaa") == True
assert s.repeatedSubstringPattern("aaabbb") == False
assert s.repeatedSubstringPattern("".join([ 'a' for _ in range(100)])) == True

# V1'
# https://blog.csdn.net/fuxuemingzhu/article/details/54564801
# IDEA : 
# go through the sting, if can find any sub-string 
# that is part of the origin string, return Ture.
# if not, return False. 
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_s = len(s)
        for i in range(1, len_s // 2 + 1): # (sub-string)* k = string. k = 2, 3, 4, ....n. so k start from 2 
            if len_s % i == 0:             # when len(sub-string)*k = len(string)
                sub_s = s[:i]              # get sub-string 
                if sub_s * (len_s // i) == s:
                    return True
        return False

# V2 
# Time:  O(n)
# Space: O(n)
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        def getPrefix(pattern):
            prefix = [-1] * len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j > -1 and pattern[j + 1] != pattern[i]:
                    j = prefix[j]
                if pattern[j + 1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        prefix = getPrefix(str)
        return prefix[-1] != -1 and \
               (prefix[-1] + 1) % (len(str) - prefix[-1] - 1) == 0

    def repeatedSubstringPattern2(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False
        ss = (str + str)[1:-1]
        return ss.find(str) != -1