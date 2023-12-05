import sys
import unbounded_knapsack_dp
import unbounded_knapsack_bnb
import time
import psutil
def callUnboundedKnapsackWithDP(W, weight,values,*args):
    sys.setrecursionlimit(100000000)
    
    n = len(weight)

    result = unbounded_knapsack_dp.unboundedKnapsackWithDP(W,n, values, weight, *args)
    return result


def callUnboundedKnapsackWithBNB(W, weight, values):
    sys.setrecursionlimit(100000000)

    items =  list(zip(weight, values))
    eliminated = unbounded_knapsack_bnb.eliminate_dominated_items(items)
    N, W_prime, m, i, z_hat, V, x_hat, x, M, U = unbounded_knapsack_bnb.initialization(eliminated, W)
    result = unbounded_knapsack_bnb.develop(N, W_prime, m,i,z_hat,V,x_hat,x,M,U)

    return result

def evaluateDP(W, weight, values):
    start_time = time.time()
    memory = psutil.Process().memory_info().rss


    max_value = callUnboundedKnapsackWithDP(W, weight, values)

    end_time = time.time()
    psutil.Process().memory_info().rss

    print("Maximum values of the sack: ", max_value)
    print("-------------------------------")
    print(f"Time taken (DP): {((end_time-start_time)*1000):.10f} ms")
    print(f"Memory used (DP): {memory} Bytes")
    print("-------------------------------")
    print()

def evaluateBNB(W, weight, values):
    start_time = time.time()
    memory = psutil.Process().memory_info().rss


    max_value = callUnboundedKnapsackWithBNB(W, weight, values)

    end_time = time.time()
    psutil.Process().memory_info().rss

    print("Maximum values of the sack: ", max_value)
    print("-------------------------------")
    print(f"Time taken (BnB): {((end_time-start_time)*1000):.10f} ms")
    print(f"Memory used (BnB): {memory} Bytes")
    print("-------------------------------")
    print()

def readDatasets(filename):
    with open(filename, 'r') as file:
        integer_list = [int(line.strip()) for line in file]
    return integer_list


if __name__ == '__main__':
    list_n = [100, 1000, 10000]
    for i in range(len(list_n)):
        W = readDatasets("W_"+str(list_n[i])+".txt")[0]
        weight = readDatasets(str(list_n[i])+"_weights.txt")
        values = readDatasets(str(list_n[i])+"_values.txt")
        print("Jumlah dataset: ", list_n[i])
        print("Weight:", W)
        print("Hasil evaluasi BnB")
        evaluateBNB(W, weight, values)
        print("Hasil evaluasi DP")
        evaluateDP(W, weight, values)
        print("-------------------------------")