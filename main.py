from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, number):
        if len(number) == 10:
            super().__init__(number)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        self.phones.remove(Phone(number))

    def edit_phone(self, old_number, new_number):
        for i in self.phones:
            if i.value == old_number:
                self.phones.remove(i)
                self.phones.append(Phone(new_number))
                self.phones.reverse()

    def find_phone(self, number):
        for i in self.phones:
            if i.value == number:
                return i.value

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, records):
        self.data[records.name.value] = records

    def find(self, name):
        for key, value in self.data.items():
            if key == name:
                return value

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")

for name, record in book.data.items():
    print(record)