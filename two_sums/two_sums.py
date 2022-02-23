'''
Brute force Solution
Runtime: 5105 ms
Memory Usage: 14.7 MB
Algorithm:
The brute force approach is simple. 
Loop through each element x and find if there is another value that equals to (target−x).
Complexity Analysis
    Time complexity:O(n^2).
    For each element, we try to find its complement by looping through the rest of the array which takes O(n) time.
    Therefore, the time complexity is O(n^2).

    Space complexity: O(1). 
    The space required does not depend on the size of the input array, so only constant space is used.
'''


def twoSum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]


'''
Two-pass Hash Table Solution
Runtime: 106 ms
Memory Usage: 15.4 MB
Algorithm:
A simple implementation uses two iterations. 
In the first iteration, we add each element's value as a key and its index as a value to the hash table. 
Then, in the second iteration, we check if each element's complement (target−nums[i]) exists in the hash table. 
If it does exist, we return current element's index and its complement's index. 
Beware that the complement must not be nums[i] itself!
Complexity Analysis
    Time complexity: O(n). 
    We traverse the list containing nnn elements exactly twice. 
    Since the hash table reduces the lookup time to O(1), the overall time complexity is O(n).

    Space complexity: O(n). 
    The extra space required depends on the number of items stored in the hash table, which stores exactly n elements.
'''


def twoSum(nums: list, target: int) -> list:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


'''
One-pass Hash Table Solution
Runtime: 88 ms
Memory Usage: 15.4 MB
Algorithm:
It turns out we can do it in one-pass. 
While we are iterating and inserting elements into the hash table, 
we also look back to check if current element's complement already exists in the hash table. 
If it exists, we have found a solution and return the indices immediately.
Complexity Analysis
    Time complexity: O(n). 
    We traverse the list containing nnn elements only once. Each lookup in the table costs only O(1) time.

    Space complexity: O(n). 
    The extra space required depends on the number of items stored in the hash table, which stores at most nnn elements.

'''


def twoSum(nums: list, target: int) -> list:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


print(twoSum(nums=[3, 4, 0, 14, 9], target=9))
