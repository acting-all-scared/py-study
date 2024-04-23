import math

d = {1,2,3,4,5}
print(d)

#평균 구하기

mean = sum(d)/len(d)
print(mean)


#분산 구하기
vsum = 0
for x in d:
    vsum = vsum + (x -mean)**2
var = vsum/len(d)
print(var)


#표준편차 
std = math.sqrt(var)
print(std)
