#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(0,N):
            for j in range(0,N):
                if i==0 or i==N-1 or j==0 or j==N-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print("")
        # Code here


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
