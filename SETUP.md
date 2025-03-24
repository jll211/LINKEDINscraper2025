# LinkedIn Scraping Tools Setup Guide

This guide will help you set up and use the LinkedIn scraping tools in this repository.

## Prerequisites

- Python 3.6+
- Chrome browser
- Chrome WebDriver
- LinkedIn account (for Sales Navigator or Recruiter tools, you need those specific subscriptions)

## Setup Steps

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure LinkedIn credentials**:
   
   Edit the `lk_credentials.json` file:
   ```json
   {
       "email": "YOUR_LINKEDIN_EMAIL",
       "password": "YOUR_LINKEDIN_PASSWORD"
   }
   ```
   Replace `YOUR_LINKEDIN_EMAIL` and `YOUR_LINKEDIN_PASSWORD` with your actual LinkedIn credentials.

3. **Test your setup**:
   ```bash
   python test_setup.py
   ```
   This will verify that all components are working correctly.

## Using the Tools

### LinkedIn Sales Navigator Search Scraper

This tool extracts profile data from LinkedIn Sales Navigator search results.

```bash
python lksn_search_scraper.py --search-url "YOUR_SEARCH_URL" --start-page 1 --end-page 5 --save-format "csv"
```

Parameters:
- `--search-url`: The URL of your Sales Navigator search (required)
- `--start-page`: First page to scrape (default: 1)
- `--end-page`: Last page to scrape (default: 1)
- `--wait-time-between-pages`: Seconds to wait between pages (default: 5)
- `--wait-after-page-loaded`: Seconds to wait after page load (default: 3)
- `--wait-after-scroll-down`: Seconds to wait after scrolling (default: 3)
- `--save-format`: Output format ("xlsx" or "csv", default: "csv")

### LinkedIn Recruiter Search Scraper

This tool extracts profile data from LinkedIn Recruiter search results.

```bash
python lkr_search_scraper.py --search-url "YOUR_SEARCH_URL" --start 1 --end 20 --save-format "csv"
```

Parameters:
- `--search-url`: The URL of your Recruiter search (required)
- `--start`: First profile index to scrape (default: 1)
- `--end`: Last profile index to scrape (default: 1)
- `--wait-time-between-pages`: Seconds to wait between profiles (default: 5)
- `--wait-after-page-loaded`: Seconds to wait after page load (default: 3)
- `--wait-after-scroll-down`: Seconds to wait after scrolling (default: 3)
- `--save-format`: Output format ("xlsx" or "csv", default: "csv")

### LinkedIn Visitor

This tool visits LinkedIn profiles from a file (CSV or Excel) containing LinkedIn URLs.

```bash
python lk_visitor.py --profile_file "YOUR_PROFILE_FILE.csv" --shortest_wait_time 3 --longest_wait_time 8
```

Parameters:
- `--profile_file`: Path to file with LinkedIn URLs (required)
- `--shortest_wait_time`: Minimum wait time between actions (default: 4)
- `--longest_wait_time`: Maximum wait time between actions (default: 7)
- `--page_load_time`: Wait time for page loading (default: 3)

## Troubleshooting

1. **LinkedIn blocking issues**: If you're getting blocked, try increasing the wait times between actions.

2. **Selenium/Chrome issues**: Make sure your Chrome and ChromeDriver versions are compatible.

3. **Authentication problems**: If you encounter 2FA challenges, the script will prompt you to complete them manually.

## Disclaimer

Use these tools responsibly and in accordance with LinkedIn's terms of service. These tools are for educational purposes only.