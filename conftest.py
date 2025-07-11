import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en or ru")

#@pytest.fixture(scope="function")
#def browser():
#    print("\nstart browser for test..")
#    browser = webdriver.Chrome()
#    yield browser
#    print("\nquit browser..")
#    browser.quit()

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    user_language = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()