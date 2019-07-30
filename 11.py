# import random
#
# game_over = False
# score = 0
#
# while not game_over:
#     score += random.randint(1,10)
#     print(score)
#
#     if score < 50:
#         continue
#
#     if score > 100:
#         game_over = True
#         break
#
#     print("You are getting close to winning")
#     print("You Win!")

nums = [1, 1, 2, 1, 2, 3]

def array123(nums):
  for num in nums:
      print(num)

array123(nums)
