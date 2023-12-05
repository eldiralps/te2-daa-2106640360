# referensi: https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/

# Python3 program to find maximum 
# achievable value with a knapsack 
# of weight W and multiple instances allowed. 

# Returns the maximum value 
# with knapsack of W capacity 
def unboundedKnapsackWithDP(W, n, val, wt): 

	# dp[i] is going to store maximum 
	# value with knapsack capacity i. 
	dp = [0 for i in range(W + 1)] 

	ans = 0

	# Fill dp[] using above recursive formula 
	for i in range(W + 1): 
		for j in range(n): 
			if (wt[j] <= i): 
				dp[i] = max(dp[i], dp[i - wt[j]] + val[j]) 

	return dp[W] 

if __name__ == '__main__':

	# Driver program 
	W = 100
	val = [10, 30, 20] 
	wt = [5, 10, 15] 
	n = len(val) 

	print("Maximum values of the sack: ",unboundedKnapsackWithDP(W, n, val, wt)) 

# This code is contributed by Anant Agarwal. 
