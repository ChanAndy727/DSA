class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        t = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[t]:
                t = i
            res = max(res, prices[i] - prices[t])
        return res