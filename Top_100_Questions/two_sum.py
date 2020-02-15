# Two Sum

# Given an array of integers, return indices of the two numbers such that 
# they add up to a specific target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15] and target = 9, should return [0, 1]
# because nums[0] + nums[1] = 2 + 7 = 9.

# Evolution of the solution in terms of improving time complexity...


# SOLUTION: BRUTE FORCE

# Start with the first index value of the array and iterate through
# every other value in the array to see if the sum is equal to the 
# target.

# Example:
# First iteration-
# Start with 2 and iterate through 7, 9 and 15.

# Second iteration-
# Start with 7 and iterate through 9 and 15.

# Third iteration-
# Start with 9 and iterate through 15.


# Time complexity: O(n^2)
# 2 for loops (nested for loop)

def two_sum_brute(nums, target):

    for i in range(len(nums)):

        for j in range(i+1, len(nums)):

            # Add the two values together.
            sum = nums[i] + nums[j]

            # If the sum of the two values is equal to the target, 
            # return the index pair.
            if sum == target:
                return [i, j]


# SOLUTION: USING HASH TABLE

# Store complements in a hash map.
# Create a map of a complement and the index position where it was found.

# Example: 
# First iteration-
# Start with 2.
# The hash map will contain {24 : 0} after the first iteration.
# complement = target - nums[i] = 26 - 2 = 24
# 0 represents the index position 2 is in in the array.

# Second iteration-
# Start with 7.
# The hash map will contain {24 : 0, 19 : 1} after the second iteration.
# complement = 26 - 7 = 19


# Time complexity: O(n)
# 1 for loop

def two_sum_hash(nums, target):

    # Check that the length of nums is greater than 1.
    if len(nums) <= 1:
        return f"There are not enough values to perform this function."

    
    # Create a hash table.
    hash_table = {}

    # Traverse through nums...
    for i in range(0, len(nums)):
        # Use the complement as the key within the hash table and
        # the index as the value.
        complement = target - nums[i]
        
        if nums[i] in hash_table:
            # Returns the index of the complement in the hash table
            # and the current index.            
            return [hash_table[nums[i]], i]
        else:
            # Insert the complement into the hash table.
            
            # Set the value (representative of the index)
            # as the current index.
            hash_table[complement] = i


# Walk through...
# a = [2, 4, 6]
# target = 10

# h_m = {}

# index position in array
# index = 0

# 8 = target - a[i] = 10 - 2
# 2 = a[0]
# h_m[8] = 2

# index = 1
# 6 = target - a[i] = 10 - 4
# 4 = a[1]
# h_m[6] = 4



# Run as test

nums = [1, 2, 3, 4, 5]

target = 9

print("Brute force solution:", two_sum_brute(nums, target))

print("Using hash table solution:", two_sum_hash(nums, target))


# Passing three parameters...

# def hash_solution(weights, length, limit):
#     # Check that the length of weights is greater than 1.
#     if length <= 1:
#         return f"We don't have enough values to perform this function."
    
#     # Create a hash table.
#     hash_table = {}

#     # Traverse through weights...
#     for i in range(0, length):
#         # Use the complement as the key within the hash table and
#         # the index as the value.
#         complement = limit - weights[i]
#         # if complement in hash_table:
#         if weights[i] in hash_table:
#             # Returns the index of the complement in the hash table
#             # and the current index.
#             # return (hash_table[complement], index)
#             return (hash_table[weights[i]], i)
#         else:
#             # Insert the complement into the hash table.
#             # hash_table.insert(complement, i)
#             # Set the value (representative of the index)
#             # as the current index.
#             hash_table[complement] = i


# weights1 = [1, 2, 3, 4, 5]
# length1 = 5
# limit1 = 9

# print(hash_solution(weights1, length1, limit1))