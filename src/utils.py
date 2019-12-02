def load_data(path):
    with open(path, 'r') as f:
        data = []
        for row in f:
            data.append(row.rstrip())
    return data


def intcode_computer(data):
    """Used to read incode programs"""
    i = 0  # instruction pointer
    cont = True
    while cont:
        if data[i] == 99:  # opcode STOP
            cont = False
        elif data[i] == 1:  # opcode ADD
            instr = data[i:i+4]
            data[instr[3]] = data[instr[1]] + data[instr[2]]
            i += len(instr)
        elif data[i] == 2:  # opcode MULTIPLY
            instr = data[i:i+4]
            data[instr[3]] = data[instr[1]] * data[instr[2]]
            i += len(instr)
        else:
            raise ValueError(f'Not understood value of {data[i]}')