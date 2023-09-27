from collections import UserDict
from datetime import date, datetime


class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    # def __str__(self):
    #     return str(self.__value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, number):
        super().__init__(number)
        self.number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if len(value) == 10 and value.isdigit():
            self.__number = value
        else:
            raise ValueError("Uncorrect number")


class Birthday(Field):
    def __init__(self, dates):
        super().__init__(dates)
        self.__dates = None
        self.dates = dates

    @property
    def date(self):
        return self.__dates

    @date.setter
    def date(self, value):
        if value:
            try:
                datetime.strptime(value, '%d/%m/%y')
            except ValueError:
                print("Uncorrect date, must will be enter date in format: day/month/year")
            else:
                self.__dates = datetime.strptime(value, '%d/%m/%y')
        else:
            self.__dates = None


class Record:
    def __init__(self, name, dates=None):
        self.name = Name(name)
        self.date_of_birthday = Birthday(dates).value
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

    def days_to_birthday(self):
        if self.date_of_birthday:
            birthday = datetime.strptime(self.date_of_birthday, '%d/%m/%y')
            current_day = date.today()
            if birthday.month < current_day.month:
                year_of_future_birthday = current_day.year + 1
            else:
                year_of_future_birthday = current_day.year
            date_of_future_birthday = date(year=year_of_future_birthday, month=birthday.month, day=birthday.day)
            days_count = date_of_future_birthday - current_day
            return days_count.days
        else:
            return None

    def __str__(self):
        return (f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, "
                f"days to birthday: {self.days_to_birthday()}")


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

    def iterator(self):
        return Iterator(list(self.data.values()))


class Iterator:
    def __init__(self, address_book):
        self.address_book = address_book

    def __iter__(self):
        self.N = 3
        self.current_count_N = 0
        self.idx = 0
        return self

    def __next__(self):
        if self.current_count_N >= self.N:
            raise StopIteration
        else:
            value = self.address_book[self.idx]
            self.idx += 1
            self.current_count_N += 1
            return value


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane", "14/3/96")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

misha_record = Record("Misha", "24/8/94")
misha_record.add_phone("9876543210")
book.add_record(misha_record)

for i in book.iterator():
    print(i)


# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")
#
# print(john)
#
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")
#
# book.delete("Jane")
