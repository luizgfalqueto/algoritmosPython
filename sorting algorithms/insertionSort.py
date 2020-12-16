def swap(vet, i, j):
    aux = vet[i]
    vet[i] = vet[j]
    vet[j] = aux


def insertionSort(vet):
    for i in range(1, len(vet)):
        aux = vet[i]
        j = i - 1

        while j >= 0 and aux < vet[j]:
            swap(vet, j + 1, j)
            j -= 1
    return vet


def main():
    vet = [6, 3, 4, 5, 2, 7, 1, 9, 8, 0]

    print(insertionSort(vet))


if __name__ == '__main__':
    main()