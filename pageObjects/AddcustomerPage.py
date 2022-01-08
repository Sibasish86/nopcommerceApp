import time
from selenium.webdriver.support.select import Select

class AddCustomer():
    lnkCustomers_menu_xpath = "//a[@href = '#']//*[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class ='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "//input[@id='Gender_Male']"
    rdFemaleGender_id = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    chkTaxexempt_xpath = "//input[@id='IsTaxExempt']"
    drpNewsletter = "//div[@class='k-widget k-multiselect k-multiselect-clearable']"
    drpMgrofVendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstItemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstItemForumMod_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstItemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstItemVendors_xpath = "//li[contains(text(),'Vendors')]"
    lstItemRegistered_xpath = "//li[contains(text(),'Registered')]"
    btnSave_xpath = "//button[@name = 'save']"
    lstItemyourStoreName_xpath = "//li[contains(text(),'Your store name')]"
    lstItemTestStore2_xpath = "//li[contains(text(),'Test store 2')]"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickonAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstItemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstItemAdministrators_xpath)
        elif role == 'Guest':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstItemGuests_xpath)
        elif role == 'Forum Moderators':
            self.driver.find_element_by_xpath(self.lstItemForumMod_xpath)
        elif role == 'Vendors':
            self.driver.find_element_by_xpath(self.lstItemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstItemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setnewsLetter(self,value):
        self.driver.find_element_by_xpath(self.drpNewsletter).click()
        if value == 'Your store name':
            self.lstitemNews = self.driver.find_element_by_xpath(self.lstItemyourStoreName_xpath)
        elif value == 'Test store 2':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedNewsletterSubscriptionStoreIds_taglist']/li/span[2]").click()
            self.lstitemNews = self.driver.find_element_by_xpath(self.lstItemTestStore2_xpath)
        else:
            self.lstitemNews = self.driver.find_element_by_xpath(self.lstItemTestStore2_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click;",self.lstitemNews)

        time.sleep(3)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.drpMgrofVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element_by_xpath(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_xpath(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_xpath(self.rdMaleGender_id).click()

    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self,content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()




