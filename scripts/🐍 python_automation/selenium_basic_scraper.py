from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

def kuma_tech_scraper():

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without window
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")



    driver = webdriver.Chrome(options=chrome_options)

    try:
        print("[Kuma-DoTech] Initializing Scraper Engine...")
        
        url = "https://www.scrapethissite.com/pages/simple/"
        driver.get(url)
        time.sleep(3) # Let the engine breathe

        print(f"[Kuma-DoTech] Accessing: {driver.title}")


        countries = driver.find_elements(By.CLASS_NAME, "country-name")
        capitals = driver.find_elements(By.CLASS_NAME, "country-capital")

        data_list = []
        for i in range(len(countries)):
            data_list.append({
                "Country": countries[i].text,
                "Capital": capitals[i].text
            })


        df = pd.DataFrame(data_list)
        df.to_csv("extracted_data.csv", index=False)
        print("[Kuma-DoTech] Success! Data saved to extracted_data.csv")

    except Exception as e:
        print(f"[!] Error Detected: {e}")
    
    finally:
        driver.quit()
        print("[Kuma-DoTech] Engine Shutdown.")

if __name__ == "__main__":
    kuma_tech_scraper()
