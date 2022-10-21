from functools import reduce

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def list1():
    my_list1 = []
    for n in my_list:
        my_list1.append(n)
    print(my_list1)

    my_list1 = [n for n in my_list]
    print(my_list1)

    my_list2 = list(map(lambda x: x, my_list))
    print(my_list2)

    my_list3 = list(filter(lambda x: x, my_list))
    print(my_list3)


def even_num():
    my_list1 = []
    for n in my_list:
        if n % 2 == 0:
            my_list1.append(n)
    print(my_list1)

    my_list2 = [n for n in my_list if n % 2 == 0]
    print(my_list2)

    my_list4 = list(filter(lambda x: x % 2 == 0, my_list))
    print(my_list4)


def doubles():
    my_list1 = []
    for n in my_list:
        my_list1.append(n * 2)
    print(my_list1)

    my_list1 = [n * 2 for n in my_list]
    print(my_list1)

    my_list3 = list(map(lambda x: x * 2, my_list))
    print(my_list3)


def list4():
    my_list1 = []
    for letter in 'abcd':
        for num in range(4):
            my_list1.append((letter, num))
    print(my_list1)

    my_list2 = [(letter, num) for letter in 'abcd' for num in range(4)]
    print(my_list2)


def dict():
    names = ['A', 'B', 'C', 'D', 'E']
    numbers = [1, 2, 3, 4, 5]

    my_dict = {}
    for name, number in zip(names, numbers):
        my_dict[name] = number
    print(my_dict)

    my_dict1 = {name: number for name, number in zip(names, numbers)}
    print(my_dict1)


def reduce_fun():
    evens = list(filter(lambda n: n % 2 == 0, my_list))
    print(evens)

    doubles = list(map(lambda n: n * 2, evens))
    print(doubles)

    sum1 = reduce(lambda a, b: a + b, doubles)
    print(sum1)


def set_fun():
    my_set = set()
    for n in my_list:
        my_set.add(n)
    print(my_set)

    my_set = {n for n in my_list}
    print(my_set)


if __name__ == '__main__':
    while True:
        choice = int(input("1.list\n2.Even numbers\n3.Double values\n"
                           "4.list 4\n5.Dictionary\n6.Reduce function\n"
                           "7.set\n"
                           "Enter your choice : "))

        choice_dictionary = {1: list1, 2: even_num, 3: doubles, 4: list4,
                             5: dict, 6: reduce_fun, 7: set_fun}
        if choice == 0:
            break
        elif choice > 7:
            print("Please enter correct choice")
        else:
            choice_dictionary.get(choice)()

