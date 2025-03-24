"""This is meant to be run as a CLI script.
It will visit the profiles in the given file and perform the actions specified in action_on_page_visit (moving mouse, scrolling down, etc.).

Example usage:
python lk_visitor.py --profile_file ./profiles.csv --shortest_wait_time 4 --longest_wait_time 7 --page_load_time 3
"""

import argparse
import logging
import time
import random
import pandas as pd
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from general_lk_utils import (
    get_lk_credentials,
    enter_ids_on_lk_signin,
)


LK_CREDENTIALS_PATH = "./lk_credentials.json"


def visit_pages(browser, wait_time, urls, action=None):
    for url in tqdm(urls):
        try:
            browser.get(url)
            # Explizites Warten auf das Laden der Seite
            WebDriverWait(browser, wait_time).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            if action:
                action(browser)
        except Exception as e:
            print(f"Fehler beim Besuch von {url}: {str(e)}")


def move_mouse(browser, x, y):
    webdriver.ActionChains(browser).move_by_offset(x, y).perform()


def scroll_down(browser, pixels):
    webdriver.ActionChains(browser).send_keys(Keys.PAGE_DOWN * pixels).perform()


def wait_random_time(minimum, maximum):
    wait = random.random() * (maximum - minimum) + minimum
    time.sleep(wait)


# Move the mouse, wait random time, scroll down, wait random time
def action_on_page_visit(driver, shortest_wait_time, longest_wait_time):
    move_mouse(driver, 0, 0)
    wait_random_time(shortest_wait_time, longest_wait_time)

    # Click on show all activity with WebDriverWait
    try:
        # Versuchen, den "Alle Aktivitäten anzeigen" Button zu finden und zu klicken
        activity_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "#main > section:nth-child(3) > div.pvs-list__outer-container > div > div > a"
            ))
        )
        activity_button.click()
        wait_random_time(shortest_wait_time, longest_wait_time)
    except:
        # No show all activity button - das ist OK, weiter machen
        pass
    
    # Scrolle die Seite nach unten
    scroll_down(driver, 10)
    wait_random_time(shortest_wait_time, longest_wait_time)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visit profiles on LinkedIn")
    parser.add_argument(
        "--profile_file",
        type=str,
        help="Path to the file containing the profiles to visit (accepts .csv and .xlsx as long as it has a column named 'linkedin_url')",
        required=True,
    )
    parser.add_argument(
        "--shortest_wait_time",
        type=int,
        help="Shortest wait time in seconds between actions",
        required=False,
        default=4,
    )
    parser.add_argument(
        "--longest_wait_time",
        type=int,
        help="Longest wait time in seconds between actions",
        required=False,
        default=7,
    )
    parser.add_argument(
        "--page_load_time",
        type=int,
        help="Time to wait in seconds for page to load",
        required=False,
        default=3,
    )
    args = parser.parse_args()

    # Get the arguments
    profile_file = args.profile_file
    shortest_wait_time = args.shortest_wait_time
    longest_wait_time = args.longest_wait_time
    page_load_time = args.page_load_time

    profiles_df = []
    # Read the profile file
    if profile_file.endswith(".csv"):
        profiles_df = pd.read_csv(profile_file)
    else:
        # ends with .xlsx
        profiles_df = pd.read_excel(profile_file)

    profile_urls = profiles_df["linkedin_url"].tolist()
    print(f"Found {len(profile_urls)} profile urls.")

    print("Starting the driver...")
    logging.getLogger("selenium").setLevel(logging.CRITICAL)
    # Start the webdriver without any logs
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.linkedin.com/login/")

    print("Inputting the credentials...")
    lk_credentials = get_lk_credentials(LK_CREDENTIALS_PATH)
    enter_ids_on_lk_signin(driver, lk_credentials["email"], lk_credentials["password"])

    if "checkpoint/challenge" in driver.current_url:
        print(
            "It looks like you need to complete a double factor authentification. Please do so and press enter when you are done."
        )
        input()
    visit_pages(
        driver,
        page_load_time,
        profile_urls,
        lambda browser: action_on_page_visit(
            browser, shortest_wait_time, longest_wait_time
        ),
    )
    driver.close()