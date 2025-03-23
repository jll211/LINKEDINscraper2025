import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import random
import json
import re
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

SELECT_CONTRACT_BUTTON_SELECTOR = "#main > div > div > div:nth-child(3) > form > div > ul > li:nth-child(1) > div > div.contract-list__item-buttons > button"


def get_lk_credentials(path="./lk_credentials.json"):
    f = open(path)
    data = json.load(f)
    f.close()
    return data


def enter_ids_on_lk_signin(driver, email, password):
    try:
        # Warten, bis das Username-Feld sichtbar und klickbar ist
        usernameInputElement = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "username"))
        )
        usernameInputElement.clear()
        usernameInputElement.send_keys(email)
        
        # Warten, bis das Passwort-Feld sichtbar und klickbar ist
        passwordInputElement = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        passwordInputElement.clear()
        passwordInputElement.send_keys(password)
        
        # Warten, bis der Submit-Button sichtbar und klickbar ist
        submitElement = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button"))
        )
        
        # Kurze Pause vor dem Klicken
        time.sleep(1)
        submitElement.click()
        
        # Nach dem Klicken längere Zeit warten, damit LinkedIn eine Sicherheitsabfrage anzeigen kann
        print("Login-Daten übermittelt. Warte auf Weiterleitung...")
        time.sleep(8)
        
        # Prüfen, ob eine Sicherheitsabfrage erscheint
        try:
            challenge_page = "checkpoint/challenge" in driver.current_url
            security_verification = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "input__email_verification_pin"))
            )
            print("SICHERHEITSABFRAGE ERKANNT! Bitte gib den Sicherheitscode ein, der an deine E-Mail oder Telefonnummer gesendet wurde.")
            input("Drücke Enter, wenn du den Sicherheitscode eingegeben hast...")
        except (TimeoutException, NoSuchElementException):
            # Wenn keine Sicherheitsabfrage erscheint, ist das in Ordnung
            if "checkpoint/challenge" in driver.current_url:
                print("SICHERHEITSABFRAGE ERKANNT! Bitte folge den Anweisungen im Browser.")
                input("Drücke Enter, wenn du die Sicherheitsüberprüfung abgeschlossen hast...")
    
    except Exception as e:
        print(f"Fehler beim Login: {str(e)}")
        print("Bitte versuche, dich manuell anzumelden, wenn du das Browserfenster siehst.")
        input("Drücke Enter, wenn du dich erfolgreich angemeldet hast...")


def get_lk_url_from_sales_lk_url(url):
    parsed = re.search("/lead/(.*?),", url, re.IGNORECASE)
    if parsed:
        return f"https://www.linkedin.com/in/{parsed.group(1)}"
    return None


def select_contract_lk(driver):
    # Auch hier WebDriverWait verwenden
    contract_filter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, SELECT_CONTRACT_BUTTON_SELECTOR))
    )
    contract_filter.click()
    time.sleep(4)
    return


def remove_url_parameter(url, param):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if param in query_params:
        del query_params[param]

    new_query = urlencode(query_params, doseq=True)
    new_url = urlunparse(
        (
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            new_query,
            parsed_url.fragment,
        )
    )

    return new_url