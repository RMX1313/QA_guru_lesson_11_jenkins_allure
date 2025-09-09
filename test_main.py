import allure
from selene import browser, be, have
import os
from selene.support.shared import browser
from selenium.webdriver.common.by import By


def test_form():
    with allure.step('Открываем формум регистрации'):
        file_path = os.path.join(os.path.dirname(__file__), 'file.txt')
        browser.open('https://demoqa.com/automation-practice-form')

        try:
            ad_iframe = browser.element('iframe#google_ads_iframe_...')
            browser.driver.execute_script("arguments[0].style.display='none';", ad_iframe._impl)
        except Exception:
            pass
        close_button = browser.element('close_button_svg')
        try:
            close_button.should(be.present, timeout=5)
            close_button.click()
        except Exception:
            pass
    with allure.step('Заполнение формы'):
        browser.element('#firstName').should(be.visible).type('Александр')
        browser.element('#lastName').should(be.visible).type("Евдошенко")
        browser.element('#userEmail').should(be.blank).type('remix-92@mail.ru')
        browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
        browser.element('#userNumber').should(be.blank).type('8800200100')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('May')
        browser.element('.react-datepicker__year-select').type('1992')
        browser.element('.react-datepicker__day--013').click()
        browser.element('#subjectsInput').type('Computer Science').press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
        browser.element('#uploadPicture').send_keys(file_path)
        browser.element('#currentAddress').type('ул.Жилая, 1')

        # Получаем WebDriver элемент из Selene
        driver = browser.driver
        element = driver.find_element(By.CSS_SELECTOR, '#state')

        # Прокручиваем элемент в видимую область
        browser.execute_script("arguments[0].scrollIntoView(true);", element)


        browser.element('#state').click()
        browser.element('#react-select-3-option-0').click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-0').click()
        browser.element('#submit').press_enter()
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    with allure.step('Проверка реезультата'):
        browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Александр Евдошенко',
        'remix-92@mail.ru',
        'Male',
        '8800200100',
        '13 May,1992',
        'Computer Science',
        'Sports',
        'file.txt',
        'ул.Жилая, 1',
        'NCR Delhi'
    ))


