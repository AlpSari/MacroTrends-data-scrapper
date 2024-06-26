from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from macrotrends_data_scrapper.utils.Logger import Logger
import json
import os


def create_driver(logger_str="info") -> "webdriver.chrome":
    """Create driver object.

    Driver is an WebDriver object that interacts with the website. Clicking,
    reading are the methods of the driver object.

    Parameters
    ----------
    url : string
        url of the website which is going to be scrapped

    logger_str : string
        logger objects level indicator

    Returns
    -------
    driver : WebDriver object

    """
    logger = Logger("create_driver", logger_str)
    logger.info("WebDriver is being created...")

    path = os.path.dirname(os.path.abspath(__file__))

    with open(f"{path}/webdriverOptions.json") as webdriver_options:
        options_dict = json.load(webdriver_options)

    # Get desired webdriver options
    logger.info(f"Webdriver Options = {options_dict['options']}...")

    # Add driver options to the driver
    options = Options()
    for opt in options_dict["options"]:
        options.add_argument(opt)

    # Below option enables web driver to be able to scrap when in headless mode
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
                 ' (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(options=options)

    # Finalize webdriver creation by calling the url
    logger.info("WebDriver is created!!!")
    return driver


def main():
    """Run create driver function."""
    driver = create_driver()
    driver.close()
    driver.quit()


if __name__ == "__main__":
    main()
