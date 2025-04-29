import asyncio
from django.core.management.base import BaseCommand
from pubchem_crawler.crawler import fetch_pubchem_data

class Command(BaseCommand):
    help = 'Crawls PubChem for specified compound'

    def handle(self, *args, **kwargs):
        print("🚀 Management command started.")
        asyncio.run(fetch_pubchem_data())
        print("✅ Management command finished.")
        self.stdout.write(self.style.SUCCESS('Crawl completed.'))