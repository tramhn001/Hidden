def hidden(matrix, n):
    # Your implementation here!
    # Flaten the matrix into new list
    # Using list comprehension
    # new_list = [letter for rows in matrix for letter in rows]
    # # new_list = []
    # # for rows in matrix:
    # #     for letter in rows:
    # #         new_list.append(letter)
     
    # # Iterate to add the nth element from the new list to the outcome, return outcome
    # result = ""
    # for i in range(len(new_list)):
    #     if i % n == 0:
    #         result += new_list[i]
    # return result 

    result = ""
    count = 0

    for rows in matrix:
        for letter in rows:
            if count % n == 0:
                result += letter
            count += 1
    return result

matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n',),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
assert hidden(matrix_1, 2) == 'ur doing great'
assert hidden(matrix_1, 3) == 'uedbnqgya'
assert hidden(matrix_1, 525600) == 'u'
assert hidden(matrix_1, 1) == 'uere edzobivnwgq 5gwryeuaut'

matrix_2 = (
    ('💜',),
)
assert hidden(matrix_2, 17) == '💜'
assert hidden(matrix_2, 1) == '💜'

print("All tests passed! Discuss time and space complexity if time remains!")

