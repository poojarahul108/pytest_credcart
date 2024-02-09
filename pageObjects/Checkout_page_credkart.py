from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

class Test_checkout_page_01:
    # driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
    Text_Email_xpath = "//input[@name='email']"
    # driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
    Text_Password_css_selctor = "input[id='password']"
    # driver.find_element(By.XPATH, "//button[@type='submit']").click()
    click_login_button_xpath_01 = "//button[@type='submit']"
    # driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div/div/a[2]/h3").click()
    click_on_product_01_xpath = "/html/body/div/div[2]/div[3]/div/div/a[2]/h3"
    # driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
    Add_to_cart_xpath = "//input[@value='Add to Cart']"
    # driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
    check_out_process_xpath = "//a[@class='btn btn-success btn-lg']"
    Text_First_Name_xpath = "//input[@id='first_name']"
    # driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Credence")
    Text_Last_Name_xpath = "//input[@id='last_name']"
    # driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Pune")
    Text_Phone_xpath = "//input[@id='phone']"
    # driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9091929355")
    Text_Address_xpath = "//textarea[@id='address']"
    # driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Dhankawdi, Pune")
    Text_Zip_xpath = "//input[@id='zip']"
    # driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("411013")
    Text_state_xpath = "//select[@id='state']"
    # state = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
    # state.select_by_visible_text("Pune")
    Text_Owner_name_xpath = "//input[@id='owner']"
    # driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Tushar")
    Text_CVV_xpath = "//input[@id='cvv']"
    # driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("043")
    Text_Year_xpath = "//select[@id='exp_year']"
    # year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
    # year.select_by_index(2)
    Text_Month_xpath = "//select[@id='exp_month']"
    # month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
    # month.select_by_index(2)
    Text_card_number_01_xpath = "//input[@id='cardNumber']"
    Text_card_number_02_xpath = "//input[@id='cardNumber']"
    Text_card_number_03_xpath = "//input[@id='cardNumber']"
    Text_card_number_04_xpath = "//input[@id='cardNumber']"
    # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
    # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
    # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
    # driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")
    Click_on_Checkout_button_xpath = "//button[@id='confirm-purchase']"
    # driver.find_element(By.XPATH,"//button[@id='confirm-purchase']").click()
    Print_bill_xpath = "/html/body/div/div[1]/p[1]"
    # print(driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]").text)

    def __init__(self,driver):
        self.driver = driver

    def Enter_Email_Id(self,Email_id):
        self.driver.find_element(By.XPATH, self.Text_Email_xpath).send_keys(Email_id)

    def Enter_Password(self,Password_payment):
        self.driver.find_element(By.CSS_SELECTOR,self.Text_Password_css_selctor).send_keys(Password_payment)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.click_login_button_xpath_01).click()

    def click_on_product(self):
        self.driver.find_element(By.XPATH,self.click_on_product_01_xpath).click()

    def Add_to_cart(self):
        self.driver.find_element(By.XPATH,self.Add_to_cart_xpath).click()

    def check_out_process(self):
        self.driver.find_element(By.XPATH,self.check_out_process_xpath).click()

    def Enter_First_Name(self,First_Name):
        self.driver.find_element(By.XPATH,self.Text_First_Name_xpath).send_keys(First_Name)

    def Enter_Last_Name(self,Last_Name):
        self.driver.find_element(By.XPATH,self.Text_Last_Name_xpath).send_keys(Last_Name)

    def Enter_Phone(self,Phone):
        self.driver.find_element(By.XPATH,self.Text_Phone_xpath).send_keys(Phone)

    def Enter_Address(self,Address):
        self.driver.find_element(By.XPATH,self.Text_Address_xpath).send_keys(Address)

    def Enter_Zip(self,Zip_Number):
        self.driver.find_element(By.XPATH,self.Text_Zip_xpath).send_keys(Zip_Number)

    def Enter_state(self):
        Select(self.driver.find_element(By.XPATH,self.Text_state_xpath)).select_by_index(4)

    def Enter_Owner_name(self,Owner_Name):
        self.driver.find_element(By.XPATH,self.Text_Owner_name_xpath).send_keys(Owner_Name)

    def Enter_CVV(self,CVV):
        self.driver.find_element(By.XPATH,self.Text_CVV_xpath).send_keys(CVV)

    def Enter_Year(self):
        Select(self.driver.find_element(By.XPATH,self.Text_Year_xpath)).select_by_index(2)

    def Enter_Month(self):
        Select(self.driver.find_element(By.XPATH,self.Text_Month_xpath)).select_by_index(3)

    def Enter_card_number_01(self,Card_number_01):
        self.driver.find_element(By.XPATH,self.Text_card_number_01_xpath).send_keys(Card_number_01)

    def Enter_card_number_02(self,Card_number_02):
        self.driver.find_element(By.XPATH,self.Text_card_number_02_xpath).send_keys(Card_number_02)

    def Enter_card_number_03(self,Card_number_03):
        self.driver.find_element(By.XPATH,self.Text_card_number_03_xpath).send_keys(Card_number_03)

    def Enter_card_number_04(self,Card_number_04):
        self.driver.find_element(By.XPATH,self.Text_card_number_04_xpath).send_keys(Card_number_04)

    def Click_on_Checkout_button(self):
        self.driver.find_element(By.XPATH,self.Click_on_Checkout_button_xpath).click()

    def Print_bill(self):
        print(self.driver.find_element(By.XPATH,self.Print_bill_xpath).text)














