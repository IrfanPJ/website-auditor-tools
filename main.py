import os
from crewai import Agent, Task, Crew
from crewai_tools import DirectoryReadTool, FileReadTool, ScrapeWebsiteTool
from crewai.llm import LLM

# === Step 1: Set your OpenAI API key ===
os.environ["OPENAI_API_KEY"] = "your api key"

# === Step 2: Create LLM instance (OpenAI) ===
# === Step 2: Initialize LLM with a high-performing model ===
llm = LLM(model="gpt-4-turbo")  # Upgraded from gpt-3.5-turbo

# === Step 3: Input target URL ===
target_url = input("Enter the website URL to scrape: ").strip()
if not target_url.startswith(("http://", "https://")):
    target_url = "https://" + target_url


# === Step 5: Define tools ===
scrape_tool = ScrapeWebsiteTool()
file_tool = FileReadTool()

# === Step 6: Define Agents with URL Context ===
web_scraper_agent = Agent(
    role="Website Scraper",
    goal=f"Extract complete HTML and CSS from the target website: {target_url}",
    backstory="A professional website scraping bot that fetches full-page HTML and all related CSS content, including external stylesheets and inline styles.",
    tools=[scrape_tool],
    llm=llm,
    verbose=True
)

code_analyzer_agent = Agent(
    role="HTML/CSS Code Analyzer",
    goal=f"Analyze the HTML and CSS scraped from the website {target_url} for structure, accessibility, redundancy, and style clarity.",
    backstory="A senior front-end expert with deep experience in identifying problems in HTML markup and CSS design systems.",
    tools=[file_tool],
    llm=llm,
    verbose=True
)

reporting_agent = Agent(
    role="Technical Report Generator",
    goal=f"Create a summarized, developer-friendly report based on the analysis of the website: {target_url}.",
    backstory="A helpful assistant who transforms technical audits into clear reports with strengths, flaws, and practical suggestions.",
    tools=[file_tool],
    llm=llm,
    verbose=True
)

# === Step 7: Define Tasks ===
scrape_task = Task(
    description=(
        f"Use your tools to scrape the website at {target_url}. "
        "Extract full HTML content, collect inline CSS, and fetch all linked external CSS files. "
        "Embed all styles into a single HTML structure. "
        "Save everything including the code of html and css in 'scraped_content/index.html'."
    ),
    expected_output="A complete HTML file with all styles embedded.",
    agent=web_scraper_agent,
    output_file='scraped_content/index.html'
)

analyze_task = Task(
    description=(
        "Read the file 'scraped_content/index.html'. Analyze it for:\n"
        "- HTML structure and semantic correctness\n"
        "- Accessibility (alt tags, ARIA, headings)\n"
        "- CSS quality (repetition, responsiveness, conflicts)\n"
        "- General best practices\n"
        "Save the results in 'analysis/web_code_analysis.md'."
    ),
    expected_output="A markdown report detailing all code issues and strengths.",
    agent=code_analyzer_agent,
    output_file='analysis/web_code_analysis.md'
)

report_task = Task(
    description=(
        "Read 'analysis/web_code_analysis.md' and summarize it into a final report with:\n"
        "1. Summary of strengths\n"
        "2. Key issues found\n"
        "3. Suggested fixes\n"
        "Save it as 'reports/final_report.md'. Keep it developer-friendly and avoid unnecessary jargon."
    ),
    expected_output="Markdown report with clear sections on strengths, issues, and recommendations.",
    agent=reporting_agent,
    output_file='reports/final_report.md'
)

# === Step 8: Create Crew and Run ===
crew = Crew(
    agents=[web_scraper_agent, code_analyzer_agent, reporting_agent],
    tasks=[scrape_task, analyze_task, report_task],
    process="sequential",
    verbose=True
)

crew.kickoff()
