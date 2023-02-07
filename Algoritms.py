from random import randint
from math import floor
from collections import deque

"""inputs"""
not_integer_list = [0, 'b', 3]
random_list = []
example_list = [x for x in range(10)]
rounded_list = [floor(x / 2) for x in range(10)]

while len(random_list) <= 20:
    random_list.append(randint(0, 100))

""" functions"""


def is_list_integer(checking_list):
    integer_list = []
    for element in checking_list:
        if isinstance(element, int):
            integer_list.append(element)
        else:
            return False
    return integer_list


def binary_search(searching_list, searching_item):
    if is_list_integer(searching_list) and isinstance(searching_item, int):
        sorted_list = sorted(searching_list)
        low = 0
        high = len(sorted_list) - 1
        while low <= high:
            mid = floor((low + high) / 2)
            guess = sorted_list[mid]
            if guess == searching_item:
                return f' your choosen value is on position {mid}'
            if guess > searching_item:
                high = mid - 1
            else:
                low = mid + 1
        return None
    else:
        return f'searching list {searching_list} or searching_item have an element(s) that is/are not an integer type'


"""quick sort and recurent"""


def quick_sort(non_sorted_list):
    if len(non_sorted_list) < 2:
        return non_sorted_list
    else:
        middle = non_sorted_list[0]
        less = [i for i in non_sorted_list[1:] if i <= middle]
        gather = [i for i in non_sorted_list[1:] if i > middle]
        return quick_sort(less) + [middle] + quick_sort(gather)


"""looking for highest diverse of value"""
value1_list = []


def diverse_value(value1, conteiner_of_list):
    if value1 < 2:
        return 1
    elif value1 % 2 == 0:
        conteiner_of_list.append(2)
        diverse_value(value1 / 2, conteiner_of_list)
    elif value1 % 3 == 0:
        conteiner_of_list.append(3)
        diverse_value(value1 / 3, conteiner_of_list)
    elif value1 % 5 == 0:
        conteiner_of_list.append(5)
        diverse_value(value1 / 5, conteiner_of_list)
    elif value1 % 7 == 0:
        conteiner_of_list.append(7)
        diverse_value(value1 / 7, conteiner_of_list)
    return conteiner_of_list


def greatest_common_divisor(val1, val2):
    if val2 > 0:
        print(f'a{val1}', f'b{val2}', f'intiger  {int(val1 / val2)} modulo', val1 % val2)
        return greatest_common_divisor(val2, val1 % val2)
    return val1


mango = {
    'ty': ['ala', 'ola', 'iza'],
    'ala': ['monika'],
    'ola': ['ula'],
    'iza': ['m'],
    'monika': [],
    'ula': [],
    'm': []}


def person_who_sells_mango(name):
    return name[-1] == 'm'


def search_who_sells_mango(name):
    searchin_queue = deque()
    searchin_queue += mango[name]
    searched = []
    while searchin_queue:
        person = searchin_queue.popleft()
        if person not in searched:
            if person_who_sells_mango(person):
                print(f'{person} sprzedaje mango')
                return True
            else:
                searchin_queue += mango[person]
                searched.append(person)
    return 'nikt nie sprzedaje mango'


"""DIJKSTRA ALGORITM"""

"""INPUTS"""
graf = {'start': {'a': 6, 'b': 2},
        'a': {'meta': 1},
        'b': {'a': 3, 'meta': 5},
        'meta': {}}
costs = {'a': 6, 'b': 2, 'meta': float('inf')}
parents = {'start': None, 'a': 'start', 'b': 'start', 'meta': None}
processed = []
"""graph with more complicated version"""
graf_a = {'start': {'a': 5, 'b': 2},
          'a': {'c': 4, 'd': 2},
          'b': {'a': 8, 'd': 7},
          'c': {'meta': 3, 'd': 6},
          'd': {'meta': 1},
          'meta': {}}

costs_a = {'a': 5, 'b': 2, 'c': float('inf'), 'd': float('inf'), 'meta': float('inf')}
parents_a = {'start': None, 'a': 'start', 'b': 'start', 'c': 'a', 'd': None, 'menta': None}

"""functions"""


def find_lowest_cost_node(costs_dict, processed_node):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node, cost in costs_dict.items():
        if cost < lowest_cost and node not in processed_node:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra_path(graph, costs_graph, parents_graph):
    processed_node_in_graph = []
    node = find_lowest_cost_node(costs_graph, processed_node_in_graph)
    while node is not None:
        cost = costs_graph[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs_graph[n] > new_cost:
                costs_graph[n] = new_cost
                parents_graph[n] = node
        processed_node_in_graph.append(node)
        node = find_lowest_cost_node(costs_graph, processed_node_in_graph)
    value = parents_graph['meta']
    path = ['meta']
    while value is not None:
        path.append(value)
        value = parents_graph[path[-1]]
    correct_path = [value for value in path[::-1]]
    return f'The most efficient path it is {correct_path} ' \
           f'and it costs is {costs_graph["meta"]}'


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4], 1))
    print(binary_search(rounded_list, 'b'))
    print(binary_search(not_integer_list, 1))
    print(binary_search(not_integer_list, 'b'))
    print(f'original list {random_list} after sorted {quick_sort(random_list)}')
    print(diverse_value(4, value1_list))
    print(diverse_value(120, value1_list))
    print(search_who_sells_mango('ty'))
    print()
    print(find_lowest_cost_node(costs, processed))
    print(dijkstra_path(graf, costs, parents))
    print(dijkstra_path(graf_a, costs_a, parents_a))
    print(greatest_common_divisor(27, 18))
