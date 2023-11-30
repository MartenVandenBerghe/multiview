# Recursively
def solve(N):
    # Base case
    if N <=0 :
         return 0
         
    # Recursion
    n1 = solve(N-1) + 1
    n3 = solve(N-3) + 1
    n5 = solve(N-5) + 1
    return n1 + n3 + n5
    
    
N = 7
print(N, solve(N))

