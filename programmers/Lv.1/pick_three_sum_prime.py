from itertools import combinations
def solution(nums):
    nums = sorted(set(sum(i) for i in list(combinations(nums, 3))))
    for i in range(2, max(nums)):
        for j in range(len(nums)):
            if nums[j] and nums[j] > i and nums[j] % i == 0:
                nums[j] = None
    return len(nums) - nums.count(None)
