def load_data(path):
    with open(path, 'r') as f:
        data = []
        for row in f:
            data.append(row.rstrip())
    return data