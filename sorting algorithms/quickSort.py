def swap(vet, i, j):
    aux = vet[i]
    vet[i] = vet[j]
    vet[j] = aux


def partition(vet, left, right):
    i = left + 1
    j = right
    pivot = vet[left]

    while i <= j:
        if vet[i] <= pivot:
            i += 1
        else:
            if vet[j] >= pivot:
                j -= 1
            else:
                if i <= j:
                    swap(vet, i, j)
                    i += 1
                    j -= 1

    swap(vet, left, j)
    return j


def quicksort(vet, left, right):
    if left < right:
        index = partition(vet, left, right)
        quicksort(vet, left, index - 1)
        quicksort(vet, index + 1, right)

    return vet

def main():
    vet = [6, 3, 4, 5, 2, 7, 1, 9, 8, 0]

    print(quicksort(vet, 0, len(vet) - 1))


if __name__ == '__main__':
    main()
