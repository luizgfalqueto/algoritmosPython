def swap(vet, i, menor):
    aux = vet[i]
    vet[i] = vet[menor]
    vet[menor] = aux


def bubbleSort(vet, tamanho):
    if tamanho <= 0: return

    for i in range(tamanho):
        if vet[i] > vet[i+1]:
            swap(vet, i, i+1)
    bubbleSort(vet, tamanho - 1)

    return vet


def main():
    vet = [6, 3, 4, 5, 2, 7, 10, 1, 9, 8, 0]
    print(bubbleSort(vet, len(vet)-1))


if __name__ == '__main__':
    main()