def calculate_structure_sum(structure):
    c = 0
    if isinstance(structure, list):
        if len(structure) == 0:
            return 0
        c = c + calculate_structure_sum(structure[0])
        if len(structure) > 1:
            return c + calculate_structure_sum(structure[1:])
        else:
            return c
    elif isinstance(structure, int):
        return structure
    elif isinstance(structure, str):
        return len(structure)
    elif isinstance(structure, dict):
        return calculate_structure_sum(list(structure.items()))
    elif isinstance(structure, tuple):
        return calculate_structure_sum(list(structure))
    elif isinstance(structure, set):
        return calculate_structure_sum(list(structure))
    else:
        return c

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]



result = calculate_structure_sum(data_structure)
print(result)