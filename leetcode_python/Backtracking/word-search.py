# V0 

# V1
# https://blog.csdn.net/fuxuemingzhu/article/details/79386066
# IDEA : BACKTRACKING 
# DEMO : 
# In [39]: 'ACV'.swapcase()
# Out[39]: 'acv'
# In [41]: 'wfwwrgergewCEVER'.swapcase()
# Out[41]: 'WFWWRGERGEWcever'
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.exit(board, word, x, y, 0):
                    return True
        return False
    
    def exit(self, board, word, x, y, i):
        if i == len(word):
            return True
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return False
        if board[y][x] != word[i]:
            return False
        board[y][x] = board[y][x].swapcase() # to mark if the route already been passed (.swapcase(), e.g. A->a)
        isexit =  self.exit(board, word, x + 1, y, i + 1) or self.exit(board, word, x, y + 1, i + 1) or self.exit(board, word, x - 1, y, i + 1) or self.exit(board, word, x, y - 1, i + 1)
        board[y][x] = board[y][x].swapcase() # if already visited all possible route within the route collection, then roll back the maked route (.swapcase(), e.g. a->A), and run the other visit again 
        return isexit
# V1'
# https://www.cnblogs.com/zuoyuan/p/3769767.html
# IDEA : DFS 
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def dfs(x, y, word):
            if len(word)==0: return True
            #up
            if x>0 and board[x-1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x-1,y,word[1:]):
                    return True
                board[x][y]=tmp
            #down
            if x<len(board)-1 and board[x+1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x+1,y,word[1:]):
                    return True
                board[x][y]=tmp
            #left
            if y>0 and board[x][y-1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y-1,word[1:]):
                    return True
                board[x][y]=tmp
            #right
            if y<len(board[0])-1 and board[x][y+1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y+1,word[1:]):
                    return True
                board[x][y]=tmp
            return False
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if(dfs(i,j,word[1:])):
                        return True
        return False
           
# V2
# Time:  O(m * n * l)
# Space: O(l)
class Solution(object):
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existRecu(board, word, 0, i, j, visited):
                    return True

        return False

    def existRecu(self, board, word, cur, i, j, visited):
        if cur == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False

        visited[i][j] = True
        result = self.existRecu(board, word, cur + 1, i + 1, j, visited) or\
                 self.existRecu(board, word, cur + 1, i - 1, j, visited) or\
                 self.existRecu(board, word, cur + 1, i, j + 1, visited) or\
                 self.existRecu(board, word, cur + 1, i, j - 1, visited)
        visited[i][j] = False

        return result