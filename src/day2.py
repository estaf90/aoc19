from pathlib import Path
from utils import load_data, intcode_computer


data = load_data(Path(Path(__file__).parent, '..', 'data', 'day2.txt'))
data = data[0].split(',')

# Convert to integers
intcode_program_default = [int(item) for item in data]

print('-- Part 1 --')

# make copy of program
intcode_program = [item for item in intcode_program_default]

intcode_program[1] = 12
intcode_program[2] = 2
# read the intcode program with an intcode computer
intcode_computer(intcode_program)

print('The value left at position 0 after restoration is: ', intcode_program[0])

print('-- Part 2 --')

# make copy of program

output = 19690720

for noun in range(len(intcode_program_default)):
    for verb in range(len(intcode_program_default)):
        intcode_program = [item for item in intcode_program_default]
        intcode_program[1] = noun
        intcode_program[2] = verb
        intcode_computer(intcode_program)
        if intcode_program[0] == output:
            print(f'Solution is: {100*noun+verb}\nFound for noun={noun} and verb={verb}')
            break

verb, noun