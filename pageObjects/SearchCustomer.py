import pytest

class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtfname_id = "SearchFirstName"
    txtlname_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults = "//table[@role='grid']"
    tbl_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,Email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(Email)

    def setfname(self,fname):
        self.driver.find_element_by_id(self.txtfname_id).clear()
        self.driver.find_element_by_id(self.txtfname_id).send_keys(fname)

    def setlname(self,lname):
        self.driver.find_element_by_id(self.txtlname_id).clear()
        self.driver.find_element_by_id(self.txtlname_id).send_keys(lname)

    def clicksearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.tbl_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.tbl_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag







