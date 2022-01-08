import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddcustomerPage import AddCustomer
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("***** Test_003_AddCustomer ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** login successful ***")

        self.logger.info("*** Starting Add Customer Test ***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickonAddNew()

        self.logger.info("*** Providing customer info ***")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("kate")
        self.addcust.setLastName("reese")
        self.addcust.setGender("Male")
        self.addcust.setDob("7/05/1985")
        self.addcust.setCompanyName("QATest")
        self.addcust.setnewsLetter("Test Store 2")
        self.addcust.setCustomerRoles("Guest")
        self.addcust.setManagerOfVendor("Vendor 1")
        self.addcust.setAdminContent("TestQA")
        self.addcust.clickOnSave()

        self.logger.info("****saving Customer info ****")

        self.logger.info("***** Add customer validation started ****")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            assert True == False

        self.driver.close()


def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))





