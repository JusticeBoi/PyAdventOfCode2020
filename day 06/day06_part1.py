RUN_TEST = False
TEST_SOLUTION = 11
TEST_INPUT_FILE = 'test_input_day_06.txt'
INPUT_FILE = 'input_day_06.txt'

ARGS = []


def main_part1(input_file, ):
    with open(input_file) as file:
        data = file.read()

    groups = data.split('\n\n')
    # create single string per group, then cast to set, then count elements
    lens = map(lambda group: len(set(''.join(group.split('\n')))),
               groups)
    solution = sum(lens)
    return solution


if __name__ == '__main__':
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert (TEST_SOLUTION == solution)
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
