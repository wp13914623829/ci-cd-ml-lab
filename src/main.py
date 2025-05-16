import pandas as pd

def load_data():
    data = {
        'name': ['Alice', 'Bob'],
        'age': [25, 30]
    }
    return pd.DataFrame(data)