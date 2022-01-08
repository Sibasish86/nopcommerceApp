import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer

class Test_004_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("***** Test_004_SearchCustomer ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** login successful ***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clicksearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.driver.close()
