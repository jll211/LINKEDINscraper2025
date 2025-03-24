#!/usr/bin/env python
"""
Simple test script to check if the LinkedIn scraping setup works correctly.
"""

import json
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def test_lk_credentials():
    """Test if credentials file exists and has the required fields."""
    try:
        with open("lk_credentials.json", "r") as f:
            creds = json.load(f)
        
        if creds["email"] == "YOUR_LINKEDIN_EMAIL" or creds["password"] == "YOUR_LINKEDIN_PASSWORD":
            print("\n❌ ERROR: You need to update the credentials in lk_credentials.json")
            print("   Replace YOUR_LINKEDIN_EMAIL and YOUR_LINKEDIN_PASSWORD with your actual LinkedIn credentials.")
            return False
        
        print("✅ LinkedIn credentials file exists and contains required fields.")
        return True
    except FileNotFoundError:
        print("\n❌ ERROR: lk_credentials.json file not found.")
        return False
    except json.JSONDecodeError:
        print("\n❌ ERROR: lk_credentials.json has invalid JSON format.")
        return False
    except KeyError:
        print("\n❌ ERROR: lk_credentials.json is missing required 'email' or 'password' fields.")
        return False

def test_selenium_setup():
    """Test if Selenium and ChromeDriver work correctly."""
    try:
        print("Starting Chrome with Selenium...")
        options = Options()
        options.add_argument("--headless")  # Run in headless mode for testing
        driver = webdriver.Chrome(options=options)
        
        # Test by opening a simple website
        driver.get("https://www.google.com")
        print(f"✅ Successfully opened Google. Page title: {driver.title}")
        
        driver.quit()
        return True
    except Exception as e:
        print(f"\n❌ ERROR: Selenium test failed: {str(e)}")
        return False

def main():
    """Run all tests and report results."""
    print("\n============ LinkedIn Scraping Tools Setup Test ============\n")
    
    creds_ok = test_lk_credentials()
    selenium_ok = test_selenium_setup()
    
    print("\n============ Test Results ============")
    if creds_ok and selenium_ok:
        print("✅ All tests passed! Your setup is ready for LinkedIn scraping.")
        print("\nTo start using the tools, update your credentials in lk_credentials.json")
        print("Then run one of the scripts with appropriate parameters:")
        print("- LinkedIn Sales Navigator Search Scraper: python lksn_search_scraper.py --search-url \"YOUR_SEARCH_URL\" --start-page 1 --end-page 5")
        print("- LinkedIn Recruiter Search Scraper: python lkr_search_scraper.py --search-url \"YOUR_SEARCH_URL\" --start 1 --end 20")
        print("- LinkedIn Visitor: python lk_visitor.py --profile_file \"YOUR_PROFILE_FILE.csv\"")
    else:
        print("❌ Some tests failed. Please fix the issues before using the tools.")
    
    return 0 if (creds_ok and selenium_ok) else 1

if __name__ == "__main__":
    sys.exit(main())