import os

dir_path = os.path.dirname(os.path.realpath(__file__))

FILE_NAME = os.path.join(dir_path, "request_counts.txt")


def import_data():
    counts = {
        'GET': 0,
        'POST': 0,
        'PUT': 0,
        'DELETE': 0
    }
    with open(FILE_NAME, 'r') as file:
        for line in file:
            if len(line) == 0:
                continue
            line = line.split()
            method = line[0]
            count = line[1]
            if method in counts:
                counts[method] = int(count)
    return counts


def export_data(datas):
    with open(FILE_NAME, 'w') as file:
        for data in datas:
            file.write('{0} {1} \n'.format(data, datas[data]))


def increase_count(method):
    counts = import_data()
    if method in counts:
        counts[method] += 1
    export_data(counts)


def main():
    print(import_data())


if __name__ == "__main__":
    main()
