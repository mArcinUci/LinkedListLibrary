class ReaderCodeGenerator:      
    def readers_code_generator():
        unique_number = 0
        while True:
            reader_unique_code = 'R' + str(unique_number)
            yield reader_unique_code
            unique_number += 1


class ReadersNode(ReaderCodeGenerator):
    def __init__(self,data):
        self.data = data
        self.next = None


class LibraryReader:
    def __init__(self):
        self.head = None

    def __str__(self):
        return self.data

    def create_reader(self, first_name, last_name, email):
        borrowed_books = []
        data = [next(reader_code), first_name, last_name, email, borrowed_books]
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

readers_code = ReaderCodeGenerator
reader_code = readers_code.readers_code_generator()