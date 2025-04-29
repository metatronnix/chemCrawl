import asyncio
from playwright.async_api import async_playwright

from playwright.async_api import async_playwright

# need to store the URL in a settings file - for now, for proof of concept, just hard-code.
async def fetch_pubchem_data():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://pubchem.ncbi.nlm.nih.gov/#query=ketamine&tab=compound")
        await page.wait_for_timeout(5000)
        await browser.close()
