# Geek is organising a bike race with N bikers. The initial speed of the ith biker is denoted by Hi Km/hr and the acceleration of ith biker as Ai Km/Hr2. A biker whose speed is 'L' or more, is considered be a fast biker. The total speed on the track for every hour is calculated by adding the speed of each fast biker in that hour. When the total speed on the track is 'M' kilometers per hour or more, the safety alarm turns on. 
# Find the minimum number of hours after which the safety alarm will start.

# Your Task:
# You do not need to read input or print anything. Your task is to complete the function buzzTime() which takes N, M, L and array H and array A as input parameters and returns the time when alarm buzzes.


# Expected Time Complexity: O(N*log(max(L,M)))
# Expected Auxiliary Space: O(1)


# Constraints:
# 1 ≤ N ≤ 105
# 1 ≤ L, M ≤ 1010
# 1 ≤ Hi, Ai ≤ 109 



def canBuzz(time, L, M, H, A):
    total_speed = 0
    for i in range(len(H)):
        speed = H[i] + A[i] * time
        if speed >= L:
            total_speed += speed
        if total_speed >= M:
            return True
    return False

def buzzTime(N, M, L, H, A):
    left = 0
    right = 10**18  # Some large enough upper bound
    
    while left < right:
        mid = left + (right - left) // 2
        if canBuzz(mid, L, M, H, A):
            right = mid
        else:
            left = mid + 1
    
    return left

# Example usage:

# Test case : 1  Output => 3
# N = 3 
# M = 400
# L = 120
# H = [20, 50, 20]
# A = [20, 70, 90]

# Test Case : 2  Output => 3
N , M , L = 2,60,120
H = [50, 30]
A = [20, 40]

print(buzzTime(N, M, L, H, A))
