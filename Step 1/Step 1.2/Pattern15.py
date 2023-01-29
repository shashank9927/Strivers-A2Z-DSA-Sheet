#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N,0,-1):
            for j in range(0,i):
                print(chr(65+j),end="")
            print("")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends
