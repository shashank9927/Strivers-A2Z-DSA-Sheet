#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(0,N):
            for j in range(0,i+1):
                print(chr(65+i),end="")
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
