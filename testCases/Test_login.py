import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("******************** Test_001_Login ************************ ")
        self.logger.info("******************** Verifying home page Title ************************ ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":

            assert True
            self.driver.close()
            self.logger.info("******************** home page Title passed ************************ ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("******************** home page Title failed ************************ ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("******************** Verifying home page login ************************ ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("******************** home page login passed ************************ ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.driver.close()
            self.logger.error("******************** home page Title failed ************************ ")
