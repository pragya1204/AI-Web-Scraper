

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
load_dotenv()

SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")
# This is a simple web scraping function using Selenium and the Browser API.
if not SBR_WEBDRIVER:
    raise ValueError("SBR_WEBDRIVER environment variable not set.")

def scrape_website(website):
    print('Connecting to Browser API...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print('waiting for the captcha to solve... ')
        solve_res=driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {
                'detectTimeout': 10000,
            }
        })
        print('Captcha solved, navigating to the website...')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html
    
def extract_body_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    else:
        return "No body content found."
    
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()  # Remove script and style elements
    cleaned_content = soup.get_text(separator='\n')
    cleaned_content="\n".join(line for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]

