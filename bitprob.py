values = [1, 2, 4, 8, 16, 32, 64]
test = 74
test_result = []
for value in values:
    result = value & test
    if result > 0:
        test_result.append(result)
print(test_result)
