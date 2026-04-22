import kagglehub
import pandas as pd
import glob
import os
import shutil

def main():
    print("Downloading dataset from Kaggle...")
    # Load the latest version
    path = kagglehub.dataset_download("patricklford/americans-belief-in-spiritual-concepts")
    
    print(f"Downloaded to: {path}")
    
    # Find the CSV file in the downloaded path
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    
    if not csv_files:
        print("No CSV files found in the dataset.")
        return
        
    csv_file = csv_files[0]
    
    # Save a copy to our data folder
    dest_path = os.path.join(os.path.dirname(__file__), 'data', 'beliefs.csv')
    shutil.copy(csv_file, dest_path)
    
    print(f"Dataset successfully copied to {dest_path}")
    
    # Verify by reading the first 5 rows
    df = pd.read_csv(dest_path)
    print("First 5 records:")
    print(df.head())

if __name__ == "__main__":
    main()
