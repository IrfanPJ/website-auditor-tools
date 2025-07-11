
# 🕸️ Web Scraper and HTML/CSS Analyzer using CrewAI

This project uses [CrewAI](https://github.com/joaomdmoura/crewai) and OpenAI's GPT-based agents to automate the process of scraping a website, analyzing its HTML/CSS code, and generating a clean technical report.

## 🚀 Features

* 🔍 **Website Scraping**
  Extracts full HTML content, inline styles, and external CSS from any valid URL.

* 🧠 **HTML/CSS Code Analysis**
  Reviews structure, accessibility, responsiveness, and code quality.

* 📝 **Report Generation**
  Summarizes strengths, flaws, and improvement suggestions into a developer-friendly markdown report.

## 📂 Project Structure

```
.
├── scraped_content/
│   └── index.html               # Scraped website HTML with embedded CSS
├── analysis/
│   └── web_code_analysis.md    # Raw HTML/CSS audit
├── reports/
│   └── final_report.md         # Summary report for developers
└── main.py                     # Main CrewAI workflow
```

## ⚙️ Requirements

* Python 3.8+
* [CrewAI](https://pypi.org/project/crewai/)
* [OpenAI Python SDK](https://github.com/openai/openai-python)
* API key for OpenAI (`gpt-4-turbo` or compatible)

Install all dependencies:

```bash
pip install crewai crewai-tools openai
```

## 🔑 Setup

1. Add your OpenAI API key in `main.py`:

```python
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
```

2. Run the script :

```bash
python main.py
```

3. Enter the target website URL when prompted.

## 🧑‍💻 How It Works

The system uses **three AI agents**, each with a specific task:

1. **Website Scraper** – Scrapes the full HTML and CSS content from a target URL.
2. **Code Analyzer** – Reviews the scraped HTML/CSS for structure and best practices.
3. **Report Generator** – Summarizes the analysis into a markdown report.

These agents work **sequentially** via CrewAI's task orchestration.

## 📌 Example Output

Here’s what to expect after running the pipeline:

* `scraped_content/index.html` – Fully embedded and clean HTML from the website.
* `analysis/web_code_analysis.md` – Raw audit of structure, semantics, and CSS quality.
* `reports/final_report.md` – Polished developer report with suggestions.

## 🛠️ Future Improvements

* Add multi-page scraping support
* Export reports in PDF/HTML
* Integrate Lighthouse or other tooling for deeper insights

# website-auditor-tools
