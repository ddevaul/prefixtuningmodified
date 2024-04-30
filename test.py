import math
q1 = 1
q2 = 0.5
q3 = 0.1
t = 0.01
print((math.e ** (q1/t))/ (math.e ** (q1/t) + math.e**(q2/t) + math.e**(q3/t)))
print((math.e ** (q2/t))/ (math.e ** (q1/t) + math.e**(q2/t) + math.e**(q3/t)))
print((math.e ** (q3/t))/ (math.e ** (q1/t) + math.e**(q2/t) + math.e**(q3/t)))
