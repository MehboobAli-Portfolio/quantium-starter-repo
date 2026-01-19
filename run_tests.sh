#!/bin/bash

# 1. Run tests using the venv's python directly.
# This bypasses the 'uname' error and ensures the correct environment is used.
./venv/Scripts/python.exe -m pytest test_app.py

# 2. Capture the result
PYTEST_EXIT_CODE=$?

# 3. Exit logic for the Bonus Task requirement
if [ $PYTEST_EXIT_CODE -eq 0 ]; then
    echo "SUCCESS: All tests passed!"
    exit 0
else
    echo "FAILURE: Tests failed. Check the logs above."
    exit 1
fi