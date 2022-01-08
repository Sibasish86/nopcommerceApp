from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############# PYTEST HTML REPORTS #####################

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sibasish'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)