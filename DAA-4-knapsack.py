def solve_knapsack():
    #val = [100,60,120]
#wt = [20,10,30]
#w = 50
    # val=[50,100,150,200] #value array
    # wt=[8,16,32,40] # Weight array
    # W=64
    val=[100,60,120] #value array
    wt=[20,10,30] # Weight array
    W=50
    
    n=len(val) - 1
    def knapsack(W,n): # (Remaining Weight, Number of items checked)
        #base case
        if n<0 or W<=0:
            return 0
        
        #Higher weight than available
        if wt[n]>W:
            return knapsack(W, n-1)
        
        else:
            return max(val[n] + knapsack(W-wt[n],n-1),knapsack(W,n-1))
            # max(including , not including)
    print(knapsack(W,n))

if __name__=="__main__":
    solve_knapsack()