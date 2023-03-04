# libraries which is we need.
import csv
import datetime


# Customer class with it's variables.
class Customer:
    sozluk_cost = {"name": [], "id_number": [], "card_number": [], "card_password": []}

    def __init__(self, name, id_number, card_number, card_password):
        self.name = name
        self.id_number = id_number
        self.card_number = card_number
        self.card_password = card_password

    # A function to save customer to .csv file
    def save_to_csv(self, name, id_number, card_number, card_password):
        with open('cards.csv', 'a') as file:
            writer = csv.writer(file)

            if file.tell() == 0:  # check if the file is empty
                writer.writerow(['name', 'customer_id', 'card_number', 'card_password'])

            current_time = datetime.datetime.now()
            writer.writerow([name, id_number, card_number, card_password, current_time])

            for i in range(len(Customer.sozluk_cost["name"])):
                writer.writerow([Customer.sozluk_cost["name"][i], Customer.sozluk_cost["id_number"][i],
                                 Customer.sozluk_cost["card_number"][i], Customer.sozluk_cost["card_password"][i],
                                 current_time])

    # A function to check customer for payment.
    def check_payment(self, card_number, card_password):
        with open('cards.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 4 and row[2] == card_number and row[3] == card_password:
                    print("Payment successful!\n")
                    return
            print("Invalid card number or password")
