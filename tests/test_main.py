# tests/test_main.py

import sys
import os
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import load_data

def test_load_data():
    df = load_data()
    print(f"DataFrame shape: {df.shape}")  # Debug info
    assert not df.empty, "DataFrame should not be empty"
