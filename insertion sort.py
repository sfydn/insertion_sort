def insertion_sort(dizi):
    for i in range (len(dizi)):
        min_index = i
        for j in range(i+1, len(dizi)):
            if dizi[min_index] > dizi [j]:
                min_index= j
        if min_index != i:
            dizi[min_index], dizi[i] = dizi[i], dizi[min_index]

def insertion_sort(dizi):
    for i in range(1, len(dizi)):
        key = dizi[i]
        j = i - 1

        while j >= 0 and key <dizi[j] :
            dizi[j+1] = dizi[j]
            j = j - 1
        dizi[j+1] = key


sirasiz_dizi = [22,27,16,2,18,6]
insertion_sort (sirasiz_dizi)
print(sirasiz_dizi)


    
