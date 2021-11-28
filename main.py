def rot(num):

    nums = str(num)

    for i in nums:
        if i == '6':
            a = nums.replace(i, '9',1)

    return a
