# def twoSum(nums: list, target: int) -> list:
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[j] == target - nums[i]:
#                 return [i, j]

def twoSum(nums: list, target: int) -> list:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


# def twoSum(nums: list, target: int) -> list:
#     hashmap = {}
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in hashmap:
#             return [i, hashmap[complement]]
#         hashmap[nums[i]] = i


print(twoSum(nums=[3, 4, 0, 14, 9], target=9))
