import sys
import random
import time
import matplotlib.pyplot as plt
collection = []
dictionary = {}
big_list = []


def rewriting_collection(n):
    global collection
    collection = []
    for x in range(n):
        collection.append(x)


def generate_edges(n, m, q, r):
    global big_list
    out_list = []

    if n == 10001:
        out_list = big_list.copy()
    else:
        for x in range(n):
            for y in range(x + 1, n):
                out_list.append([x, y])

    m = min(m, (n**2 - n) // 2)
    out_list = random.sample(out_list, m)

    for x in range(len(out_list)):
        y = random.randint(q, r)
        out_list[x].append(y)
    
    return out_list


def get_parent_comp(a):
    if collection[a] == a:
        return a
    else:
        collection[a] = get_parent_comp(collection[a])  
        return collection[a]


def parent_init_comp(a, b):
    x = get_parent_comp(a)
    y = get_parent_comp(b)
    if x > y:
        collection[y] = x
    else:
        collection[x] = y


def get_parent(a):
    if collection[a] == a:
        return a
    else:
        return get_parent_comp(collection[a])


def parent_init(a, b):
    x = get_parent(a)
    y = get_parent(b)
    if x > y:
        collection[y] = x
    else:
        collection[x] = y

        
def quick_sort(nums):  
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)


def partition(nums, low, high):
    pivot = nums[(low + high) // 2][2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i][2] < pivot:
            i += 1

        j -= 1
        while nums[j][2] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def finding_way_comp(num_edges):
    out = []

    #Алгоритм Краскала по поиску минимального остовного дерева

    for x in range(len(num_edges)):
        if get_parent_comp(num_edges[x][0]) != get_parent_comp(num_edges[x][1]):
            out.append(num_edges[x])
            parent_init_comp(num_edges[x][0], num_edges[x][1])

    return out


def finding_way(num_edges):
    out = []

    #Алгоритм Краскала по поиску минимального остовного дерева

    for x in range(len(num_edges)):
        if get_parent(num_edges[x][0]) != get_parent(num_edges[x][1]):
            out.append(num_edges[x])
            parent_init(num_edges[x][0], num_edges[x][1])

    return out


def test_1():
    print('ruinning test 1')
    #Вариант с n^2/10
    n = 1
    q = 1
    r = 1000000
    T1 = []
    T2 = []
    n_list = []

    while n < 1002:
        m = n ** 2 // 10
        print(n)

        rewriting_collection(n)
        list_1 = generate_edges(n, m, q, r)
        quick_sort(list_1)

        start = time.time()
        void = finding_way_comp(list_1)
        T1.append(time.time() - start)
        
        rewriting_collection(n)
        start = time.time()
        void = finding_way(list_1)
        T2.append(time.time() - start)

        n_list.append(n)
        n += 100

    plt.figure()
    plt.plot(n_list, T1, label='T1')
    plt.plot(n_list, T2, label='T2')
    plt.legend()
    plt.grid(True)
    plt.show()

    #Вариант с n^2

    n = 1
    q = 1
    r = 1000000
    T1 = []
    T2 = []
    n_list = []

    while n < 1002:
        m = int(1 + (0.45 + random.random() / 20) * n ** 2)
        print(n)

        rewriting_collection(n)
        list_1 = generate_edges(n, m, q, r)
        quick_sort(list_1)

        start = time.time()
        void = finding_way_comp(list_1)
        T1.append(time.time() - start)
        
        rewriting_collection(n)
        start = time.time()
        void = finding_way(list_1)
        T2.append(time.time() - start)

        n_list.append(n)
        n += 100

    plt.figure()
    plt.plot(n_list, T1, label='T1')
    plt.plot(n_list, T2, label='T2')
    plt.legend()
    plt.grid(True)
    plt.show()


def test_2():
    print('ruinning test 2')
    #Вариант с 100n
    n = 101
    q = 1
    r = 1000000
    T1 = []
    T2 = []
    n_list = []

    while n < 10002:
        m = n * 100
        print(n)

        rewriting_collection(n)
        list_1 = generate_edges(n, m, q, r)
        quick_sort(list_1)

        start = time.time()
        void = finding_way_comp(list_1)
        T1.append(time.time() - start)
        
        rewriting_collection(n)
        start = time.time()
        void = finding_way(list_1)
        T2.append(time.time() - start)

        n_list.append(n)
        n += 100

    plt.figure()
    plt.plot(n_list, T1, label='T1')
    plt.plot(n_list, T2, label='T2')
    plt.legend()
    plt.grid(True)
    plt.show()

    #Вариант с 1000n

    n = 101
    q = 1
    r = 1000000
    T1 = []
    T2 = []
    n_list = []

    while n < 10002:
        m = n * 1000
        print(n)

        rewriting_collection(n)
        list_1 = generate_edges(n, m, q, r)
        quick_sort(list_1)

        start = time.time()
        void = finding_way_comp(list_1)
        T1.append(time.time() - start)
        
        rewriting_collection(n)
        start = time.time()
        void = finding_way(list_1)
        T2.append(time.time() - start)

        n_list.append(n)
        n += 100

    plt.figure()
    plt.plot(n_list, T1, label='T1')
    plt.plot(n_list, T2, label='T2')
    plt.legend()
    plt.grid(True)
    plt.show()


def test_3():
    #Вариант с m
    n = 10001
    m = 0
    q = 1
    r = 1000000
    T1 = []
    T2 = []
    m_list = []

    while m < 1000001:
        print(m)

        rewriting_collection(n)
        list_1 = generate_edges(n, m, q, r)
        quick_sort(list_1)

        start = time.time()
        void = finding_way_comp(list_1)
        T1.append(time.time() - start)
        
        rewriting_collection(n)
        start = time.time()
        void = finding_way(list_1)
        T2.append(time.time() - start)

        m_list.append(m)
        m += 100000

    plt.figure()
    plt.plot(m_list, T1, label='T1')
    plt.plot(m_list, T2, label='T2')
    plt.legend()
    plt.grid(True)
    plt.show()


def test_4():
    print('ruinning test 4')
    #Вариант с r, m = n^2
    n = 10001
    q = 1
    r = 1
    T1 = []
    T2 = []
    r_list = []

    while r < 21:
        m = int(1 + (0.45 + random.random() / 20) * n ** 2)
        print(r)

        rewriting_collection(n)
        list_1 = generate_edges(n, m, q, r)
        quick_sort(list_1)
        print(r)

        start = time.time()
        void = finding_way_comp(list_1)
        T1.append(time.time() - start)
        print(r)
        
        rewriting_collection(n)
        start = time.time()
        void = finding_way(list_1)
        T2.append(time.time() - start)
        print(r)

        r_list.append(r)
        r += 1

    plt.figure()
    plt.plot(r_list, T1, label='T1')
    plt.plot(r_list, T2, label='T2')
    plt.legend()
    plt.grid(True)
    plt.show()

    #Вариант с r, m = 1000n
    n = 10001
    q = 1
    r = 1
    T1 = []
    T2 = []
    r_list = []

    while r < 21:
        m = 1000 * n
        print(r)

        rewriting_collection(n)
        list_1 = generate_edges(n, m, q, r)
        quick_sort(list_1)

        start = time.time()
        void = finding_way_comp(list_1)
        T1.append(time.time() - start)
        
        rewriting_collection(n)
        start = time.time()
        void = finding_way(list_1)
        T2.append(time.time() - start)

        r_list.append(r)
        r += 1

    plt.figure()
    plt.plot(r_list, T1, label='T1')
    plt.plot(r_list, T2, label='T2')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    for x in range(10001):
        for y in range(x + 1, 10001):
            big_list.append([x, y])

    #test_1()
    test_2()
    #test_3()
    #test_4()
