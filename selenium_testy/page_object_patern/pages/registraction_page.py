# -*- coding: utf-8 -*-
from base_page import BasePage
from locators import RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    """Klasa Strony Rejestracji"""

    def _verify_page(self):
        """Walidacja nazwy strony"""
        assert u"MediaMarkt" in self.driver.title

    def registration_button(self):
        """Klikniecie przycisku zarejestruj sie"""
        element = self.driver.find_element(*RegistrationPageLocators.REGISTRACTION_BUTTON)
        element.click()
        print u"Registration click registration button success"

    def error_validation_notice_is_no_presented(self):
        """Sprawdzenie czy nie sa presentowane errory"""
        error_notices = self.driver.find_elements(*RegistrationPageLocators.ERRPR_ALL_VALIDATION_FIELD)
        for error in error_notices:
            assert not error.is_displayed(), error.get_attribute(u"innerText")
            print u"Registration error all message no exist"

    def error_choose_gender(self):
        """Validacja pola plec"""
        error_message = self.driver.find_element(*RegistrationPageLocators.ERROR_VALIDATION_RADIO)
        assert error_message.is_displayed(), u"Wybierz zwrot"
        print u"Registration error message radio exist"

    def error_name_field(self):
        """Validacja pola imie"""
        error_message = self.driver.find_element(*RegistrationPageLocators.ERROR_VALIDATION_NAME_FIELD)
        assert error_message.is_displayed(), u"Podaj imię"
        print u"Registration error message name exist"

    def error_surname_field(self):
        """Validacja pola nazwisko"""
        error_message = self.driver.find_element(*RegistrationPageLocators.ERROR_VALIDATION_SURNAME_FIELD)
        assert error_message.is_displayed(), u"Podaj nazwisko"
        print u"Registration error message surname exist"

    def error_e_mail_field(self):
        """Validacja pola e_mail"""
        error_message = self.driver.find_element(*RegistrationPageLocators.ERROR_VALIDATION_E_MAIL_FIELD)
        assert error_message.is_displayed(), u"Podaj adres email"
        print u"Registration error message e_mail exist"

    def error_password_field(self):
        """Validacja pola haslo"""
        error_message = self.driver.find_element(*RegistrationPageLocators.ERROR_VALIDATION_PASSWORD_FIELD)
        assert error_message.is_displayed(), u"Podaj hasło"
        print u"Registration error message password exist"

    def error_phone_field(self):
        """Validacja pola telefon"""
        error_message = self.driver.find_element(*RegistrationPageLocators.ERROR_VALIDATION_PHONE_NUMBER)
        assert error_message.is_displayed(), u"Podaj numer telefonu"
        print u"Registration error message phone number exist"

    def error_pstal_code_field(self):
        """Validacja pola kod pocztowy"""
        error_message = self.driver.find_element(*RegistrationPageLocators.ERROR_VALIDATION_POSTAL_CODE)
        assert error_message.is_displayed(), u"Podaj kod pocztowy"
        print u"Registration error message postal code exist"
