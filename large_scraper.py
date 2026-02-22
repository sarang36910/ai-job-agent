import time
import psycopg2
from playwright.sync_api import sync_playwright


# -----------------------------
# SUPABASE CONNECTION
# -----------------------------

conn = psycopg2.connect(

    host="aws-1-ap-northeast-1.pooler.supabase.com",
    database="postgres",
    user="postgres.idszbogxpqxoberjaoga",
    password="JobAgent@123",
    port=6543

)

cursor = conn.cursor()


# -----------------------------
# CREATE TABLE IF NOT EXISTS
# -----------------------------

cursor.execute("""

CREATE TABLE IF NOT EXISTS jobs (

    id SERIAL PRIMARY KEY,

    title TEXT,

    company TEXT,

    experience TEXT,

    location TEXT,

    link TEXT UNIQUE,

    scraped_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)

""")

conn.commit()


# -----------------------------
# JOB ROLES TO SCRAPE
# -----------------------------

roles = [

    "data-analyst-jobs",

    "data-scientist-jobs",

    "data-engineer-jobs",

    "python-developer-jobs",

    "machine-learning-engineer-jobs",

    "ai-engineer-jobs",

    "business-analyst-jobs",

    "sql-developer-jobs",

    "power-bi-jobs"

]


# -----------------------------
# SCRAPER
# -----------------------------


# -----------------------------
# SCRAPER
# -----------------------------

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True,
        args=[
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-blink-features=AutomationControlled"
        ]
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
        viewport={"width": 1920, "height": 1080}
    )

    page = context.new_page()

    # IMPORTANT: for loop must align like this
    for role in roles:

        print(f"Scraping role: {role}")

        for page_num in range(1, 21):

            url = f"https://www.naukri.com/{role}-{page_num}"

            print(url)

            try:

                page.goto(url, timeout=60000)

                page.wait_for_timeout(5000)

                page.wait_for_selector("article", timeout=10000)

                jobs = page.query_selector_all("article")

                print("Found jobs:", len(jobs))

                for job in jobs:

                    title = job.query_selector("a.title").inner_text()
                    company = job.query_selector(".comp-name").inner_text()
                    experience = job.query_selector(".expwdth").inner_text()
                    location = job.query_selector(".locWdth").inner_text()
                    link = job.query_selector("a.title").get_attribute("href")

                    cursor.execute(
                        """
                        INSERT INTO jobs (title, company, experience, location, link)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (link) DO NOTHING
                        """,
                        (title, company, experience, location, link)
                    )

                    conn.commit()

            except Exception as e:

                print("Page error:", e)

    browser.close()


cursor.close()

conn.close()


print("Scraping completed successfully")


