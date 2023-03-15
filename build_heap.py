# 221RDB231 Emīlija Ostaševska 4.gr


def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        parent = i

        while True:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            
            if left_child <= n - 1 and data[left_child] < data[parent]:
                parent = left_child
            if right_child <= n - 1 and data[right_child] < data[parent]:
                parent = right_child
            if i != parent:
                swaps.append((i, parent))
                data[i], data[parent] = data[parent], data[i]
                i = parent
            else:
                break

    return swaps


def main():
    fi = input("I or F: ")
    n = 0

    if "I" in fi or "i" in fi:
        n = int(input())
        data = list(map(int, input().split()))

    elif "F" in fi or "f" in fi:
        test_num = input("Choose test number (only 04 lol): ")
        with open(f"tests/{test_num}", "r") as file:
            n = int(file.readline().strip())
            data = list(map(int, file.readline().strip().split())) 

    assert len(data) == n
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
