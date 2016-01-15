python -m models.create_all_tables --drop_tables Y
python -m models.create_all_tables --create_tables Y
python -m models.master --load_csv Master.csv
python -m models.batting --load_csv Batting.csv