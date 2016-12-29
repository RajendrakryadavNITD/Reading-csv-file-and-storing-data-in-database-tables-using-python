from excel_reader.excel_file_helper import csv_file_helper

def save_csv_file_info():
    csv_path = 'd:\\excel_sheets\\Sample-Data.csv'
    # csv_file_helper.CsvFileHelper().save_csv_file_info(csv_path)

save_csv_file_info()

def get_csv_file_info_list():
    csv_file_helper.CsvFileHelper().get_csv_file_info_list(1, 15)
get_csv_file_info_list()