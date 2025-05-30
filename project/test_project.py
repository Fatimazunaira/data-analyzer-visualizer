import pandas as pd
import pytest
import os
from project import load_csv, filter_data, export_data, show_basic_info

# --------- Test load_csv ---------

def test_load_csv_valid():
    df = load_csv("employees.csv")
    assert not df.empty
    assert isinstance(df, pd.DataFrame)

def test_load_csv_invalid():
    df = load_csv("non_existing_file.csv")
    assert df is None


# --------- Test filter_data ---------

def test_filter_data_found():
    df = pd.DataFrame({
        'Name': ['Ali', 'Sara', 'Ahmed'],
        'Department': ['IT', 'HR', 'Finance']
    })
    filtered = filter_data(df, 'Department', 'IT')
    assert len(filtered) == 1
    assert filtered.iloc[0]['Name'] == 'Ali'

def test_filter_data_not_found():
    df = pd.DataFrame({
        'Name': ['Ali', 'Sara'],
        'Department': ['IT', 'HR']
    })
    filtered = filter_data(df, 'Department', 'Marketing')
    assert filtered.empty


# --------- Test export_data ---------

def test_export_data():
    df = pd.DataFrame({'A': [1, 2, 3]})
    filename = "test_export.csv"
    export_data(df, filename)
    assert os.path.exists(filename)

    # Cleanup
    os.remove(filename)


# --------- Test show_basic_info ---------
def test_show_basic_info_empty():
    df = pd.DataFrame()  # Empty DataFrame
    info = show_basic_info(df)
    
    # Test if the function returns the correct message for empty DataFrame
    assert isinstance(info, str)
    assert "empty" in info.lower()  # Ensure message mentions "empty"


# --------- Edge Case Tests ---------

def test_filter_data_case_sensitivity():
    df = pd.DataFrame({
        'Department': ['IT', 'it', 'It']
    })
    filtered = filter_data(df, 'Department', 'IT')
    assert len(filtered) == 1  # Because exact match is case-sensitive

def test_filter_data_invalid_column():
    df = pd.DataFrame({'Name': ['Ali', 'Sara']})
    with pytest.raises(ValueError):
        filter_data(df, 'InvalidColumn', 'Value')
