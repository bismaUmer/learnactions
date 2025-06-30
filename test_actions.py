import pytest
from playwright.sync_api import sync_playwright


def test_launch_google():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com")
        assert "Googlle" in page.title()  # Simple validation
        print("Google launched and title verified")
        browser.close()
