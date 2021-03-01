from selenium import webdriver
from macrotrends_scraper.helpers import get_balance_sheet_df


def main():
    url = "https://www.macrotrends.net/stocks/charts/AAPL/apple/balance-sheet"

    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get(url)
    html = driver.page_source

    df = get_balance_sheet_df(html=html)
    return df


if __name__ == "__main__":
    main()
