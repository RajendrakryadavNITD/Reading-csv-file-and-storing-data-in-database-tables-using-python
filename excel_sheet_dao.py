import queries
from sqlalchemy.sql import text
from sqlalchemy import exc
from excel_reader.dal import dbcondao
from excel_reader import sample_data_vo
class ExcelDao(dbcondao.DbConDao):
    def insert_excel_sheet_data(self, excel_sheet_info):
        try:
            if excel_sheet_info is not None :
                query = text(queries.Queries.insert_sample_data_info)
                conn = super(ExcelDao, self).getconnection()

                values = {'excel_id': excel_sheet_info._id_number ,
                          'databasecategory': excel_sheet_info._database_Category,
                          'businessname': excel_sheet_info._business_name ,
                          'address1':excel_sheet_info._add1 ,
                          'address2': excel_sheet_info._add2 ,
                          'locality': excel_sheet_info._locality ,
                          'town': excel_sheet_info._town,
                          'country': excel_sheet_info._county ,
                          'postcode': excel_sheet_info._postcode ,
                          'area': excel_sheet_info._Area ,
                          'postcodearea': excel_sheet_info._postcodearea ,
                          'postcodesubarea': excel_sheet_info._postcodesubarea ,
                          'lineofbusiness' : excel_sheet_info._LineOfBusiness  ,
                          'sicnumeric': excel_sheet_info._sicnumeric ,
                          'sicdiscription': excel_sheet_info._SIC_Description ,
                          'telephone' :excel_sheet_info._telephone ,
                          'tps': excel_sheet_info._tps ,
                          'fax': excel_sheet_info._fax ,
                          'fps': excel_sheet_info._fps,
                          'employeesnumeric': excel_sheet_info._employeesnumeric,
                          'premisestype' :excel_sheet_info._premises_type,
                          'title1': excel_sheet_info._title1,
                          'fname':excel_sheet_info._fname1 ,
                          'sname': excel_sheet_info._sname1,
                          'position1': excel_sheet_info._position1,
                          'email': excel_sheet_info._email,
                          'emailaddress': excel_sheet_info._Email_Address}
                conn.execute(query, values)
        except exc.SQLAlchemyError:
            raise
        except:
            raise


    def get_excel_sheet_info_list(self, start_limit, count):
        try:
            query = text(queries.Queries.get_excel_sheet_info)
            conn = super(ExcelDao, self).getconnection()
            values = {'startlimit': start_limit, 'count': count}
            result = conn.execute(query, values).fetchall()
            excel_sheet_info_list = []
            for row in result:
                excel_sheet_info = sample_data_vo.SampleDataVo()
                excel_sheet_info.id=row['id']
                excel_sheet_info.id_number =row ['excel_id']
                excel_sheet_info.database_Category = row ['databasecategory']
                excel_sheet_info.business_name = row ['businessname']
                excel_sheet_info.add1 = row ['address1']
                excel_sheet_info.add2 = row ['address2']
                excel_sheet_info.locality = row ['locality']
                excel_sheet_info.town = row ['town']
                excel_sheet_info.county = row ['country']
                excel_sheet_info.postcode = row ['postcode']
                excel_sheet_info.Area = row ['area']
                excel_sheet_info.postcodearea = row ['postcodearea']
                excel_sheet_info.postcodesubarea = row ['postcodesubarea']
                excel_sheet_info.LineOfBusiness = row ['lineofbusiness']
                excel_sheet_info.sicnumeric = row ['sicnumeric']
                excel_sheet_info.SIC_Description = row ['sicdiscription']
                excel_sheet_info.telephone = row ['telephone']
                excel_sheet_info.tps = row ['tps']
                excel_sheet_info.fax = row ['fax']
                excel_sheet_info.fps = row ['fps']
                excel_sheet_info.employeesnumeric = row ['employeesnumeric']
                excel_sheet_info.premises_type = row ['premisestype']
                excel_sheet_info.title1 = row ['title1']
                excel_sheet_info.fname1 = row ['fname']
                excel_sheet_info.sname1 = row ['sname']
                excel_sheet_info.position1 = row ['position1']
                excel_sheet_info.email = row ['email']
                excel_sheet_info.Email_Address = row ['emailaddress']
                excel_sheet_info_list.append(excel_sheet_info)
            return excel_sheet_info_list
        except exc.SQLAlchemyError:
            raise
        except:
            raise
