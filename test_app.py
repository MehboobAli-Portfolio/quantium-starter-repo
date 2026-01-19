import os
from app import app
from webdriver_manager.chrome import ChromeDriverManager

# --- AUTOMATIC DRIVER CONFIGURATION ---
# This downloads the correct driver and adds its folder to your system PATH
# so that dash_duo can find 'chromedriver' without manual setup.
driver_path = ChromeDriverManager().install()
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)
# ---------------------------------------

# 1. Test for the Header
def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "PINK MORSEL: SALES ARENA"

# 2. Test for the Visualisation
def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    # Note: Using the ID we set in app.py
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

# 3. Test for the Region Picker
def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    # Note: Using the ID we set in app.py
    picker = dash_duo.find_element("#region-filter")
    assert picker is not None