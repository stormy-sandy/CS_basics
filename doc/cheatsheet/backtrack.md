# Bracktrack 

> Brute force via  `decision tree process`

- [fuck algorithm : backtrack]( https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3%E4%BF%AE%E8%AE%A2%E7%89%88.md)

- Backtrack (brute force) -> DP (dynamic programming)
- optimization:
    - remove duplicated sub cases
    - have a cache (e.g. hash table) list finished cases (not re-compute them)
    - "cut the sub-tree" via conditions such as `contains`, `start`

## 0) Concept  

### 0-1) Types

- 3 things to consider : 
 - `Route` : The choices have made
 - `Choice list` : The choices we can select currently
 - `End condition` : bottom of decision tree, meet this point then can't do any other choise 

- Algorithm
    - dfs
    - recursive

- Data structure
    - dict
    - set
    - array

- Problems types
    - `Combinations (組成)` 
        - LC 77
        - backtrack. via `start` remove already used numbers and return all cases
        - deal with `idx` !!! (start idx)
        - start + for loop + pop(-1) + help func
        ```python
        # ...
        cur = []
        res = []
        def help(idx, cur):
            if len(cur) == k:
                res.append(cur)
                return
            for i in range(idx, n+1):
                cur.append(i)
                help(idx+1, cur)
                cur.pop(-1)
        # ...
        ```
    - `Permutations (排列組合)`
        - LC 46
        - backtrack. via `contains` remove already used numbers and return all cases
        - contains (visited) (or not in `cur`) + for loop + pop(-1) + help func
        ```python
        # ...
        res = []
        cur = []
        def help(cur):
            if len(cur) == len(s):
                res.append(cur[:])
                return
            if len(cur) > len(s):
                return
            for i in nums:
                # NOTE this !!!
                if i not in cur:
                    cur.append(i)
                    help(cur)
                    cur.pop(-1)
        # ...
        ```
    - `Subsets`
        - LC 78, 140, 17
        - backtrack. find minumum case. transform the problem to `tree-problem`. via `start` remove already used numbers and return all cases
        - (for loop call help func) + for loop + pop(-1)
        - "全排列"
        ```python
        # ...
        cur = []
        res = []
        def help(cur):
            _cur = "".join(cur[:])
            if _cur == s:
                res.append(cur[:])
                return
            if len(_cur) > len(s):
                cur = []
                return
            # NOTE !!! since we need get ALL sub group (全排列), so WE DON'T NEED deal with idx here
            for i in range(len(wordDict)):
                cur.append(wordDict[i])
                help(cur)
                cur.pop(-1)
        # ...
        ```
    - Parentheses (括弧)
        - LC 20, LC 22


### 0-2) Pattern

```python
# python pseudo code 1
for choice in choice_list:
    # do choice
    routes.add(choice)
    backtrack(routes, choice_list)
    # undo choice
    routes.remove(choice)
```

```python
# python pseudo code 2
result = []
def backtrack(route, choice_list):
    if end_condition:
        result.add(route)
        return
    
    for choice in choice_list:
        ### core of backtrack
        do_choice   ### this one is necessary
        backtrack(route, choice_list)
        undo_choice ### this one is necessary
```

## 1) General form

### 1-1) Basic OP

### 1-2) Trick
```python
# LC 131. Palindrome Partitioning

# ...
def help(s, res, path):
    if not s:
        res.append(path)
    for i in range(1, len(s)):
        if s[:i] == s[:i][::-1]:
            """
            NOTE below !!!
                -> we call help recursively with s[i:] subset
                -> we append [s[:i]] to tmp cache (path) 
            """
            help(s[i:], res, path + [s[:i]])
# ...
```

## 2) LC Example

### 2-1) Letter Combinations of a Phone Number 
```python
# 017   Letter Combinations of a Phone Number
# V0
# IDEA : backtracking
class Solution(object):
    def letterCombinations(self, digits):
        # help func
        def help(idx, cur):
            if len(cur) == len(digits):
                tmp = "".join(cur[:])
                res.append(tmp)
                cur = []
                return
            if len(cur) > len(digits):
                cur = []
                return
            for a in d[digits[idx]]:
                cur.append(a)
                help(idx+1, cur)
                cur.pop(-1)  # NOTE this !!! : we pop last element
        # edge case
        if not digits:
            return []
        res = []
        cur = []
        idx = 0
        d =  {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        help(idx, cur)
        return res

# V0'
# IDEA : dfs + backtracking
class Solution(object):
    def letterCombinations(self, digits):

        def dfs(idx, tmp):

            """
            NOTE : if idx == len(digits)
               -> if tmp is not null, then we append tmp to our result (res)
               -> and we out of the loop
            """
            if idx == len(digits):
                if tmp != "":
                    res.append(tmp)
                return

            ### NOTE : we loop alphabets in d map per number rather than loop over number !!!
            for alpha in d[digits[idx]]:
                """
                NOTE !!!!
                idex+1 : for loop to next number
                tmp+j : for collect cur update
                """
                print ("digits = " + str(digits), " tmp = " + str(tmp) + " alpha = " + str(alpha))
                dfs(idx+1, tmp + alpha)

        d = {'2' : "abc", '3' : "def", '4' : "ghi", '5' : "jkl", '6' : "mno", '7' : "pqrs", '8' : "tuv", '9' : "wxyz"}
        res = []
        dfs(0,"")
        return 

# V1 
# idea : for loop
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        d = {'2' : "abc", '3' : "def", '4' : "ghi", '5' : "jkl", '6' : "mno", '7' : "pqrs", '8' : "tuv", '9' : "wxyz"}
        res = ['']
        for e in digits:
            res = [w + c for c in d[e] for w in res]
        return res
```

### 2-2) combination-sum
```python
# LC 039, LC 040 combination-sum
# V0
# IDEA : DFS + BACKTRACK
class Solution(object):
    def combinationSum(self, candidates, target):

        def dfs(tmp):
            if sum(tmp) == target:
                tmp.sort()
                if tmp not in res:
                    res.append(tmp)
                return
            if sum(tmp) > target:
                return
            for c in candidates:
                dfs(tmp + [c])

        res = []
        tmp = []
        dfs(tmp)
        return res
``` 

### 2-3) Word Search
```python
# LC 079 Word Search

# V0
# IDEA : DFS + backtracking
class Solution(object):
 
    def exist(self, board, word):
        ### NOTE : construct the visited matrix
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]

        ### NOTE : we visit every element in board and trigger the dfs
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j, visited):
                    return True

        return False

    def dfs(self, board, word, cur, i, j, visited):
        # if "not false" till cur == len(word), means we already found the wprd in board
        if cur == len(word):
            return True

        ### NOTE this condition
        # 1) if idx out of range
        # 2) if already visited
        # 3) if board[i][j] != word[cur] -> not possible to be as same as word
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False

        # mark as visited
        visited[i][j] = True
        ### NOTE THIS TRICK (run the existRecu on 4 directions on the same time)
        result = self.dfs(board, word, cur + 1, i + 1, j, visited) or\
                 self.dfs(board, word, cur + 1, i - 1, j, visited) or\
                 self.dfs(board, word, cur + 1, i, j + 1, visited) or\
                 self.dfs(board, word, cur + 1, i, j - 1, visited)
        # mark as non-visited
        visited[i][j] = False

        return result
```

### 2-4) Subsets
```python
# LC 078 Subsets
# V0
# IDEA : Backtracking
class Solution:
    def subsets(self, nums):
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

# V0'
# brack tracking
class Solution(object):
    def subsets(self, nums):
        def help(start, tmp, res):
            tmp.sort()
            if tmp not in res:
                res.append(tmp)
            for i in range(start, len(nums)):
                if nums[i] not in tmp:
                    help(start+1, tmp + [nums[i]], res)
        res = []
        start = 0
        tmp = []
        if len(nums) == 1:
            res = [[]]
            res.append(nums)
            return res
        help(start, tmp, res)
        return res

# V0''
# IDEA : DFS 
class Solution(object):
    def subsets(self, nums):
        def dfs(layer, start, tmp):
            if tmp not in res:
                res.append(tmp)
            if layer == len(nums):
                return
            ### NOTE : we have if condition first, then for loop
            for i in range(start, len(nums)):
                ### NOTE below can make loop start `start idx` updated each time
                dfs(layer+1, i+1, tmp + [nums[i]])
        nums.sort()
        res = []
        dfs(0, 0, [])
        return res
```
```c++
// c++
// backtrack
// (algorithm book (labu) p.303)

// save all subset
vector<vector<int>> res;

/* main func */
vector<vector<int>> subsets(vector<int> & nums){
    // record visited routes
    vector<int> tracks;
    backtrack(nums, 0, track);
    return res;
}

/* use backtrack pattern */
void backtrack(vector<int> & nums, int start, vector<int> & track){
    // pre-order tranverse
    res.push_back(track);
    // start from `start`, avoid duplivated subset
    for (int i = start; i < nums.size(); i++){
        // make choice
        track.push_back(nums[i]);
        // iteration backtrack
        backtrack(nums, i+1, track);
        // undo choice
        track.pop_back();
    }
}
```

### 2-4') Subsets II
```python
# LC 90 Subsets II
# V0
# IDEA : BACKTRACKING + LC 078 Subsets
from collections import Counter
class Solution(object):
    def subsetsWithDup(self, nums):
        def help(start, tmp, _cnt):
            tmp.sort()
            if tmp not in res:
                res.append(tmp)
            if start >= len(nums):
                return
            for i in range(start, len(nums)):
                if _cnt[nums[i]]  > 0:
                    _cnt[nums[i]] -= 1
                    help(start+1, tmp + [nums[i]], _cnt)
                    """
                    NOTE : here we "undo" the "_cnt[nums[i]] -= 1" op,
                          -> so next recursive can still have the "capacity" of such element
                    """
                    _cnt[nums[i]] += 1

        # edge case
        if not nums:
            return []

        # edge case
        if len(nums) == 1:
            res = [[]]
            res.append([nums[0]])
            return res

        res = [[]]
        _cnt = Counter(nums)
        help(0, [], _cnt)
        print ("res = " + str(res))
        return res

# V0
# IDEA : BRUTE FORCE
class Solution:
    def subsetsWithDup(self, nums):
        # small trick (init with a null array)
        ans=[[]]
        for i in nums:
            for l in list(ans):
                # sorted here, since we want to the "non-duplicated" power set
                temp=sorted(l+[i])
                # avoid duplicated
                if temp not in ans:
                    ans.append(temp) 
        return ans

```

### 2-5) Combinations
```python
# LC 77. Combinations
# V0
# BACKTRACK
class Solution(object):
    def combine(self, n, k): 
        def dfs(current, start):
            if(len(current) == k):
                """
                Both of below approach are OK
                
                list(current) : transform current reference to list
                current[:] : shallow copy
                """
                result.append(list(current))
                return
            
            for i in range(start, n + 1):
                current.append(i)
                dfs(current, i + 1)
                current.pop()
            
        result = []
        dfs([], 1)
        return result

# V0'
# IDEA : BACKTRACK
class Solution:
    def combine(self, n, k):
        res=[]
        def go(i,ma,ans):
            if ma==k:
                res.append(list(ans))
                return
            if i>n:
                return
            ans.append(i)
            go(i+1,ma+1,ans)
            ans.pop()
            go(i+1,ma,ans)
        go(1,0,[])
        return res
```
```c++
// c++
// backtrack
// (algorithm book (labu) p.305)

// record all combinations
vector<vector<int>> res;

/* main func */
vector<vector<int>> combine(int n, int k){
    if (k <= 0 || n <= 0) return res;
    vector<int> track;
    backtrack(n, k, 1, track);
    return res;
}

/* use backtrack pattern */
void backtrack(int n, int k, int start, vector<int> & track){
    // not update res till visit leaf node
    if (k == track.size()){
        res.push_back(track);
        return;
    }

    // increase from i
    for (int i = start; i <= n; i ++){
        // do choice
        track.push_back(i);
        // backtrack
        backtrack(n, k, i+1, track);
        // undo choice
        track.pop_back();
    }
}
```

### 2-6) Permutations
```python
# LC 46. Permutations
# V0
# IDEA : BACKTRACK, 
# similar idea as LC 77 -> difference : contains VS start
class Solution(object):
    def permute(self, nums):
        def help(cur):
            if len(cur) == n_len:
                if cur not in res:
                    res.append(list(cur))
                    return
            if len(cur) > n_len:
                return
            for i in nums:
                #print ("i = " + str(i) + " cur = " + str(cur))
                if i not in cur:
                    cur.append(i)
                    help(cur)
                    cur.pop(-1)
        # edge case
        if not nums:
            return [[]]
        n_len = len(nums)
        res = []
        help([])
        #print ("res = " + str(res))
        return res

# V0 
class Solution(object):
    def permute(self, nums):
        visited = [0] * len(nums)
        res = []
        path = []
        self.dfs(path)
        return res
        
    def dfs(self, path):
        if len(path) == len(nums):
            res.append(path)
        else:
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = 1
                    dfs(path + [nums[i]])
                    visited[i] = 0    ### to check if "visited[i] = 0" is necessary
```
```java
// LC 46. Permutations
// java
// (algorithm book (labu) p.307)
List<List<Integer>> res = new LinkedList<>{};

/* main func, insert a set with non-duplicated numbers, return its Permutations */
List<List<Integer>> permute(int nums[]){
    // record "route"
    LinkedList<Integer> track = new LinkedList<>{};
    backtrack(nums, track);
    return res;

void backtrack(int[] nums, LinkedList<Integer> track){
    // arrive leaf node
    if (track.size() == nums.length){
        res.add(new LinkedList(track));
        return ;
    }

    for (int i = 0; i < nums.length; i++){
        // remove "illegal" choices
        if (track.contains(nums[i])){
            continue;
        }
        // make choice
        track.add(nums[i]);
        // go to next decision tree
        backtrack(nums, track);
        // undo choice
        backtrack.removeLast();
     }
  }
}
```

### 2-7) Generate Parentheses
```python
# python
# LC 022 Generate Parentheses
# V0
# IDEA : bracktrack + Valid Parentheses (LC 020)
class Solution(object):
    def generateParenthesis(self, n):
        # help func for backtracking
        def help(tmp, res, n):
            if len(tmp) == n * 2 and check(tmp):
                res.append(tmp)
                return
            if len(tmp) == n * 2:
                return
            for l in _list:
                print ("l = " + str(l))
                help(tmp + l, res, n)

        """
        LC 020 Valid Parentheses
        """
        def check(s):
            lookup = {"(":")", "[":"]", "{":"}"}
            q = []
            for i in s:
                if i not in lookup and len(q) == 0:
                    return False
                elif i in lookup:
                    q.append(i)
                else:
                    tmp = q.pop()
                    if lookup[tmp] != i:
                        return False
            return True if len(q) == 0 else False

        _list = ['(', ')']
        if n == 1:
            return ["()"]
        res = []
        help("", res, n)
        return res

# V0'
# https://blog.csdn.net/fuxuemingzhu/article/details/79362373
# IDEA: BACKTRACKING + DFS 
# NOTE : KEEP DFS WHEN MEAT 2 CONDTIONS:
#  1) len(path) < n 
#  2) # of "("  > # of ")" (means it's still possible to form a "paratheses" as expected)
class Solution(object):
    def generateParenthesis(self, n):
        res = []
        self.dfs(res, n, n, '')
        return res
        
    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')
```
```java
// java
// LC 022 Generate Parentheses
// (algorithm book (labu) p.316)

/* main func */
vector<String> generateParentheses(int n){
    if (n == 0) return {};
    // record all legal collections
    vector<string> res;
    // backtrack the routes (in process)
    string track;
    // init : available left Parentheses and right Parentheses counts as n
    backtrack(n, n, track, res);
    return res;
}

/* remain left Parentheses count : left ;.. remain right Parentheses : right */
void backtrack(int left, int right, string& track, vector<string> & res){
    // if count < 0 : illegal
    if (left < 0 || right < 0) return;
    // if remain  left Parentheses count >  right Parentheses count : illegal
    if (right < left) return;
    // if all Parentheses are used : legal, we got one OK solution
    if (left == 0 && right == 0){
        res.push_back(track);
        return;
    }

    // add one more left Parentheses
    track.push_back('(') // do choice
    backtrack(left - 1, right, track, res);
    track.push_back(); // undo choice

    // add one more right Parentheses
    track.push_back(')') // do choice
    backtrack(left, right - 1, track, res);
    track.push_back(); // undo choice
}
```
### 2-8) Palindrome Partitioning
```python
# LC 131 Palindrome Partitioning
# V0
# IDEA : BACKTRCK, similar as LC 046 permutations
class Solution(object):
    def partition(self, s):
        def help(s, res, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    help(s[i:], res, path + [s[:i]])
        # edge case
        if not s:
            return
        res = []
        path = []
        help(s, res, path)
        return res

# V0'
# IDEA : BACKTRCK, similar as LC 046 permutations
class Solution(object):
    def partition(self, s):
        res = []
        self.helper(s, res, [])
        return res
        
    def helper(self, s, res, path):
        if not s:
            res.append(path)
            return
        # beware of the start and the end index
        for i in range(1, len(s) + 1): 
            if self.isPalindrome(s[:i]):
                """
                ### backtrcking 
                if s[:i] is palindrome, then check if there is palindrome in s[i:] as well
                e.g.  
                    a a b b a 
                  => 
                    if 'aa' (<-) is palindrome, then check a b b a (->)
                """
                self.helper(s[i:], res, path + [s[:i]])

    def isPalindrome(self, x):
        return x == x[::-1]
```

### 2-9) Restore IP Addresses
```python
# 093 Restore IP Addresses
# V0 
# IDEA : DFS
class Solution(object):
    def restoreIpAddresses(self, s):
        # if not valid input form (ip address length should < 12)
        if len(s) > 12:
            return []
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        # if not remaining elments (not s) and path is in "xxx.xxx.xxx.xxx" form
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in [1,2,3]:
            # avoid "out of index" error
            if i > len(s):
                continue
            number = int(s[:i])
            # str(number) == s[:i] for checking if digit is not starting from "0"
            # e.g. 030 is not accepted form, while 30 is OK
            if str(number) == s[:i] and number <= 255:
                self.dfs(s[i:], path + [s[:i]], res)
```

### 2-9) Word Break
```python
# LC 139 Word Break
# V0
# IDEA : BFS
class Solution:
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return
        q = collections.deque()
        q.append(0)
        visited = [None]*len(s)
        while q:
            i = q.popleft()
            if not visited[i]:
                for j in range(i+1,len(s)+1):                 
                    if s[i:j] in wordDict:                    
                        if j == len(s):
                            return True  
                        q.append(j)
                visited[i]=True
```

### 2-10) Word Break II
```python
# LC 140 Word Break II
# NOTE : there is also dfs, dp approaches
# V0
# IDEA : BACKTRCK, LC 078 Subsets
class Solution(object):
    def wordBreak(self, s, wordDict):
        def help(cur):
            """
            NOTE this !!! : 
                -> shallow copy cur[:]
            """
            if "".join(cur[:]) == s:
                res.append(" ".join(cur[:]))
                return
            if len("".join(cur[:])) > len(s):
                return
            for i in range(len(wordDict)):
                cur.append(wordDict[i])
                help(cur)
                # NOTE this
                cur.pop()

        # edge case
        if not wordDict:
            return []
        res = []
        cur = []
        cnt = 0
        help(cur)
        print ("res = " + str(res))
        return res

# V1
# IDEA : RECURSION
# https://leetcode.com/problems/word-break-ii/discuss/1426014/Python-interview-friendly-simple-recursion
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def recur(s, path):
            if not s:
                out.append(' '.join(path))
                return
            for i in range(1,len(s)+1):
                w,new_s = s[:i], s[i:]
                if w in wordDict:
                    recur(new_s, path + [w])
        wordDict, out = set(wordDict), []
        recur(s,[])
        return out

# V1'
# IDEA : BACKTRCK
# https://leetcode.com/problems/word-break-ii/discuss/44404/Python-backtracking
class Solution:
    def wordBreak(self, s, dic):
        if not dic:
            return []
        n = max(len(d) for d in dic)
        stack, parents = [0], collections.defaultdict(set)
        while stack:
            parent = stack.pop()
            for child in range(parent+1, parent+n+1):
                if s[parent:child] in dic:
                    if child not in parents:
                        stack.append(child)
                    parents[child].add(parent)
        stack, res = [[len(s)]], []
        while stack:
            r = stack.pop()
            if r[0] == 0:
                r = [s[i:j] for i, j in zip(r[:-1], r[1:])]
                res.append(' '.join(r))
            for parent in parents[r[0]]:
                stack.append([parent]+r)
        return res
```