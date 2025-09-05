import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attach

@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    options = Options()
    # Добавляем UUID для дополнительной уникальности в CI
    unique_id = str(uuid.uuid4())
    temp_profile_dir = tempfile.mkdtemp(prefix=f'chrome_profile_{unique_id}_')
    options.add_argument(f'--user-data-dir={temp_profile_dir}')
    browser.config.driver_options = options
    yield  # Тест выполняется здесь
    # Teardown: закрываем браузер и очищаем директорию
    browser.quit()
    shutil.rmtree(temp_profile_dir, ignore_errors=True)

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options

    )

    browser.config.driver = driver  # Создаем объект Selene с WebDriver
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()