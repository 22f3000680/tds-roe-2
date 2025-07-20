# scrape.py
import asyncio
from playwright.async_api import async_playwright

urls = [
    "https://example.com/seed35",
    "https://example.com/seed36",
    "https://example.com/seed37",
    "https://example.com/seed38",
    "https://example.com/seed39",
    "https://example.com/seed40",
    "https://example.com/seed41",
    "https://example.com/seed42",
    "https://example.com/seed43",
    "https://example.com/seed44",
]

async def main():
    total = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for url in urls:
            await page.goto(url)
            await page.wait_for_selector("table")  # Wait until table appears
            numbers = await page.eval_on_selector_all(
              "table td",
              "elements => elements.map(e => parseFloat(e.textContent)).filter(n => !isNaN(n))"
            )
            print(f"{url}: {numbers}")  # Debug
            total += sum(numbers)
        print(f"Sum: {total}")
        await browser.close()

asyncio.run(main())
