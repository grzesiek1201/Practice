def grow(arr):
    x = 1
    for num in arr:
        x *= num
    return x


"""Description:
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24"""
