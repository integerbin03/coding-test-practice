class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        visited = []
        for _ in range(len(matrix)):
            s = []
            for _ in range(len(matrix[0])):
                s.append(False)
            visited.append(s)
    
        row_len = len(matrix[0])
        col_len = len(matrix)
        offset = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        i = 0
        j = 0
        answer = []
        offidx = 0
        while True:
            xoff, yoff = offset[offidx]
            if not visited[i][j]:
                visited[i][j] = True
                answer.append(matrix[i][j])
            if i + yoff < col_len and j + xoff < row_len and not visited[i + yoff][j + xoff]:
                i = i + yoff
                j = j + xoff
            else:
                offidx += 1
                if offidx > 3:
                    offidx = 0
            if len(answer) == row_len * col_len:
                break
        return answer
        
            
print(spiralOrder(0, [[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
print(spiralOrder(0, [[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])