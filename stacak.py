class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None 

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None 

    def size(self):
        return len(self.items)

    def display(self):
        if not self.is_empty():
            print("daftar pelanggan yang sedang mengantri:")
            for i, item in enumerate(reversed(self.items), 1):
                print(f"{i}. {item}")
        else:
            print("tidak ada pelanggan yang sedang mengantri.")


stack = Stack()
dilayani = []  
batal = []  

'''menampilkan antrian dengan urutan LIFO (Last In, First out) 
yang dimana urutan yang terakhir masuk, adalah yang pertama keluar.'''
stack.push("Agus")
stack.push("Samsul")
stack.push("Kipli")
stack.display() 


#menampilkan hasil antrian ketika sudah ada yang membatalkan tiket
batal.append(stack.pop())
print("\n(kondisi ketika ada yang membatalkan tiket)")
stack.display() #code ini untuk nampilkan sisa antrian yang sudah di kurangi oleh antrian yang batal untuk membeli tiket.
print(f"pelanggan yang membatalkan tiket: {batal[-1]}") #code ini untuk menampilkan pelanggan yang batal membeli tiket.

while not stack.is_empty():
    dilayani.append(stack.pop())

#menampilkan hasil semua antrian yang sudah terlayani
print("\n(setelah semua antrian terlayani)")
print("daftar pelanggan yang telah dilayani:")
for i, item in enumerate(dilayani, 1): #pada fungsi "enumerate", berguna untuk menambah indeks pada perulangan
    print(f"{i}. {item}") #menampilkan hasil dari semua antrian yang sudah terlayani

#menampilkan pelanggan yang membatalkan tiket
print("\ndaftar pelanggan yang membatalkan tiket:")
if batal:
    for i, item in enumerate(batal, 1): 
        print(f"{i}. {item}")

#menampilkan pesan jika tidak ada yang membatalkan tiket
else:
    print("tidak ada yang membatalkan tiket.")
