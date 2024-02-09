import time
import random
import string
import pytest

from pageObjects.Checkout_page_credkart import Test_checkout_page_01
from utilities.readConfigFile import Readconfig
from utilities.Logger import LogGenerator


@pytest.mark.usefixtures("setup")

class Test_checkout:

    email= Readconfig.getemail_name()
    password = Readconfig.getpassword()
    First_name = Readconfig.getFirst_name()
    Last_name = Readconfig.getLast_name()
    Phone = Readconfig.getPhone()
    Address = Readconfig.getAddress()
    Zip = Readconfig.getZip()
    Owner_name = Readconfig.getOwner_name()
    CVV = Readconfig.get_CVV()
    Card_number_01 = Readconfig.getCard_number_01()
    Card_number_02 = Readconfig.getCard_number_02()
    Card_number_03 = Readconfig.getCard_number_03()
    Card_number_04 = Readconfig.getCard_number_04()
    log = LogGenerator.loggen()


    def test_chechout_login(self,setup):
        self.log.info("Testcase test_UserLogin001 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lc =Test_checkout_page_01(self.driver)
        self.lc.Enter_Email_Id(self.email)
        self.log.info(" Entering Email-->" + self.email)
        self.lc.Enter_Password(self.password)
        self.log.info(" Entering password-->" + self.password)
        self.lc.click_login_button()
        self.log.info("Click on login_button" )
        self.lc.click_on_product()
        self.log.info("Click on product")
        self.lc.Add_to_cart()
        self.log.info("Add to card")
        self.lc.check_out_process()
        self.log.info("Check out_process")
        self.lc.Enter_First_Name(self.First_name)
        self.log.info(" First_name-->" + self.First_name)
        self.lc.Enter_Last_Name(self.Last_name)
        self.log.info("Last_name-->" + self.Last_name)
        self.lc.Enter_Phone(self.Phone)
        self.log.info("Phone_number-->" + self.Phone)
        self.lc.Enter_Address(self.Address)
        self.log.info("Address-->" + self.Address)
        self.lc.Enter_Zip(self.Zip)
        self.log.info("Zip-->" + self.Zip)
        self.lc.Enter_state()
        self.log.info("Enter_sate->" +" ")
        self.lc.Enter_Owner_name(self.Owner_name)
        self.log.info("Owner_name-->" + self.Owner_name)
        self.lc.Enter_CVV(self.CVV)
        self.log.info("CVV-->" + self.CVV)
        self.lc.Enter_Year()
        self.log.info("Year-->" + " ")
        self.lc.Enter_Month()
        self.log.info("Month-->" + " ")
        self.lc.Enter_card_number_01(self.Card_number_01)
        self.log.info("Card_numner_01-->" + self.Card_number_01)
        self.lc.Enter_card_number_02(self.Card_number_02)
        self.log.info("Card_numner_02-->" + self.Card_number_02)
        self.lc.Enter_card_number_03(self.Card_number_03)
        self.log.info("Card_numner_03-->" + self.Card_number_03)
        self.lc.Enter_card_number_04(self.Card_number_04)
        self.log.info("Card_numner_04-->" + self.Card_number_04)
        self.lc.Click_on_Checkout_button()
        self.log.info("Chekout_button")
        self.lc.Print_bill()
        self.log.info("Print_bill->" + " ")

# pytest -v -s -n=1 --html=HtmlReports/chrome_report.html --browser chrome
















