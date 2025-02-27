# Web Scraping and Data Cleaning Project

## 📌 Overview
This project scrapes a dynamically loaded table from a JavaScript-rendered webpage using **Playwright**, extracts the data, and then processes it with **Pandas** to retain only the last 10 years of relevant records.

## 📦 Requirements
- **Python 3.8+** installed
- **Google Chrome** or Chromium-based browser installed

## 📁 Project Structure
```
.
├── data/                   # Data files
│   ├── raw/               # Raw scraped data
│   └── processed/         # Cleaned and processed data
├── docs/                  # Documentation files
├── notebooks/            # Jupyter notebooks
├── src/                  # Source code
└── requirements.txt      # Project dependencies
```

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2️⃣ Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 3️⃣ Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Install Playwright Browsers
```bash
python3 -m playwright install
```

## 🚀 Running the Project

urls = {
    'Federal_Funds_Rate': 'https://fred.stlouisfed.org/data/FEDFUNDS.txt',
    '1_Year_Treasury_Rate': 'https://fred.stlouisfed.org/data/GS1.txt',
    '10_Year_Treasury_Rate': 'https://fred.stlouisfed.org/data/GS10.txt'
}

#### 1️⃣ Run the Scripts
```bash
python3 src/federal_rate_web_scrapping.py 'url1' 'url2' 'url3'
python3 src/clean_data.py data/table_data_*.csv
```

## Next Steps
- [ ] Data Analysis using a Notebook in notebooks/rate_analysis_stats.ipynb
