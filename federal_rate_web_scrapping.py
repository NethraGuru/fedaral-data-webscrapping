import csv
import time
import argparse
from playwright.sync_api import sync_playwright

def scrape_full_table(urls, table_selector="table", button_selector="#viewall-button", output_prefix="table_data"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        for index, url in enumerate(urls):
            print(f"🔹 Processing URL {index+1}/{len(urls)}: {url}")
            page.goto(url)
            
            # Wait for page to load
            page.wait_for_timeout(5000)
            
            # Check if the "View All" button exists
            if page.locator(button_selector).count() > 0:
                print("🔹 Clicking 'View All' button to load full data...")
                page.locator(button_selector).click()
                page.wait_for_timeout(5000)
            
            # Extract table data
            if page.locator(table_selector).count() == 0:
                print("❌ Table not found on this page.")
                continue
            
            table = page.locator(table_selector)
            rows = table.locator("tr").all()
            
            data = []
            for row in rows:
                cells = row.locator("td, th").all_inner_texts()
                if cells:
                    data.append(cells)
            
            # Save data to CSV
            output_file = f"{output_prefix}_{index+1}.csv"
            with open(output_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            
            print(f"✅ Data saved to {output_file}")
        
        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape tables from multiple URLs.")
    parser.add_argument("urls", nargs="+", help="List of URLs to scrape")
    args = parser.parse_args()
    
    scrape_full_table(args.urls)
