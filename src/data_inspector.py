"""
Quick data inspection utility
"""
import pandas as pd
import numpy as np

def inspect_data(filepath):
    """Perform initial data inspection"""
    print("="*80)
    print("GLOBAL WEATHER REPOSITORY - INITIAL INSPECTION")
    print("="*80)
    
    # Load data
    df = pd.read_csv(filepath)
    
    print(f"\n📊 Dataset Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"💾 Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    print("\n" + "="*80)
    print("COLUMN OVERVIEW")
    print("="*80)
    print(df.dtypes)
    
    print("\n" + "="*80)
    print("MISSING VALUES")
    print("="*80)
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing': missing,
        'Percentage': missing_pct
    }).sort_values('Missing', ascending=False)
    print(missing_df[missing_df['Missing'] > 0])
    
    print("\n" + "="*80)
    print("FIRST FEW ROWS")
    print("="*80)
    print(df.head())
    
    print("\n" + "="*80)
    print("NUMERICAL STATISTICS")
    print("="*80)
    print(df.describe())
    
    print("\n" + "="*80)
    print("UNIQUE VALUES IN KEY COLUMNS")
    print("="*80)
    for col in df.columns:
        unique_count = df[col].nunique()
        if unique_count < 50:  # Show only for categorical-like columns
            print(f"{col}: {unique_count} unique values")
    
    return df

if __name__ == "__main__":
    df = inspect_data('data/GlobalWeatherRepository.csv')
