'''
CellPhone class should have
    instance variables to keep track of the model
    phone number
    contacts (dict)
    messages (list)
    and if it's on vibrate or not

model and phone number are passed as parameters
hard code multiple contacts in the dictionary (value name, key contact's phone)

have a method to receive a text and prints the message as well as adds it to the messages list.
method to create and send (print) new text messages to contacts
'''


class CellPhone:
    def __init__(self, model, my_number):
        self.model = model
        self.my_number = my_number
        self.contacts = {
            "Mom": "(123) 456-7890",
            "Alex":  "(234) 567-8901",
            "Ian": "(345)678-9012"
        }
        self.message_list = []
        self.vibrate = False

    def receive_texts(self, message):
        print(message)
        self.message_list.append(message)

    def send_messages(self, message, recipient):
        if recipient in self.contacts:
            name = self.contacts.get(str(recipient))
            print(f"To {recipient}: {message}")
        else:
            print(f"To unknown number: {message}")
