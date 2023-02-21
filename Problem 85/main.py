limit = 2000000
min = 10000

for n in range(2, 1200):
  for m in range(n, 1200):
    diff = abs((n*(n + 1) * m*(m + 1) / 4) - limit)
    if diff < min:
      area = n * m
      min = diff

print(area)