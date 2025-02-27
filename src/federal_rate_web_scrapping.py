import csv
import time
import json
import argparse
from playwright.sync_api import sync_playwright

def scrape_full_table(urls_dict, table_selector="table", button_selector="#viewall-button", output_prefix="table_data"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        total_urls = len(urls_dict)
        for index, (name, url) in enumerate(urls_dict.items(), 1):
            print(f"🔹 Processing URL {index}/{total_urls}: {url}")
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
            
            # Save data to CSV using the name from the dictionary key
            output_file = os.path.join('data', f"{output_prefix}_{name}.csv")
            with open(output_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            
            print(f"✅ Data saved to {output_file}")
        
        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape tables from URLs specified in a dictionary.")
    parser.add_argument("urls_json", help="JSON string containing URLs dictionary")
    args = parser.parse_args()
    
    try:
        urls_dict = json.loads(args.urls_json)
        if not isinstance(urls_dict, dict):
            raise ValueError("Input must be a JSON dictionary")
        scrape_full_table(urls_dict)
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON input")
    except ValueError as e:
        print(f"❌ Error: {e}")