# Латынин А.А.
def main(input: str) -> str:
    values_list = input.split()
    operation_tuple = ('+', '-', '/', '*')
    range_list = tuple(map(str, range(1, 11)))
    if len(values_list) != 3:
        raise Exception
    a, op, b = values_list
    if op not in operation_tuple:
        raise Exception
    if not ((a in range_list) and (b in range_list)):
        raise Exception
    return eval(input)


if __name__ == '__main__':
    print(main(input=input()))
