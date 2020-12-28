def merge(vetor, inicio, meio, fim):
    esq = vetor[inicio:meio]
    dir = vetor[meio:fim]

    topo_esq, topo_dir = 0, 0
    for i in range(inicio, fim):
        if topo_esq >= len(esq):
            vetor[i] = dir[topo_dir]
            topo_dir += 1
        elif topo_dir >= len(dir):
            vetor[i] = esq[topo_esq]
            topo_esq += 1
        elif esq[topo_esq] < dir[topo_dir]:
            vetor[i] = esq[topo_esq]
            topo_esq += 1
        else:
            vetor[i] = dir[topo_dir]
            topo_dir += 1



def mergeSort(vetor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor)
    if (fim - inicio > 1):
        meio = (fim + inicio)//2
        mergeSort(vetor, inicio, meio)
        mergeSort(vetor, meio, fim)
        merge(vetor, inicio, meio, fim)

    return vetor

def main():
    vet = [0, 5, 8, 3, 2, 9, 6, 1, 7, 4]
    print(mergeSort(vet))

if __name__ == '__main__':
    main()
