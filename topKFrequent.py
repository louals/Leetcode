class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        if k == len(nums):
            return nums
        
    
        count = Counter(nums)
        
        heap = []
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
       
        return [pair[1] for pair in heap]

        
