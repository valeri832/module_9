first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(X) for X in first_strings if len(X) >= 5]

second_result = [(X, Y) for X in first_strings for Y in second_strings if len(X) == len(Y)]

third_result = {X: len(X) for X in first_strings + second_strings if len(X) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
