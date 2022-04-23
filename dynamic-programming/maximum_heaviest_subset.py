import heapq


def maxHeaviestSubArray(array):
    sum_of_elements = sum(array)
    sum_of_set_a = 0
    set_a = []
    length = len(array)
    negative_array = [-element for element in array]
    heapq.heapify(negative_array)  # o(n)
    for index in range(length):  # o(n)
        next_largest_element = - heapq.heappop(negative_array)  # o(log n)
        current_sum = sum_of_set_a + next_largest_element
        if current_sum > (sum_of_elements - current_sum):
            set_a.append(next_largest_element)
            break
        else:
            set_a.append(next_largest_element)
            sum_of_set_a = current_sum
    set_a.sort()  # o(nlogn)
    return set_a


# time complexity o(n) , space complexity o(nlog(n))
def execute():
    result = maxHeaviestSubArray([5, 5, 5, 5, 5])
    print(result)


if __name__ == '__main__':
    execute()
