from pathlib import Path

from utils import load_data


def fuel_module(mass, fuel_included=False):
    fuel = int(mass/3)-2

    if not fuel_included:
        return fuel
    else:  # go recursive
        if fuel <=0:
            return 0
        else:
            return fuel + fuel_module(fuel, fuel_included=True)


def main():

    # load data
    datapath = Path(Path(__file__).parent, '..', 'data', 'day1.txt')
    data = load_data(datapath)

    # convert to integers
    data = [int(item) for item in data]

    print('-- Part 1 --')
    
    # total fuel required
    fuel = sum([fuel_module(item) for item in  data])

    print(f'Total fuel requirement is: {fuel}')

    print('-- Part 2 --')

    # total fuel required
    fuel = sum([fuel_module(item, fuel_included=True) for item in  data])

    print(f'Total fuel requirement (including fuel weight) is: {fuel}')


if __name__ == '__main__':
    main()