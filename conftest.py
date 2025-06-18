import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en or ru")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "en":
        print("\nstart chrome en browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': en})
        browser = webdriver.Chrome(options=options)
    elif language == "ru":
        print("\nstart chrome ru browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': ru})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be en or ru")
    yield browser
    print("\nquit browser..")
    browser.quit()