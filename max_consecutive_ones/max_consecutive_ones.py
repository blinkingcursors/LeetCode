from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        count_max = 0
        for item in nums:
            if item == 1:
                count += 1
            else:
                if count > count_max:
                    count_max = count
                count = 0
        if count > count_max:
            count_max = count
        return count_max

   # If 1 is there, increment count and compare it with maximum (count_max). If we see a 0, we reset count as 0


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, ''.join(map(str, nums)).split('0')))
