
from collections import Counter
class Solution:
  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)
        freq = count.most_common(k)
        result = []
        for x in freq:
            result.append(x[0])
        return result
