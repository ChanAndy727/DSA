from collections import defaultdict
class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    map = defaultdict(list)
    for s in strs:
      map[str(sorted(s))].append(s)
    return map.values()
