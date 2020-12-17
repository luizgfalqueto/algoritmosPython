def swap(vet, i, menor):
    aux = vet[i]
    vet[i] = vet[menor]
    vet[menor] = aux



def selectionSort(vet):
    for i in range(len(vet)):
        menor = i
        for j in range(i+1, len(vet)):
            if vet[j] < vet[menor]:
                menor = j

        if i != menor:
            swap(vet, i, menor)
    return vet


def main():
    vet = [6, 3, 4, 5, 2, 7, 1, 9, 8, 0]

    print(selectionSort(vet))

if __name__ == '__main__':
    main()