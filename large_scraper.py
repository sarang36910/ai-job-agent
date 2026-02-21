from playwright.sync_api import sync_playwright
import psycopg2
import time


# database connection

conn = psycopg2.connect(

    host="aws-1-ap-northeast-1.pooler.supabase.com",

    database="postgres",

    user="postgres.idszbogxpqxoberjaoga",

    password="JobAgent@123",

    port=6543

)

cursor = conn.cursor()


# job roles

roles = [

    "data-analyst-jobs",

    "data-scientist-jobs",

    "data-engineer-jobs",

    "python-developer-jobs"

]


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()


    for role in roles:

        for page_num in range(1,6):

            url = f"https://www.naukri.com/{role}-{page_num}"

            print("Scraping:", url)

            page.goto(url)

            page.wait_for_timeout(4000)

            jobs = page.locator("div.srp-jobtuple-wrapper")

            count = jobs.count()

            print("Found:", count)


            for i in range(count):

                job = jobs.nth(i)


                title = job.locator("a.title").inner_text() if job.locator("a.title").count() else ""

                company = job.locator("a.comp-name").inner_text() if job.locator("a.comp-name").count() else ""

                exp = job.locator("span.expwdth").inner_text() if job.locator("span.expwdth").count() else ""

                location = job.locator("span.locWdth").inner_text() if job.locator("span.locWdth").count() else ""

                link = job.locator("a.title").get_attribute("href") if job.locator("a.title").count() else ""


                cursor.execute("""

                INSERT INTO jobs (title, company, experience, location, link)

                VALUES (%s, %s, %s, %s, %s)

                """,

                (title, company, exp, location, link)

                )


            conn.commit()

            time.sleep(3)


    browser.close()

cursor.close()

conn.close()

print("Large scraping completed")
