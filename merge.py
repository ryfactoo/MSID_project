import pandas as pd
import glob
from config import api_key

# Ścieżka do katalogu, w którym znajdują się pliki CSV
directory_path = r"D:\Studia\4 semestr\MSID\L\Projekt MSID\datebase v2"

# Wyszukiwanie plików CSV
csv_files = glob.glob(directory_path + "/*.csv")

# Tworzenie pustego obiektu DataFrame
combined_data = pd.DataFrame()

# Łączenie plików CSV
for file_path in csv_files:
    df = pd.read_csv(file_path)
    combined_data = pd.concat([combined_data, df])

# Zapisanie połączonych danych do nowego pliku CSV
combined_data.to_csv("merged_all_csv.csv", index=False)