import random_number_generator
import math
random = random_number_generator.random_number_generator(1000)
#random_nums = random.random(53)

def run_simulation(n : int):
    """
    Run a simulation given problem
    """
    wait_times = []
    for i in range(0, n):
        wait_times.append(run_customer())
        #print(wait_times[i])
    statistics = calculateStatistics(wait_times)
    print(statistics)

#simulates a single caller interaction and returns the wait time until they respond
def run_customer(iteration=0) -> float:
     wait_time = 0
     if(iteration > 4):
         return wait_time
     wait_time += 6 #picking up her phone and dialing a number
     first_random = random.next()
     #using line
     if(first_random <= 0.2):
         wait_time += 3
         return wait_time + run_customer(iteration + 1) + 1
     #wait for 5 rings
     elif (first_random <= 0.5):
         wait_time += 25
         return wait_time + run_customer(iteration + 1) + 1
     #customer is available
     else:
         random_variable = exponential_random(random.next(), 12)
         if(random_variable <= 25):
             return wait_time + random_variable +  1
         else:
             return 25 + run_customer(iteration + 1) + 1
 
def exponential_random(x : float, lamda : float) -> int:
    x = - (1/lamda) * math.log(1 - x)
    return x

def calculateStatistics(data : list[float]) -> dict[str : float]:
    statistics = {}
    data.sort()
    statistics['mean'] = sum(data) / len(data)
    statistics['median'] = data[len(data) // 2]
    statistics['first_quartile'] = data[len(data) // 4]
    statistics['third_quartile'] = data[len(data) * (3 // 4)]
    statistics['W <= 15'] = calc_prob_under(data, 15)
    statistics['W <= 20'] = calc_prob_under(data, 20)
    statistics['W <= 30'] = calc_prob_under(data, 30)
    statistics['W > 40'] = 1 - calc_prob_under(data, 40)
    w_5 = 0.0
    w_6 = 0.0
    w_7 = 0.0
    statistics['W > w_5'] = 1 - calc_prob_under(data, w_5)
    statistics['W > w_6'] = 1 - calc_prob_under(data, w_6)
    statistics['W > w_7'] = 1 - calc_prob_under(data, w_7)
    return statistics
    
def calc_prob_under(data : list[int], threshold : int) -> float:
    for i in range(0, len(data)):
        if data[i] > threshold:
            return i / len(data)
    return 1.0
            

run_simulation(1000)

