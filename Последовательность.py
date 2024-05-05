def input_numbers():
    while True:
        numbers_str = input("Введите последовательность чисел через пробел: ")
        numbers_list = numbers_str.split()
        if all(x.isdigit() for x in numbers_list):
            return [int(x) for x in numbers_list]
        else:
            print("Некорректный ввод. Введите последовательность чисел через пробел.")

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

def main():
    numbers = input_numbers()
    x = int(input("Введите любое число: "))
    selection_sort(numbers)
    index = binary_search(numbers, x)
    if index < len(numbers) and numbers[index] == x:
        print(f"Число {x} находится в последовательности и его индекс равен {index}.")
    elif index == len(numbers):
        print(f"Число {x} больше всех чисел в последовательности.")
    else:
        print(f"Число {x} находится между числами с индексами {index - 1} и {index}.")

if __name__ == "__main__":
    main()
