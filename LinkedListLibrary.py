class CodeGenerators:      
    def readers_code_generator():
        unique_number = 0
        while True:
            reader_unique_code = 'R' + str(unique_number)
            yield reader_unique_code
            unique_number += 1

    def book_code_generator(author, book_title):
        author_full_name = author.split()
        author_code = author_full_name[0][0] + author_full_name[0][-1] + author_full_name[-1][0] + author_full_name[-1][-1]
        book_full_title = book_title.split()
        book_code = book_full_title[0][0] + book_full_title[0][-1] + book_full_title[-1][0] + book_full_title[-1][-1]
        unique_number = 0
        while True:
            unique_number += 1
            yield author_code + book_code + str(unique_number)


class ReadersNode(CodeGenerators):
    def __init__(self,data):
        self.data = data
        self.next = None


class LibraryReader:
    def __init__(self):
        self.head = None

    def __str__(self):
        return self.data

    def create_reader(self, first_name, last_name, email):
        my_books = []
        data = [next(reader_code), first_name, last_name, email, my_books]
        new_node = ReadersNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete_reader_data(self, first_name, last_name, email):
        count = 0
        if self.head.data[1] == first_name and self.head.data[2] == last_name and self.head.data[3] == email and len(self.head.data[4]) != 0:
            print(f'Sorry {self.head.data[1]} there are still books to be returned in your account')
            count += 1
        if self.head.data[1] == first_name and self.head.data[2] == last_name and self.head.data[3] == email and len(self.head.data[4]) == 0:
            self.head = self.head.next
            count +=1
    
        pointer = self.head
        while pointer.next:
            if pointer.next.data[1] == first_name and pointer.next.data[2] == last_name and pointer.next.data[3] == email and len(pointer.next.data[4]) != 0:
                print(f'Sorry {pointer.data[1]} there are still books to be returned in your account')
                count += 1
                break
            if pointer.next.data[1] == first_name and pointer.next.data[2] == last_name and pointer.next.data[3] == email and len(pointer.next.data[4]) == 0:
                pointer.next = pointer.next.next
                count += 1
                break
            pointer = pointer.next
        if count == 0:
            print(f'There is something wrong with input data, there is no such person as {first_name} {last_name} with email: {email} in Library Readers List')

    def change_reader_data(self, reader_code, new_first_name, new_last_name, new_email):
        pointer = self.head
        while pointer != None:
            if pointer.data[0] == reader_code:
                pointer.data[1] = new_first_name
                pointer.data[2] = new_last_name
                pointer.data[3] = new_email
                break
            pointer = pointer.next

    def print_users(self):
        pointer = self.head
        while pointer != None:
            print(f'Reader: {pointer.data[1]} {pointer.data[2]}, with email: {pointer.data[3]} and Readers Code: {pointer.data[0]}')
            print(pointer.data[4])
            pointer = pointer.next

    def find_reader_code(self, first_name, last_name, email):
        count = 0
        pointer = self.head
        while pointer != None:
            if pointer.data[1] == first_name and pointer.data[2] == last_name and pointer.data[3] == email:
                print(pointer.data[0])
                count += 1
                break
            pointer = pointer.next
        if count == 0:
            print(f'There is something wrong with input data, there is no such person as {first_name} {last_name} with email: {email} in Library Readers List')
    
    def find_reader_by_code(self, reader_code):
        count = 0
        pointer = self.head
        while pointer != None:
            if pointer.data[0] == reader_code:
                print(f'{reader_code} is coding Library Reader: {pointer.data[1]} {pointer.data[2]} with email {pointer.data[3]}')
                count += 1
                break
            pointer = pointer.next
        if count == 0:
            print(f'Sorry Mate, there is no such ReaderCode as  in our Library {reader_code}, do you want to create an account?')

    def book_borrowing(self, reader_code, borrowed_book):
        pointer = self.head
        while pointer != None:
            if pointer.data[0] == reader_code:
                pointer.data[4].append(borrowed_book)
                break
            pointer = pointer.next
    
    def what_book_to_return(self, reader_code):
        pointer = self.head
        while pointer != None:
            if pointer.data[0] == reader_code:
                print(f'dear {pointer.data[1]}, you have {len(pointer.data[4])} book(s) to return: \n {pointer.data[4]}')
                break
            pointer = pointer.next


class BookNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class BookLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return self.data

    def add_book_to_library(self, author, book_title, how_many_copies):
        data = [author, book_title, how_many_copies]
        new_book_node = BookNode(data)
        if self.head == None:
            self.head = self.tail = new_book_node
            self.head.prev = None
            self.head.next = None
        
        self.tail.next = new_book_node
        new_book_node.prev = self.tail
        new_book_node.next = None
        self.tail = new_book_node

    def serch_book(self, author, book_title):
        pointer = self.head
        while pointer != None:
            if pointer.data[0] == author and pointer.data[1] == book_title:
                print(f'Book found. There are {pointer.data[2]} copie(s) in the Library')
                break
            pointer = pointer.next

    def book_borrow(self, author, book_title, reader_code):
        borrowed_book = []
        pointer = self.tail
        while pointer != None:
            if pointer.data[0] == author and pointer.data[1] == book_title and int(pointer.data[2]) == 0:
                print(f'Sorry but thera are no more copies of {book_title} in the Library')
                break
            if pointer.data[0] == author and pointer.data[1] == book_title and int(pointer.data[2]) > 0:
                pointer.data[2] -= 1
                borrowed_book = [author, book_title]
                l.book_borrowing(reader_code, borrowed_book)
                print(borrowed_book)
                break
            pointer = pointer.prev
     
    def print_library_books(self):
        pointer = self.head
        while pointer != None:
            print(pointer.data[0], pointer.data[1])
            pointer = pointer.next


code = CodeGenerators
reader_code = code.readers_code_generator()
book_code = code.book_code_generator('Stanislaw Lem', 'Solaris')
print(next(book_code))
print(next(book_code))


l = LibraryReader()
l.create_reader('Basia', 'Jarok', 'bj@bj.bj')
l.create_reader('Marko', 'Babul', 'markoB@bolal.op')
l.create_reader('Jahun', 'Gardias', 'jahunG@op.com')
l.create_reader('Martha', 'Frun', 'frun@allert.us')
l.create_reader('Gary', 'Zol', 'gzol@areozol.air')
l.print_users()
l.find_reader_by_code('R3')
l.find_reader_code('Marko', 'Babul', 'markoB@bolal.op')

l.delete_reader_data('Basia', 'Jarok', 'bj@bj.bj')
l.delete_reader_data('Martha', 'Frun', 'frun@allert.us')
l.delete_reader_data('Gary', 'Zo', 'gzol@areozol.air')
l.delete_reader_data('Marko', 'Babul', 'markoB@bolal.op')
l.print_users()
print('===========')
l.change_reader_data('R4','Gary', 'Z+++++++', 'gzol@areozol.air')
l.print_users()
lb = BookLinkedList()
lb.add_book_to_library('Stanislaw Lem', 'Solaris', 4)
lb.add_book_to_library('Stev Erikson', 'Gardens of the Moon', 1)
lb.add_book_to_library('Samantha Shannon', 'The Priory of the Orange Tree', 2)
lb.print_library_books()
lb.serch_book('Samantha Shannon', 'The Priory of the Orange Tree')
lb.book_borrow('Samantha Shannon', 'The Priory of the Orange Tree', 'R2')
print('++++++++')
lb.print_library_books()
lb.serch_book('Samantha Shannon', 'The Priory of the Orange Tree')

l.what_book_to_return('R2')