def array_front9(nums):
  num = 4 if len(nums) >= 4 else len(nums)
  for x in range(0, num):
    if nums[x] == 9:
      return True

  return False