class Library:
    def __init__(self):
        self.books_file = open("books.txt", "a+")
    
    def __del__(self):
        self.books_file.close()

    def list_books(self):
        self.books_file.seek(0)
        books = self.books_file.read().splitlines()#dosyayı okuyup her satırı bir dizi elemanı olarak ele alır
        for book in books:
            book_info = book.split(",")#book değişkeninin içeriğini virgülle ayırarak bir liste oluşturur. 
            #Bu işlem, book değişkeninin içinde bulunan metni virgüllerle ayrılmış parçalara böler ve 
            #her bir parçayı liste olarak book_info değişkenine atar. Bu sayede book_info listesi, 
            #kitap bilgilerini içeren bir listeye dönüşür.
            print(f"Kitap Adi: {book_info[0]}, Yazar: {book_info[1]}")
    
    def add_book(self):
        book_title = input("Kitabin ismi:")
        book_author = input("Kitabin yazari:")
        release_year = input("Yayinlanma tarihi:")
        number_of_pages = input("Sayfa sayisi:")
        book_info = f"{book_title},{book_author},{release_year},{number_of_pages}\n"
        self.books_file.write(book_info)
        print("Kitap Basariyla eklendi.")
    
    def remove_book(self):
        book_title = input("Hangi Kitabi Silmek Istiyorsunuz?")
        self.books_file.seek(0)
        books = self.books_file.read().splitlines()
        new_books = []
        for book in books:
            book_info = book.split(",")
            if book_info[0] != book_title:
                new_books.append(book)
        self.books_file.close()
        self.books_file = open("books.txt", "w")
        for book in new_books:
            self.books_file.write(f"{book}\n")
        self.books_file.close()
        print("Kitap başariyla silindi.")
        self.books_file = open("books.txt", "a+")
        
lib = Library()
while(True):
    
    metin = "***MENU***\n1) List Books\n2) Add Book\n3) Remove Book\nq) Quit"
    satirlar = metin.splitlines()
    for satir in satirlar:
        print(satir)

    secim = input("Hangi İslemi Yapmak Istiyorsunuz?")
    if secim.lower() == "q":
        break
    secim = int(secim)
    if secim == 1:
        lib.list_books()
    elif secim == 2:
        lib.add_book()
    elif secim == 3:
        lib.remove_book()
    else:
        print("Geçersiz Seçim")





























  


    
