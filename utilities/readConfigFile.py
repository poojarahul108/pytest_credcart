import configparser

config = configparser.RawConfigParser()  # this (configparser.RawConfigParser) method is use  to read the data from
# config.ini
# file # .ini file we have # create to save the common data

config.read("C:\\Users\\Sir\\PycharmProjects\\pythonProjectframe\\Configuration\\config.ini")

#
class Readconfig:

    @staticmethod
    def getUserEmail():
        UserEmail = config.get('login data', 'UserEmail') # this is gpoing to fetch data from common data section and from Useremail field
        #config.get('section', 'Field')
        return UserEmail

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'Password')
        return Password

    @staticmethod
    def getemail_name():
        email = config.get('Checkout product', 'email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('Checkout product', 'password')
        return password

    @staticmethod
    def getFirst_name():
        First_name = config.get('Checkout product','First_name')
        return First_name

    @staticmethod
    def getLast_name():
        Last_name = config.get('Checkout product','Last_name')
        return Last_name

    @staticmethod
    def getPhone():
        Phone = config.get('Checkout product', 'Phone')
        return Phone

    @staticmethod
    def getAddress():
        Address = config.get('Checkout product', 'Address')
        return Address

    @staticmethod
    def getZip():
        Zip = config.get('Checkout product', 'Zip')
        return Zip

    @staticmethod
    def getOwner_name():
        Owner_name = config.get('Checkout product', 'Owner_name')
        return Owner_name

    @staticmethod
    def get_CVV():
        CVV = config.get('Checkout product', 'CVV')
        return CVV


    @staticmethod
    def getCard_number_01():
        Card_number_01 = config.get('Checkout product', 'Card_number_01')
        return Card_number_01

    @staticmethod
    def getCard_number_02():
        Card_number_02 = config.get('Checkout product', 'Card_number_02')
        return Card_number_02

    @staticmethod
    def getCard_number_03():
        Card_number_03 = config.get('Checkout product', 'Card_number_03')
        return Card_number_03

    @staticmethod
    def getCard_number_04():
        Card_number_04 = config.get('Checkout product', 'Card_number_04')
        return Card_number_04

















