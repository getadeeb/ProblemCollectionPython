def countDecreasingRatings(ratings):
    ratings_length = len(ratings)
    result_count = 0
    for row in range(ratings_length):
        current_element = ratings[row]
        r = 0
        for col in range(ratings_length):
            if col >= row:
                if current_element - r == ratings[col]:
                    result_count = result_count + 1
                r = r + 1
    return result_count


# time complexity o(n) , space complexity o(nlog(n))
def execute():
    result = countDecreasingRatings([4, 3, 5, 4, 3])
    print(result)


if __name__ == '__main__':
    execute()
