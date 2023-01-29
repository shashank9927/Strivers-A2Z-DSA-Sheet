#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        idx=65
        for i in range(0,N):
            for j in range(0,N-i-1):
                print("",end=" ")
            breakpoint=(2*i+1)//2
            c=0
            for j in range(0,2*i+1):
                if j< breakpoint:
                    print(chr(idx+c),end="")
                    c+=1
                else:
                    print(chr(idx+c),end="")
                    c-=1

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
