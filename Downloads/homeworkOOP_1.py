class Phone:
    def __init__(self) -> None:
        self.number = None
        self._incoming_call = 0

    def set_number(self, number: str) -> None:
        """
        set number встановлює номер телефону
        :param number: номер в форматі +** *** *** ****
        :return: None
        """
        self.number = number

    def get_incoming_call(self) -> int:
        return self._incoming_call

    def received_call(self) -> None:
        self._incoming_call += 1

    def __str__(self) -> str:
        return f"Phone number: {self.number}"


def get_incoming_call(phones: list) -> int:
    count = 0
    for phone in phones:
        count += phone.get_incoming_call()
    return count


my_phone = Phone()
my_phone.set_number("+38 093 607 6687")
my_phone_1 = Phone()
my_phone_1.set_number("+38 095 685 4331")
print(my_phone.number)
print(my_phone.get_incoming_call())
my_phone.received_call()
my_phone.received_call()
my_phone_1.received_call()
print(my_phone.get_incoming_call())
print(my_phone.__str__())
print(get_incoming_call([my_phone, my_phone_1]))
