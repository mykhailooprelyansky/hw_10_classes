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
        self.number = number
        if len(number) == 10 and number.isdigit():
            super().__init__(number)
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)
        else:
            return None

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                self.phones.remove(phone)
                self.phones.append(Phone(new_number))
                self.phones.reverse()
                break
        else:
            raise ValueError

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
        else:
            return None

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

print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")
