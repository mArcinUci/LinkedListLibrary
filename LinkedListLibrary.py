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
        data = [next(reader_code_generator), first_name, last_name, email, my_books]
        new_node = ReadersNode(data)
        new_node.next = self.head
        self.head = new_node
        print(f'Account created. Reader {first_name} {last_name} succcesfully added to the Library')

    def delete_reader_data(self, first_name, last_name, email):
        count = 0
        if self.head.data[1] == first_name and self.head.data[2] == last_name and self.head.data[3] == email and len(self.head.data[4]) != 0:
            print(f'Sorry {self.head.data[1]} there are still books to be returned in your account')
            count += 1
        if self.head.data[1] == first_name and self.head.data[2] == last_name and self.head.data[3] == email and len(self.head.data[4]) == 0:
            self.head = self.head.next
            print(f'{first_name}`s data deleted')
            count +=1
    
        pointer = self.head
        while pointer.next:
            if pointer.next.data[1] == first_name and pointer.next.data[2] == last_name and pointer.next.data[3] == email and len(pointer.next.data[4]) != 0:
                print(f'Sorry {pointer.data[1]} there are still books to be returned in your account')
                count += 1
                break
            if pointer.next.data[1] == first_name and pointer.next.data[2] == last_name and pointer.next.data[3] == email and len(pointer.next.data[4]) == 0:
                pointer.next = pointer.next.next
                print(f'{first_name}`s data deleted')
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
                print(f'Succes. New data: {new_first_name} {new_last_name}, with email: {new_email}')
                break
            pointer = pointer.next

    def print_users(self):
        pointer = self.head
        while pointer != None:
            print(f'Reader: {pointer.data[1]} {pointer.data[2]}, with email: {pointer.data[3]} and Readers Code: {pointer.data[0]}')
            pointer = pointer.next

    def find_reader_code(self, first_name, last_name, email):
        count = 0
        pointer = self.head
        while pointer != None:
            if pointer.data[1] == first_name and pointer.data[2] == last_name and pointer.data[3] == email:
                print(f'{first_name}`s Library Code is: {pointer.data[0]}')
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
            print(f'Sorry Mate, there is no such ReaderCode as {reader_code} in our Library, do you want to create an account?')

    def book_borrowing(self, reader_code, borrowed_book):
        pointer = self.head
        while pointer != None:
            if pointer.data[0] == reader_code:
                pointer.data[4].append(borrowed_book)
                break
            pointer = pointer.next

    def book_returning(self, reader_code, author, book_title):
        pointer = self.head
        while pointer != None:
            if pointer.data[0] == reader_code:
                for value in pointer.data[4]:
                    if value[0] == author and value[1] == book_title:
                        pointer.data[4].remove(value)
                        print(pointer.data[4])
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
        book_all_copies_code = []
        borrowed_copies_codes = []
        book_code = code.book_code_generator(author, book_title)
        for _ in range(int(how_many_copies)):
            single_book_code = next(book_code)
            book_all_copies_code.append(single_book_code)
        
        data = [author, book_title, book_all_copies_code, borrowed_copies_codes]
        new_book_node = BookNode(data)
        if self.head == None:
            self.head = self.tail = new_book_node
            self.head.prev = None
            self.head.next = None
        
        self.tail.next = new_book_node
        new_book_node.prev = self.tail
        new_book_node.next = None
        self.tail = new_book_node
        print(f'Succes. {how_many_copies} copies of book \"{book_title}\" by {author.upper()} added to the Library')

    def serch_book(self, author, book_title):
        pointer = self.head
        while pointer != None:
            if pointer.data[0] == author and pointer.data[1] == book_title:
                print(f'Book found. Out of all {len(pointer.data[2])} Library copies, {len(pointer.data[3])} were borrowed')
                break
            pointer = pointer.next

    def book_borrow(self, author, book_title, reader_code):
        borrowed_book_data = []
        pointer = self.tail
        while pointer != None:
            if pointer.data[0] == author and pointer.data[1] == book_title and (len(pointer.data[2]) - len(pointer.data[3])) == 0:
                print(f'Sorry Reader with code {reader_code}, but thera are no more copies of \"{book_title}\" in the Library')
                break
            if pointer.data[0] == author and pointer.data[1] == book_title and (len(pointer.data[2]) - len(pointer.data[3])) > 0:
                codes_taken = [taken_book_code[0] for taken_book_code in pointer.data[3]]
                codes_available = [available_book_code for available_book_code in pointer.data[2] if available_book_code not in codes_taken]
                pointer.data[3].append([codes_available[0], reader_code])
                borrowed_book_data = [author, book_title, codes_available[0]]
                l.book_borrowing(reader_code, borrowed_book_data)
                print(f'Confirmed, book {book_title} is now saved as borrowed')
                break
            pointer = pointer.prev

    def book_back(self,reader_code, author, book_title):
        pointer = self.tail
        while pointer != None:
            if pointer.data[0] == author and pointer.data[1] == book_title:
                book_back_data = [value for value in pointer.data[3] if reader_code in value]
                pointer.data[3].remove(book_back_data[0])
                print(f'Confirmed, book {book_title} is now back to the Library by: {reader_code}')
                l.book_returning(reader_code, author, book_title)
                break
            pointer = pointer.prev

    def print_library_books(self):
        pointer = self.head
        while pointer != None:
            print(f'{pointer.data[0].upper()} book: \"{pointer.data[1]}\", all copies: {len(pointer.data[2])}, copies beeing borrowed: {len(pointer.data[3])}')
            pointer = pointer.next


code = CodeGenerators
reader_code_generator = code.readers_code_generator()
l = LibraryReader()
lb = BookLinkedList()


l.create_reader('Basia', 'Jarok', 'bj@bj.bj')
l.create_reader('Marko', 'Babul', 'markoB@bolal.op')
l.create_reader('Jahun', 'Gardias', 'jahunG@op.com')
l.create_reader('Martha', 'Frun', 'frun@allert.us')
l.create_reader('Gary', 'Zol', 'gzol@areozol.air')
l.find_reader_code('Jahun', 'Gardias', 'jahunG@op.com')

lb.add_book_to_library('Stanislaw Lem', 'Solaris', 4)
lb.add_book_to_library('Steven Erikson', 'Gardens of the Moon', 1)
lb.add_book_to_library('Samantha Shannon', 'The Priory of the Orange Tree', 5)
lb.print_library_books()
print('++++++++')
lb.serch_book('Samantha Shannon', 'The Priory of the Orange Tree')
print('++++++++')
lb.book_borrow('Steven Erikson', 'Gardens of the Moon', 'R2')
lb.book_borrow('Steven Erikson', 'Gardens of the Moon', 'R4')
lb.book_borrow('Stanislaw Lem', 'Solaris', 'R3')
lb.book_borrow('Stanislaw Lem', 'Solaris', 'R2')
lb.print_library_books()
print('++++++++')
l.what_book_to_return('R2')
l.what_book_to_return('R3')
l.what_book_to_return('R4')
lb.book_back('R3','Stanislaw Lem', 'Solaris')
lb.book_back('R2', 'Steven Erikson', 'Gardens of the Moon')
lb.book_back('R2', 'Stanislaw Lem', 'Solaris')
l.what_book_to_return('R4')
print('++++++++')
l.print_users()
l.delete_reader_data('Basia', 'Jarok', 'bj@bj.bj')
l.delete_reader_data('Gary', 'Zol', 'gzol@areozol.air')
print('++++++++')
lb.serch_book('Samantha Shannon', 'The Priory of the Orange Tree')
l.print_users()