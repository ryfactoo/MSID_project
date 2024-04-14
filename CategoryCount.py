# zliczanie z wsyztskich plików csv


# import csv
# import glob
#
# category_counts = {}
#
# directory_path = r"D:\Studia\4 semestr\MSID\L\Projekt MSID\datebase_yt"
#
# txt_files = glob.glob(directory_path + "/*.csv")
#
# for file_path in txt_files:
#     file_name = file_path.split("/")[-1]
#     with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             category_id = row['categoryId']
#             if category_id in category_counts:
#                 category_counts[category_id] += 1
#             else:
#                 category_counts[category_id] = 1
#
# # Wyświetlenie wyników
# for category_id, count in category_counts.items():
#     print(f"CategoryId: {category_id}, Count: {count}")




# zliczanie z jednego pliku csv


import csv

category_counts = {}

with open('datebase_yt/youtube_database.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        category_id = row['categoryId']
        if category_id in category_counts:
            category_counts[category_id] += 1
        else:
            category_counts[category_id] = 1

for category_id, count in category_counts.items():
    print(f"CategoryId: {category_id}, Count: {count}")
