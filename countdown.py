from operator import *

def countdown(nums, ops, trace):
	n0 = nums[0]
	if len(nums) == 1:
		yield n0, str(n0)
		return
	for i,n in enumerate(nums[1:]):
		for f in ops:
			for r,t in countdown(nums[1:i] + nums[i+1:], [add, mul, sub], trace):
				if f != div or r != 0 and n0 % r == 0:
					yield f(n0, r), '%s(%s,%s)'% (f.__name__, n0, t)

def search(nums, target):
	for x,t in countdown(nums, [add, mul, sub, div], []):
		if x == target:
			print x,t

search([100,9,7,6,3,1], 253)