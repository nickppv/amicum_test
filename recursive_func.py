import json


def func(data):
    for i in data:
        if 'id' in i:
            res_list.append((i['title'], i['id']))
        if 'children' in i:
            new_data = i['children']
            func(new_data)
    return tuple(res_list)


with open('new_test_hw.json', 'r', encoding='UTF-8') as js:

    res_list = []
    data = json.load(js)
    data = data['children']
    res = func(data)
    print(*res)
    # print(*sorted(res, key=lambda x: x[1]))  # сортировка по id
