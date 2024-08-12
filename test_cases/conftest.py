import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from utilities.customLogger import LogGenerator
from selenium.webdriver.chrome.options import Options
import subprocess
logger = LogGenerator.genLog()

@pytest.fixture()
def setup(browser):
    logger.info(f"......Test Case Started......!")
    if browser == "chrome":
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(options=options)
        print("Launching chrome browser")
        return driver
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser")
        return driver
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching edge browser")
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = "Test_Enable_Technologies"
    config.stash[metadata_key]['Module Name'] = "Products"
    config.stash[metadata_key]['SDET'] = "Amol-Chopade"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep