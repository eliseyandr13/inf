# 18021 76432

kol, max_from, m = 0, 0, 0
for i in range(12356, 76476):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count >= 16:
        kol += 1
        if m == 0:
            m = 1
            max_from = i
        elif i > max_from:
            max_from = i

print(kol)