import random #Berfungsi untuk memasukan modul random pada code
NUMBER = [1,2,3,4,5,6,7,8,9,10]#menyimpan list yang berisi angka
random.shuffle(NUMBER)#mengacak isi dari "NIMBER" menggunakan function shuffle
def quickSort(arr): #function def untuk quick sort
    if len(arr) <= 1: #Jika panjang list atau jumlah elemen yang ada pada list kurang dari atau sama dengan satu
        return arr #maka akan mengembalikan function
    else:
        pivot = arr[0] #pivot yang digunakan adalah elemen list arr pada index ke-0

        print(f"Pivot : {pivot}")
        
        less = [x for x in arr[1:] if x <= pivot] #jika nilai x kurang dari atau sama dengan pivot yang digunakan maka akan dimasukan pada list variabel "less"

        greater = [x for x in arr[1:] if x > pivot]#jika nilai x lebih dari pivot yang digunakan maka akan dimasukan pada list variabel "greater"
    
        return quickSort(less) + [pivot] + quickSort(greater) #mengembalikan nilai dari quicksort list arr ditambah dengan nilai pivot dan ditambah quicksort list greater

print('''
1. Untuk Quicksort
''')
while True: #digunakan untuk melakukan perulangan
    a = input("Masukan Sorting Yang Ingin Digunakan: ") #digunakan untuk menyimpan inputan sorting yang akan digunakan
    if a == "1": #jika user memilih "1" maka akan menjalankan function quick sort
        print(f'list sebelum disort: {NUMBER}')
        print()
        print(f'list setelah disort: {quickSort(NUMBER)}')
        break #setelah function dijalankan maka akan mem break perulangan
    else:
        print("Input salah atau tidak ada") #jika input yang dimasukan tidak ada maka akan mengulangi inputan