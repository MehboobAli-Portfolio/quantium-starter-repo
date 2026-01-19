import os
import pytest
from app import app
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# --- THE FIX: FORCE PATH INJECTION ---
# This block ensures that even if the terminal is confused, 
# the Python process knows exactly where the driver is.
driver_path = ChromeDriverManager().install()
driver_dir = os.path.dirname(driver_path)
if driver_dir not in os.environ["PATH"]:
    # Add to the start of PATH to ensure it is found first
    os.environ["PATH"] = driver_dir + os.pathsep + os.environ["PATH"]
# -------------------------------------

def pytest_setup_options():
    options = webdriver.ChromeOptions()
    # Headless mode is essential for CI/Bash environments
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return options

# 1. Test for the Header
def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "PINK MORSEL: SALES ARENA"

# 2. Test for the Visualisation
def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

# 3. Test for the Region Picker
def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    picker = dash_duo.find_element("#region-filter")
    assert picker is not None