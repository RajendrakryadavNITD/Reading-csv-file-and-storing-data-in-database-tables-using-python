import os
from flask import current_app
from excel_reader import excel_sheet_reader, sample_data_vo, csv_file_reader
from excel_reader.dal import connection_factory
from excel_reader.dao import dao_factory
from xlrd import open_workbook

class CsvFileHelper(object):
    def get_connection(self, existing_conn=None):
        is_new_connection = False
        conn = None
        try:
            if existing_conn is None:
                myconn = connection_factory.ConnectionFactory.create()
                conn = myconn.getconnection()
                is_new_connection = True
            else:
                conn = existing_conn
            return conn
        except:
            raise


    def save_csv_file_info_list(self, excel_sheet_info_list, existing_conn=None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.get_excel_sheet_dao(conn)
            count = 0
            if excel_sheet_info_list is not None and len(excel_sheet_info_list) > 0:
                for excel_sheet_info in excel_sheet_info_list:
                    if count == 10:
                        break
                    dao.insert_excel_sheet_data(excel_sheet_info)
                    count+=1
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()

    def get_csv_file_info_list(self, start_limit, count, existing_conn=None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.get_excel_sheet_dao(conn)
            excel_sheet_info_list = dao.get_excel_sheet_info_list(start_limit, count)
            return excel_sheet_info_list
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()


    def save_csv_file_info(self, csv_path, existing_conn=None):
        conn = None

        try:
            if csv_path is not None:
                excel_sheet_info_list = csv_file_reader.CsvFileReader().manipulation_of_csv_data_list(csv_path)
                self.save_csv_file_info_list(excel_sheet_info_list, conn)
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()
