

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
# Your code here:
ans = 0
for i in range(1000):
    if i%3==0 or i%5==0:
        ans+=i
print(ans)

ans1=0
print(sum([i for i in range(1000) if i%3==0 or i%5==0]))

def SumMultiple_3_5(k):
    ans1=0
    for i in range(k):
        if i % 3 == 0 or i % 5 == 0:
            ans1 += i
    return ans1
print(SumMultiple_3_5(1000))

def SumMultiple_3_5A(k,List):
    ans2=0
    for i in range(k):
        for num in List:
            if i%num==0:
                ans2 += i
                break
    return ans2
print(SumMultiple_3_5A(1000,[3,5]))


