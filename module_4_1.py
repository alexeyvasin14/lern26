from true_math import divid as div
from fake_math import divid as vid
fake_divide = vid
true_divide = div

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)