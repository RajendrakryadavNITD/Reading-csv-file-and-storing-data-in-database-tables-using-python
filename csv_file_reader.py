import csv
from excel_reader import sample_data_vo
class CsvFileReader(object):
    def read_excel_sheet_info(self, csv_path):
        try:
            excel_info_list = []
            f = open(csv_path, 'rb')
            reader = csv.reader(f)
            for row in reader:
                excel_info_list.append(row)
            f.close()
            return excel_info_list
        except:
            raise

    def manipulation_of_csv_data_list(self, csv_path):
        try:
            final_list = []
            count = 0
            excel_info_list_of_list = self.read_excel_sheet_info(csv_path)
            for excel_info_list in excel_info_list_of_list:
                if count == 0:
                    count+=1
                    continue
                excel_sheet_info = sample_data_vo.SampleDataVo()
                excel_sheet_info.id_number = excel_info_list[0]
                excel_sheet_info.database_Category = excel_info_list[1]
                excel_sheet_info.business_name = excel_info_list[2]
                excel_sheet_info.add1 = excel_info_list[3]
                excel_sheet_info.add2 = excel_info_list[4]
                excel_sheet_info.locality = excel_info_list[5]
                excel_sheet_info.town = excel_info_list[6]
                excel_sheet_info.county = excel_info_list[7]
                excel_sheet_info.postcode = excel_info_list[8]
                excel_sheet_info.Area = excel_info_list[9]
                excel_sheet_info.postcodearea = excel_info_list[10]
                excel_sheet_info.postcodesubarea = excel_info_list[11]
                excel_sheet_info.LineOfBusiness = excel_info_list[12]
                excel_sheet_info.sicnumeric = excel_info_list[13]
                excel_sheet_info.SIC_Description = excel_info_list[14]
                excel_sheet_info.telephone = excel_info_list[15]
                excel_sheet_info.tps = excel_info_list[16]
                excel_sheet_info.fax = excel_info_list[17]
                excel_sheet_info.fps = excel_info_list[18]
                excel_sheet_info.employeesnumeric = excel_info_list[19]
                excel_sheet_info.premises_type = excel_info_list[20]
                excel_sheet_info.title1 = excel_info_list[21]
                excel_sheet_info.fname1 = excel_info_list[22]
                excel_sheet_info.sname1 = excel_info_list[23]
                excel_sheet_info.position1 = excel_info_list[24]
                excel_sheet_info.email = excel_info_list[25]
                excel_sheet_info.Email_Address = excel_info_list[26]
                final_list.append(excel_sheet_info)
            return final_list
        except:
            raise

