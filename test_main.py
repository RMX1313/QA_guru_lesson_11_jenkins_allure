from selene import browser, be, have
import os
from utils import attach
image_path = os.path.abspath("textfile.txt")
import allure
from selene.support.shared import browser

def test_fill_form(setup_browser):
    browser = setup_browser
    browser.open('https://demoqa.com/automation-practice-form')
    #Заполнение графы Имя
    attach.add_screenshot(browser)
    with allure.step("Заполняем имя"):
        browser.element('[id="firstName"]').should(be.visible).type("Иван")
    #Заполнение графы Фамилия
    with allure.step("Заполняем фамилию"):
        browser.element('[id="lastName"]').should(be.visible).type("Иванов")
    #Заполнение графы почты
    with allure.step("Заполняем почту"):
        browser.element('[id="userEmail"]').should(be.visible).type("ivanov22@gmail.com")
    #Выбор радиокнопки
    with allure.step("Выбираем пол"):
        browser.element('label[for="gender-radio-1"]').click()
    #Заполнение графы телефон
    with allure.step("Заполняем телефон"):
        browser.element('[id="userNumber"]').should(be.visible).type("89098887678")
    #Выбор даты рождения
    with allure.step("Выбор даты рождения"):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__day--021').should(be.visible).click()
    #Выбор Subjects
    with allure.step("Выбор предмета"):
        browser.element('#subjectsInput').should(be.visible).type('Maths').press_enter()
    #Выбор хобби
    with allure.step("Выбор хобби"):
        browser.element('label[for ="hobbies-checkbox-1"]').click()
    #Загрузка файла
    with allure.step("Загрузка файла"):
        browser.element('[id = "uploadPicture"]').should(be.visible).send_keys(image_path)
    #Заполнение адреса
    with allure.step("Заполнение адреса"):
        browser.element('[id="currentAddress"]').should(be.visible).type("ул.Пушкина д.Колотушкина кв.3")
    #Выбор штата
    with allure.step("Выбор штата"):
        browser.element('#state input').type('NCR').press_enter()
        #browser.element('[id="state"]').should(be.visible).click()
        #browser.element('#react-select-3-input').type('NCR').press_enter()
    #Выбор города
    with allure.step("Выбор города"):
        browser.element('[id="city"]').should(be.visible).click()
        browser.element('[id="react-select-4-input"]').type('Delhi').press_enter()
    #Отправка формы
    with allure.step("Отправка формы"):
        browser.element('#submit').click()
    #browser.element('[id="submit"]').should(be.visible).click()
    #Проверка отправки формы
    with allure.step("Проверка отправки формы"):
        browser.element('[id="example-modal-sizes-title-lg"]').should(be.visible).should(have.text('Thanks for submitting the form'))

def test_successfully_filling(setup_browser):
    with allure.step("Проверка формы"):
        test_fill_form(setup_browser)
        attach.add_screenshot(browser)
        table_element = browser.all('table.table-dark tbody tr')
        table_element.element_by(have.text('Student Name')).all('td').second.should(have.text('Иван Иванов'))
        table_element.element_by(have.text('Student Email')).all('td').second.should(have.text('ivanov22@gmail.com'))
        table_element.element_by(have.text('Gender')).all('td').second.should(have.text('Male'))
        table_element.element_by(have.text('Mobile')).all('td').second.should(have.text('8909888767'))
        table_element.element_by(have.text('Date of Birth')).all('td').second.should(have.text('21 August,2025'))
        table_element.element_by(have.text('Subjects')).all('td').second.should(have.text('Maths'))
        table_element.element_by(have.text('Hobbies')).all('td').second.should(have.text('Sports'))
        table_element.element_by(have.text('Picture')).all('td').second.should(have.text('textfile.txt'))
        table_element.element_by(have.text('Address')).all('td').second.should(have.text('ул.Пушкина д.Колотушкина кв.3'))
        table_element.element_by(have.text('State and City')).all('td').second.should(have.text('NCR Delhi'))



