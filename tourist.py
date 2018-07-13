# -*- coding: utf-8 -*-


def read_file(i=0, number_campus=0, lines=None, fo=None):

    line = next(lines).split()
    N, K, V = int(line[0]), int(line[1]), int(line[2])
    attractions = [next(lines).strip() for _ in range(int(line[0]))]
    attractions.extend(attractions)
    index = (K * (V - 1)) % N
    attractions_list = [{'rank': (index + i + 1) % N, 'name': attraction}
                        for i, attraction in enumerate(attractions[index:index + K])]
    for attraction in attractions_list:
        if attraction['rank'] == 0:
            attraction['rank'] = N
    attractions_list = list(sorted(attractions_list, key=lambda x: x['rank']))
    attractions_name = ' '.join([attraction['name'] for attraction in attractions_list])
    fo.write(f"Case #{i+1}: {attractions_name}\n")

    if i == number_campus - 1:
        return
    else:
        return read_file(i + 1, number_campus, lines, fo)


def main():

    f = open('tourist.txt', "r", encoding="utf-8")
    fo = open("output.txt", "w", encoding="utf-8")
    lines = f.readlines()
    read_file(number_campus=int(lines[0]), lines=(x for i, x in enumerate(lines) if i > 0 ), fo=fo)


if __name__ == "__main__":
    main()
