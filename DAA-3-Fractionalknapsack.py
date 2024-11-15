# def fractional_knapsack():
#     weights=[10,20,30]
#     values=[60,100,120]
#     capacity=50
#     res=0
#     # Pair : [Weight,value]
#     for pair in sorted(zip(weights,values), key= lambda x: x[1]/x[0], reverse=True):
#         if capacity<=0: # Capacity completed - Bag fully filled 
#             break 
#         if pair[0]>capacity: # Current's weight with highest value/weight ratio Available Capacity
#             res+=int(capacity * (pair[1]/pair[0]))  # Completely fill the bag
#             capacity=0
#         elif pair[0]<=capacity: # Take the whole object
#             res+=pair[1]
#             capacity-=pair[0]
#     print(res)        

# if __name__=="__main__":
#     fractional_knapsack()
-----------------------------------------------------------------------------------------------------------------------
class ItemValue:
    def __init__(self , wt_ , val_ , ind_):
        self.wt = wt_
        self.val = val_
        self.ind = ind_
        self.cost = val_ // wt_

    def __lt__(self ,other):
        return self.cost < other.cost


def fractionalKnapSack(wt , val , capacity):

    ival = [ItemValue(wt[i] , val[i] , i) for i in range(len(wt))]
    ival.sort(reverse=True)
    totalvalue = 0
    for i in ival:
        curwt = i.wt
        curval = i.val
        if capacity-curwt >= 0:
            capacity-=curwt
            totalvalue += curval
        else:
            fraction = capacity / curwt
            totalvalue += curval * fraction 
            break
    return totalvalue

wt = [20, 10, 30]
val = [100, 60, 120]
capacity = 50
maxvalue = fractionalKnapSack(wt , val , capacity)
print("Maximaum value = " , maxvalue)

--------------------------------------------------------------------------------------------------------------------------
    

class Item:
    def __init__(self, weight,value):
        self.weight= weight
        self.value= value
        
    def __str__(self):
        return (f" weight : {self.weight}, value: {self.value}")
        
def fractionalKnapsack(w,arr):
    arr.sort(key=lambda x: x.value/x.weight, reverse=True)
    finalvalue= 0.0
    
    for item in arr:
        if w >= item.weight:
            finalvalue+=item.value
            w-=item.weight
        else:
            finalvalue+=item.value*(w/item.weight)
            break
    return finalvalue
    
if __name__ =="__main__":
    n=int(input("enter no of items : "))
    arr=[]
    for i in range(n):
        weight = int(input(f"enter weight for {i+1} - "))
        value = int(input(f"enter value for {i+1} -"))
        arr.append(Item(weight,value))
        
    for item in arr:
        print (item)
     
    w= int(input("enter the capacity for knapsack"))
    print("maximum value of knapsack", fractionalKnapsack(w, arr))           
