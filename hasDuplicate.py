class solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        map = dict()
        for n in nums:
            if n in map:
                return True
            map[n] = True
        return False

