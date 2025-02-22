import random_number_generator
random = random_number_generator.random_number_generator(1000)
#random_nums = random.random(53)

def run_simulation(n : int):
    """
    Run a simulation given problem
    """
    wait_times = []
    for i in range(0, n):
        wait_times.append(run_customer())
    statistics = calculateStatistics(wait_times)

#simulates a single caller interaction and returns the wait time until they respond
def run_customer() -> int:
     wait_time = 0
     return wait_time

def calculateStatistics(data : list[int]) -> dict[str : float]:
    statistics = {}
    data = data.sort()
    statistics['mean'] = sum(data) / len(data)
    statistics['stddev'] = 0.0
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

