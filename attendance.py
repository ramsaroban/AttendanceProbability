#########
# Using DP approach
# Approach:
# 1. Total Number of Valid Attendance Sequences (Answer of 1):
#    -> Need find all possible attendance sequences where you are not absent for 4 or more consecutive days.
# 2. Number of Valid Attendance Sequences Ending with an Absence (Answer of 2):
#   -> We specifically look for sequences that end with 1, 2, or 3 consecutive absences on the Nth day, which means missing the graduation ceremony.
########

def attendance(N):
    # Initialize dp array
    dp = [[0] * 4 for _ in range(N + 1)]
    
    # Base cases
    dp[1][0] = 1
    dp[1][1] = 1
    dp[1][2] = 0
    dp[1][3] = 0
    
    for i in range(2, N + 1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
        dp[i][1] = dp[i-1][0]
        dp[i][2] = dp[i-1][1]
        dp[i][3] = dp[i-1][2]
    
    total_valid_sequences = dp[N][0] + dp[N][1] + dp[N][2] + dp[N][3]
    sequences_missing_graduation = dp[N][1] + dp[N][2] + dp[N][3]
    
    return f"{sequences_missing_graduation}/{total_valid_sequences}"

print(attendance(5))
print(attendance(10))

