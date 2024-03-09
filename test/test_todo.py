from selene import have, be, browser, by
import os


def test_complete():
    browser.open('/')
    browser.element('#firstName').type("Ivanov")
    browser.element('#lastName').type("Ivan")
    browser.element('#userEmail').type("test@gmail.com")
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type("7145236584")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text("February")).click()
    browser.element('.react-datepicker__year-select').click().element(by.text("1998")).click()
    browser.element('.react-datepicker__day--018').click()
    browser.element('#subjectsInput').type("Maths").press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#currentAddress').type('Moscow, Russia')
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/image.jpg')
    browser.element('#react-select-4-input').should(be.disabled)
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').should(be.enabled)
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()
    browser.element('.table').all('td:nth-child(2)').should(have.texts(
        'Ivanov Ivan',
        'test@gmail.com',
        'Male',
        '7145236584',
        '18 February,1998',
        'Maths',
        'Reading',
        'image.jpg',
        'Moscow, Russia',
        'NCR Delhi'
    ))
